#!/usr/bin/env python3
"""Record practice-exam scores and build a compact Markdown report."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from statistics import mean
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "site/data/scores.json"
DEFAULT_REPORT = ROOT / "notes/score-report.md"


def load_data(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"score file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc
    validate_data(data)
    return data


def validate_data(data: dict[str, Any]) -> None:
    if data.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")
    if not isinstance(data.get("targets"), dict) or not isinstance(data.get("attempts"), list):
        raise ValueError("targets and attempts are required")
    for exam, target in data["targets"].items():
        if not exam or not isinstance(target, (int, float)) or not 0 <= target <= 100:
            raise ValueError(f"invalid target: {exam}={target}")
    seen: set[str] = set()
    for attempt in data["attempts"]:
        required = {"id", "date", "exam", "set", "attempt", "score", "weak_domains", "notes"}
        if not required.issubset(attempt):
            raise ValueError(f"attempt is missing fields: {required - set(attempt)}")
        try:
            date.fromisoformat(attempt["date"])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid date: {attempt.get('date')}") from exc
        if not isinstance(attempt["score"], (int, float)) or not 0 <= attempt["score"] <= 100:
            raise ValueError(f"invalid score: {attempt['score']}")
        if not isinstance(attempt["weak_domains"], list):
            raise ValueError("weak_domains must be a list")
        if attempt["id"] in seen:
            raise ValueError(f"duplicate id: {attempt['id']}")
        seen.add(attempt["id"])


def add_attempt(data: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    try:
        date.fromisoformat(args.date)
    except ValueError as exc:
        raise ValueError("--date must be YYYY-MM-DD") from exc
    if not 0 <= args.score <= 100:
        raise ValueError("--score must be between 0 and 100")
    if not args.exam.strip() or not args.set_name.strip():
        raise ValueError("--exam and --set must not be empty")

    related = [
        item for item in data["attempts"]
        if item["exam"].casefold() == args.exam.casefold()
        and item["set"].casefold() == args.set_name.casefold()
    ]
    attempt_number = max((item["attempt"] for item in related), default=0) + 1
    item_id = f"{args.date}:{args.exam}:{args.set_name}:{attempt_number}".lower().replace(" ", "-")
    item = {
        "id": item_id,
        "date": args.date,
        "exam": args.exam.strip(),
        "set": args.set_name.strip(),
        "attempt": attempt_number,
        "score": round(args.score, 1),
        "weak_domains": [value.strip() for value in args.weak_domains.split(",") if value.strip()],
        "notes": args.notes.strip(),
    }
    data["attempts"].append(item)
    data["attempts"].sort(key=lambda value: (value["date"], value["exam"], value["set"], value["attempt"]))
    validate_data(data)
    return item


def readiness(data: dict[str, Any], exam: str, scores: list[float]) -> tuple[str, str]:
    target = float(data["targets"].get(exam, 85))
    if not scores:
        return "未判定", "模試スコアを記録する"
    recent = scores[-3:]
    average = mean(recent)
    if len(recent) >= 2 and average >= target and min(recent) >= target - 3:
        return "受験候補", f"直近{len(recent)}回平均{average:.1f}%"
    if average >= target - 5:
        return "要確認", f"目標{target:.0f}%まで{target-average:.1f}pt"
    return "延期推奨", f"目標{target:.0f}%まで{target-average:.1f}pt"


def build_report(data: dict[str, Any]) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in data["attempts"]:
        grouped[item["exam"]].append(item)

    lines = [
        "# Practice exam score report",
        "",
        "`site/data/scores.json` から生成。受験判断は直近スコアだけでなく、弱点の再現性と本番日程も含めて行う。",
        "",
        "## Readiness",
        "",
        "| 試験 | 目標 | 直近 | 直近3回平均 | 判定 | 根拠 |",
        "|---|---:|---:|---:|---|---|",
    ]
    exams = sorted(set(data["targets"]) | set(grouped))
    for exam in exams:
        scores = [float(item["score"]) for item in grouped.get(exam, [])]
        status, reason = readiness(data, exam, scores)
        latest = f"{scores[-1]:.1f}%" if scores else "—"
        avg = f"{mean(scores[-3:]):.1f}%" if scores else "—"
        lines.append(f"| {exam} | {data['targets'].get(exam, 85)}% | {latest} | {avg} | {status} | {reason} |")

    lines.extend([
        "",
        "## Attempts",
        "",
        "| 日付 | 試験 | セット | 回 | 正答率 | 弱ドメイン | メモ |",
        "|---|---|---|---:|---:|---|---|",
    ])
    if not data["attempts"]:
        lines.append("| — | — | — | — | — | 未記録 | `score_tracker.py add` で追加 |")
    for item in sorted(data["attempts"], key=lambda value: value["date"], reverse=True):
        weak = ", ".join(item["weak_domains"]) or "—"
        notes = item["notes"].replace("|", "\\|") or "—"
        lines.append(
            f"| {item['date']} | {item['exam']} | {item['set']} | {item['attempt']} | "
            f"{item['score']:.1f}% | {weak} | {notes} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("check")
    subparsers.add_parser("report")
    add = subparsers.add_parser("add")
    add.add_argument("--date", default=date.today().isoformat())
    add.add_argument("--exam", required=True)
    add.add_argument("--set", dest="set_name", required=True)
    add.add_argument("--score", type=float, required=True)
    add.add_argument("--weak-domains", default="")
    add.add_argument("--notes", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = load_data(args.data)
        if args.command == "add":
            item = add_attempt(data, args)
            write_json(args.data, data)
            print(f"added {item['exam']} {item['set']} attempt {item['attempt']}: {item['score']:.1f}%")
        if args.command in {"add", "report"}:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(build_report(data), encoding="utf-8")
            print(f"wrote {args.report}")
        if args.command == "check":
            print(f"valid: {len(data['attempts'])} attempts")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
