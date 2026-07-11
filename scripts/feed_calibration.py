#!/usr/bin/env python3
"""Prepare and evaluate monthly human reviews of the feed analyzer."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIGEST = ROOT / "site/data/feed-digest.json"
REVIEW_DIR = ROOT / "calibration/reviews"
REPORT_DIR = ROOT / "calibration/reports"
CATEGORIES = {"genai", "security", "data", "network", "operations", "cost", "certification", "deprecation"}
PRIORITIES = {"今すぐ確認", "今週確認", "記録のみ"}


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc


def review_path(month: str) -> Path:
    return REVIEW_DIR / f"{month}.json"


def report_path(month: str) -> Path:
    return REPORT_DIR / f"{month}.md"


def validate_month(value: str) -> str:
    try:
        parsed = date.fromisoformat(f"{value}-01")
    except ValueError as exc:
        raise ValueError("month must be YYYY-MM") from exc
    return parsed.strftime("%Y-%m")


def validate_review(review: dict[str, Any]) -> None:
    if review.get("schema_version") != 1 or not isinstance(review.get("items"), list):
        raise ValueError("review schema_version=1 and items are required")
    validate_month(review.get("month", ""))
    seen: set[str] = set()
    for item in review["items"]:
        required = {
            "id", "vendor", "title", "url", "predicted_category", "predicted_priority",
            "score", "actual_category", "actual_priority", "notes",
        }
        if not required.issubset(item):
            raise ValueError(f"review item missing fields: {required - set(item)}")
        if item["id"] in seen:
            raise ValueError(f"duplicate review item: {item['id']}")
        seen.add(item["id"])
        if item["predicted_category"] not in CATEGORIES:
            raise ValueError(f"invalid predicted category: {item['predicted_category']}")
        if item["predicted_priority"] not in PRIORITIES:
            raise ValueError(f"invalid predicted priority: {item['predicted_priority']}")
        if item["actual_category"] is not None and item["actual_category"] not in CATEGORIES:
            raise ValueError(f"invalid actual category: {item['actual_category']}")
        if item["actual_priority"] is not None and item["actual_priority"] not in PRIORITIES:
            raise ValueError(f"invalid actual priority: {item['actual_priority']}")


def prepare(digest: dict[str, Any], month: str, limit: int, existing: dict[str, Any] | None = None) -> dict[str, Any]:
    if limit < 1:
        raise ValueError("limit must be positive")
    previous = {item["id"]: item for item in (existing or {}).get("items", [])}
    items = []
    for source in digest.get("items", [])[:limit]:
        prior = previous.get(source["id"], {})
        items.append({
            "id": source["id"],
            "vendor": source["vendor"],
            "title": source["title"],
            "url": source["url"],
            "predicted_category": source["category"],
            "predicted_priority": source["priority"],
            "score": source["score"],
            "actual_category": prior.get("actual_category"),
            "actual_priority": prior.get("actual_priority"),
            "notes": prior.get("notes", ""),
        })
    review = {
        "schema_version": 1,
        "month": month,
        "digest_generated_at": digest.get("generated_at", ""),
        "instructions": {
            "actual_category": sorted(CATEGORIES),
            "actual_priority": ["今すぐ確認", "今週確認", "記録のみ"],
            "rule": "公式リンクを確認してactual_*を入力する。判断不能はnullのままにする。",
        },
        "items": items,
    }
    validate_review(review)
    return review


def ratio(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 4) if denominator else None


def evaluate(review: dict[str, Any]) -> dict[str, Any]:
    validate_review(review)
    category_items = [item for item in review["items"] if item["actual_category"] is not None]
    priority_items = [item for item in review["items"] if item["actual_priority"] is not None]
    category_correct = sum(item["predicted_category"] == item["actual_category"] for item in category_items)

    tp = sum(
        item["predicted_priority"] == "今すぐ確認" and item["actual_priority"] == "今すぐ確認"
        for item in priority_items
    )
    fp = sum(
        item["predicted_priority"] == "今すぐ確認" and item["actual_priority"] != "今すぐ確認"
        for item in priority_items
    )
    fn = sum(
        item["predicted_priority"] != "今すぐ確認" and item["actual_priority"] == "今すぐ確認"
        for item in priority_items
    )
    precision = ratio(tp, tp + fp)
    recall = ratio(tp, tp + fn)
    f1 = None
    if precision is not None and recall is not None and precision + recall:
        f1 = round(2 * precision * recall / (precision + recall), 4)

    errors = [
        {
            "id": item["id"],
            "title": item["title"],
            "predicted_category": item["predicted_category"],
            "actual_category": item["actual_category"],
            "predicted_priority": item["predicted_priority"],
            "actual_priority": item["actual_priority"],
            "notes": item["notes"],
        }
        for item in review["items"]
        if (item["actual_category"] is not None and item["predicted_category"] != item["actual_category"])
        or (item["actual_priority"] is not None and item["predicted_priority"] != item["actual_priority"])
    ]
    return {
        "month": review["month"],
        "total": len(review["items"]),
        "category_labeled": len(category_items),
        "priority_labeled": len(priority_items),
        "category_accuracy": ratio(category_correct, len(category_items)),
        "urgent_precision": precision,
        "urgent_recall": recall,
        "urgent_f1": f1,
        "urgent_true_positive": tp,
        "urgent_false_positive": fp,
        "urgent_false_negative": fn,
        "errors": errors,
    }


def percent(value: float | None) -> str:
    return "—" if value is None else f"{value * 100:.1f}%"


def build_report(metrics: dict[str, Any]) -> str:
    lines = [
        f"# Feed classifier calibration — {metrics['month']}",
        "",
        "## Metrics",
        "",
        "| 指標 | 値 |",
        "|---|---:|",
        f"| レビュー対象 | {metrics['total']} |",
        f"| カテゴリ入力済み | {metrics['category_labeled']} |",
        f"| 優先度入力済み | {metrics['priority_labeled']} |",
        f"| カテゴリ正解率 | {percent(metrics['category_accuracy'])} |",
        f"| 緊急Precision | {percent(metrics['urgent_precision'])} |",
        f"| 緊急Recall | {percent(metrics['urgent_recall'])} |",
        f"| 緊急F1 | {percent(metrics['urgent_f1'])} |",
        f"| 緊急見逃し (FN) | {metrics['urgent_false_negative']} |",
        f"| 緊急過検知 (FP) | {metrics['urgent_false_positive']} |",
        "",
        "## Errors",
        "",
        "| 更新 | カテゴリ (予測→正解) | 優先度 (予測→正解) | メモ |",
        "|---|---|---|---|",
    ]
    if not metrics["errors"]:
        message = "ラベル未入力" if not metrics["category_labeled"] and not metrics["priority_labeled"] else "誤りなし"
        lines.append(f"| — | — | — | {message} |")
    for item in metrics["errors"]:
        title = item["title"].replace("|", "\\|")
        notes = item["notes"].replace("|", "\\|") or "—"
        lines.append(
            f"| {title} | {item['predicted_category']} → {item['actual_category'] or '—'} | "
            f"{item['predicted_priority']} → {item['actual_priority'] or '—'} | {notes} |"
        )
    lines.extend([
        "",
        "## Decision rule",
        "",
        "緊急Recallを最優先する。見逃しが1件でもあれば、該当語を明示ルールへ追加してテストを作成する。過検知だけの場合はタイトル一致と本文一致の重みを先に調整する。",
    ])
    return "\n".join(lines) + "\n"


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare_parser = subparsers.add_parser("prepare")
    prepare_parser.add_argument("--month", default=date.today().strftime("%Y-%m"))
    prepare_parser.add_argument("--digest", type=Path, default=DEFAULT_DIGEST)
    prepare_parser.add_argument("--limit", type=int, default=20)
    evaluate_parser = subparsers.add_parser("evaluate")
    evaluate_parser.add_argument("--month", default=date.today().strftime("%Y-%m"))
    subparsers.add_parser("check")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "prepare":
            month = validate_month(args.month)
            path = review_path(month)
            existing = load_json(path) if path.exists() else None
            review = prepare(load_json(args.digest), month, args.limit, existing)
            write_json(path, review)
            print(f"prepared {len(review['items'])} items: {path}")
        elif args.command == "evaluate":
            month = validate_month(args.month)
            metrics = evaluate(load_json(review_path(month)))
            path = report_path(month)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build_report(metrics), encoding="utf-8")
            print(f"evaluated {metrics['category_labeled']}/{metrics['total']} category labels: {path}")
        else:
            files = sorted(REVIEW_DIR.glob("*.json"))
            for path in files:
                validate_review(load_json(path))
            print(f"valid: {len(files)} review files")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
