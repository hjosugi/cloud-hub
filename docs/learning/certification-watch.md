# 資格情報の月次定点観測

資格ページの表を更新する前に、各providerの一次情報を同じ順序で確認する。検索結果や学習サイトの要約だけで状態を変更しない。

## Check sources

| Provider | Primary source | Check |
|---|---|---|
| AWS | [Coming soon to AWS Certification](https://aws.amazon.com/certification/coming-soon/) | 新試験、beta、改称、最終受験日 |
| Azure | [Credential retirement](https://learn.microsoft.com/credentials/support/credential-retirement) | 資格の廃止日、後継credential |
| Google Cloud | [Certification catalog](https://cloud.google.com/learn/certification) | Next更新告知、新資格、各exam guide |
| Google Cloud | [Exam terms](https://cloud.google.com/certification/terms) | validity、renewal eligibility、retake policy |
| OCI | [Oracle Certification](https://education.oracle.com/certification) / [MyLearn](https://mylearn.oracle.com/) | 当年の試験コード、受験可能状態、更新条件 |

## Observation log

### 2026-07-12

- AWS: Coming soonはSOA-C02 → CloudOps Engineer SOA-C03の既知更新を掲載。資格表へ追加すべき新しい2026年変更は確認できなかった。
- Azure: AZ-204は2026-07-31、AZ-500は2026-08-31に廃止予定。DP-100は2026-06-01、AI-102とAI-900は2026-06-30に廃止済みとなったため、サイトのfuture表記を修正した。
- Google Cloud: catalogはNext '26のGemini Enterprise Agent Platformとdata/analytics stackを各試験へ反映中と告知。Professional certificationのvalidityは3年ではなく2年のため修正した。PDEはstandard $200/2時間、renewal $100/1時間、どちらもvalidity 2年。
- OCI: 公開Certification landing pageから`-26`試験コードを確認できなかった。受験可能な`-26` trackをMyLearn/CertViewで確認できるまでは、サイトの`-25`表を推測で置換しない。

## Update rule

1. 日付と確認結果をこのlogへ追記する。
2. 状態・期限・料金・validityに差分がある場合だけ`site/cloud-hub.html`を更新する。
3. 後継資格は公式ページで名称またはcourse replacementを確認できた場合だけ記載する。
4. OCIの年次suffixは、検索結果ではなく受験可能な公式exam pageで確認してから切り替える。
