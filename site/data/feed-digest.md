# Cloud Hub release intelligence

生成日時: 2026-09-21T21:25:56.349123Z
取得元: 4/4、分析件数: 48

## 優先項目

### 今すぐ確認 (75) — GCP / 廃止・移行 / retirement

2026-09-14 [Gemini Enterprise Agent Platform — Deprecated: Gemini model deprecation and retirement date updates](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation、retirement、agent」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (73) — OCI / 廃止・移行 / retirement

2026-09-14 [Cohere Command A Vision and Cohere Embed 4 on-demand models deprecated in Abu Dhabi](https://docs.oracle.com/iaas/releasenotes/generative-ai/cohere-command-a-vision-embed-4-on-demand-deprecated-abudhabi.htm)

- 設計観点: 「deprecated、retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (73) — GCP / 廃止・移行 / deprecation

2026-09-09 [Looker — Deprecated: The deprecation of the Looker Mobile (Legacy) application has been postponed to January 31, 2027. Starting on January 31, 2027, support for ](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (72) — GCP / セキュリティ / security

2026-09-07 [AI Hypercomputer — Security: Google addressed a security vulnerability (CVE-2026-65107) that affects Slurm clusters. Based on the Google Cloud product that you used to c](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability、security」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今週確認 (71) — AZURE / 廃止・移行 / retirement

2026-09-16 [Retirement Update: SAP container images removed October 14, 2026](https://azure.microsoft.com/updates?id=571342)

- 設計観点: 「retired、retirement、agent」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (71) — GCP / 廃止・移行 / deprecation

2026-09-11 [Google SecOps SIEM — Deprecated: Deprecation of write permissions from the chronicle.readonly OAuth scope](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (71) — GCP / 廃止・移行 / deprecation

2026-09-11 [Google SecOps — Deprecated: Deprecation of write permissions from the chronicle.readonly OAuth scope](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (69) — AZURE / 廃止・移行 / retirement

2026-08-14 [Announcing: Azure Databricks Runtime 10.4 LTS will reach end of life on November 1, 2026](https://azure.microsoft.com/updates?id=569353)

- 設計観点: 「end of support、end of life」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (68) — GCP / 廃止・移行 / deprecation

2026-09-14 [Google SecOps SIEM — Deprecated: MANDIANT_ACTIVE_BREACH_IOC , MANDIANT_FUSION_IOC , and OPEN_SOURCE_INTEL_IOC` feeds are being removed](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (67) — AZURE / 廃止・移行 / retirement

2026-08-05 [Retirement: Nested confidential (cc_v5) VMs will be retired on September 1, 2026](https://azure.microsoft.com/updates?id=568661)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (66) — GCP / 生成AI / ga

2026-09-18 [Gemini Enterprise Agent Platform — Feature: xAI's Grok 4.6 is generally available](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、now available、introduces、agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-08-24 [Retirement: Support for Node 22 LTS ends on April 30, 2027](https://azure.microsoft.com/updates?id=567334)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (63) — GCP / 生成AI / update

2026-09-16 [Gemini Enterprise Agent Platform — Feature: CodeMender updates (v0.8.0)](https://docs.cloud.google.com/release-notes)

- 設計観点: 「introduces、guardrails、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (63) — AZURE / 廃止・移行 / retirement

2026-08-18 [Retirement: Azure VMware Solution License-included service will be retired August 30, 2027](https://azure.microsoft.com/updates?id=569535)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (63) — AZURE / 廃止・移行 / retirement

2026-08-12 [Retirement: Containerized data connector agent for the Microsoft Sentinel solution for SAP applications](https://azure.microsoft.com/updates?id=568457)

- 設計観点: 「retirement、agent」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (62) — AZURE / 廃止・移行 / retirement

2026-09-11 [Retirement: Azure Linux with OS Guard in Azure Kubernetes Service](https://azure.microsoft.com/updates?id=571257)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (60) — GCP / 生成AI / update

2026-09-21 [BigQuery — Feature: BigQuery generative AI functions now support the gemini-3.8-flash Gemini model.](https://docs.cloud.google.com/release-notes)

- 設計観点: 「gemini、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (60) — GCP / 廃止・移行 / deprecation

2026-09-14 [Cloud SQL for SQL Server — Deprecated: Beginning April 12, 2027, you won't be able to create new instances of Cloud SQL for SQL Server 2017. Starting on October 13, 2027, SQL Serv](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、end of life」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (58) — GCP / 生成AI / ga

2026-09-14 [Vertex AI Search — Feature: Agent Search: Search query add-ons for configurable pricing (GA)](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、vertex ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (58) — GCP / ネットワーク / ga

2026-09-09 [Gemini Enterprise Agent Platform — Feature: Computer Use and Shell sandboxes are generally available](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、gemini、network」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (57) — AWS / 生成AI / ga

2026-09-18 [Kimi K3 by Moonshot AI is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/moonshot-ai-kimi-k3-on-amazon-bedrock/)

- 設計観点: 「generally available、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (56) — AWS / 生成AI / ga

2026-09-18 [The new AgentCore Runtime is now available in Amazon Bedrock AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/09/new-agentcore-runtime-generally-available)

- 設計観点: 「now available、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (56) — OCI / 生成AI / ga

2026-09-10 [Use xAI Grok 4.6 in OCI Generative AI](https://docs.oracle.com/iaas/releasenotes/generative-ai/xai-grok-4-6.htm)

- 設計観点: 「now available、agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AWS / ネットワーク / update

2026-09-18 [AWS PrivateLink announces Tunnel Endpoints to access network segments](https://aws.amazon.com/about-aws/whats-new/2026/9/privatelink-tunnel-endpoint/)

- 設計観点: 「network、vpc、privatelink」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (54) — AZURE / ネットワーク / ga

2026-09-17 [[Launched] Generally Available: High-scale mesh in Azure Virtual Network Manager](https://azure.microsoft.com/updates?id=571572)

- 設計観点: 「generally available、general availability、network」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (54) — AWS / 生成AI / ga

2026-09-14 [granite-speech-4.1-2b, kanana-2-30b-a3b-instruct, and OpenFold3 models now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/granite-speech-4.1-2b-edge-kanana-2-30b-a3b-instruct-openfold3-jumpstart/)

- 設計観点: 「now available、agent、foundation model」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AWS / 生成AI / update

2026-09-11 [Amazon SageMaker HyperPod now supports model caching for faster inference autoscaling and reduced cold starts](https://aws.amazon.com/about-aws/whats-new/2026/09/sgm-hyperpod-model-caching-inf/)

- 設計観点: 「agent、rag」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AWS / 生成AI / update

2026-09-11 [Amazon Bedrock Managed Knowledge Base now supports multimodal embeddings for video, audio, and image content with TwelveLabs Marengo 3.0](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-managed-knowledge-base-multimodal-embeddings-twelvelabs-marengo/)

- 設計観点: 「bedrock、embedding」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AWS / 生成AI / ga

2026-09-10 [Amazon OpenSearch Serverless is now available on v0 by Vercel](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-opensearch-serverless-available-V0-vercel/)

- 設計観点: 「now available、rag、vector、prompt」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AWS / 生成AI / ga

2026-09-08 [OpenAI GPT-6 Astra is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-astra-on-amazon-bedrock/)

- 設計観点: 「generally available、general availability、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (52) — AZURE / 運用・信頼性 / ga

2026-09-18 [[Launched] Generally Available: Logical replication slot sync status metric for Azure PostgreSQL Flexible Server](https://azure.microsoft.com/updates?id=568414)

- 設計観点: 「generally available、monitor、metric」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (52) — AZURE / 運用・信頼性 / ga

2026-08-13 [[Launched] Generally Available: Control plane metrics collection for AKS with Managed Prometheus](https://azure.microsoft.com/updates?id=568830)

- 設計観点: 「generally available、monitor、metric、observability」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

## 判定方式

小型Naive Bayes分類器と期限・GA・セキュリティ等の明示ルールを併用し、設計・運用・cross-cloudの観点を付与する。最終判断はリンク先の公式情報で確認する。
