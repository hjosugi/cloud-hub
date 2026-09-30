# Cloud Hub release intelligence

生成日時: 2026-09-30T21:29:41.059676Z
取得元: 4/4、分析件数: 48

## 優先項目

### 今すぐ確認 (80) — GCP / 廃止・移行 / retirement

2026-09-28 [Cloud Logging — Deprecated: The legacy Logging agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have ceased](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation、end of support、agent」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (80) — GCP / 廃止・移行 / retirement

2026-09-28 [Cloud Monitoring — Deprecated: The legacy Monitoring agent has officially reached its end of support. All standard maintenance and regular bug fixes for the agent have cea](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation、end of support、agent」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (76) — GCP / 廃止・移行 / retirement

2026-09-30 [Backup and DR — Deprecated: Support for backing up and restoring workloads managed via the legacy appliance management console is deprecated.](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation、end of support」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (75) — AZURE / 廃止・移行 / retirement

2026-09-29 [Retirement: Microsoft HPC Pack](https://azure.microsoft.com/updates?id=570046)

- 設計観点: 「retirement、end of support」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (75) — GCP / セキュリティ / security

2026-09-28 [Application Integration — Security: A Confused Deputy vulnerability was discovered in the Email Task component in Application Integration versions prior to June 30, 2026. For m](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability、security」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今すぐ確認 (73) — AZURE / 廃止・移行 / retirement

2026-09-29 [Retirement: Azure IoT Central will be retired on September 20, 2029](https://azure.microsoft.com/updates?id=569914)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (72) — AZURE / 廃止・移行 / retirement

2026-09-24 [Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028](https://azure.microsoft.com/updates?id=557117)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今すぐ確認 (72) — GCP / 廃止・移行 / retirement

2026-09-22 [Compute Engine — Deprecated: As of September 15, 2026, NVIDIA P100 ( nvidia-tesla-p100 and nvidia-tesla-p100-vws ) GPUs have reached end of support (EOS) and are shut do](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、end of support」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (71) — AZURE / 廃止・移行 / retirement

2026-09-16 [Retirement Update: SAP container images removed October 14, 2026](https://azure.microsoft.com/updates?id=571342)

- 設計観点: 「retired、retirement、agent」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (70) — OCI / 廃止・移行 / retirement

2026-09-14 [Cohere Command A Vision and Cohere Embed 4 on-demand models deprecated in Abu Dhabi](https://docs.oracle.com/iaas/releasenotes/generative-ai/cohere-command-a-vision-embed-4-on-demand-deprecated-abudhabi.htm)

- 設計観点: 「deprecated、retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (68) — AZURE / 廃止・移行 / retirement

2026-09-23 [Retirement: Support for PowerShell 7.4 ends on November 10, 2026](https://azure.microsoft.com/updates?id=572770)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (68) — AZURE / 廃止・移行 / retirement

2026-09-23 [Retirement: Support for .NET 8 and .NET 9 ends on November 10, 2026—upgrade your apps to .NET 10](https://azure.microsoft.com/updates?id=572838)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (68) — AZURE / 廃止・移行 / retirement

2026-09-22 [Retirement: Support for Node.js 22 ends on April 30, 2027](https://azure.microsoft.com/updates?id=572771)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (67) — OCI / 廃止・移行 / retirement

2026-09-21 [New Retirement Date for On-Demand Models in Abu Dhabi](https://docs.oracle.com/iaas/releasenotes/generative-ai/new-on-demand-retirement-date-AUH.htm)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (67) — AZURE / 廃止・移行 / retirement

2026-08-14 [Announcing: Azure Databricks Runtime 10.4 LTS will reach end of life on November 1, 2026](https://azure.microsoft.com/updates?id=569353)

- 設計観点: 「end of support、end of life」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (66) — AWS / 生成AI / ga

2026-09-29 [Amazon Bedrock Managed Agents, powered by OpenAI, is now available in preview](https://aws.amazon.com/about-aws/whats-new/2026/09/bedrock-managed-agents-preview/)

- 設計観点: 「now available、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-09-30 [Retirement: NVv3-series Azure Virtual Machines](https://azure.microsoft.com/updates?id=573414)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (65) — GCP / 生成AI / ga

2026-09-30 [Gemini Enterprise Agent Platform — Feature: The App Topology API that provides agent topologies in Gemini Enterprise Agent Platform is now generally available](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、introduces、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (65) — GCP / 廃止・移行 / deprecation

2026-09-28 [Cloud Service Mesh — Deprecated: Cloud Service Mesh support for the in-cluster ISTIOD control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of Sep](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-08-24 [Retirement: Support for Node 22 LTS ends on April 30, 2027](https://azure.microsoft.com/updates?id=567334)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (63) — AZURE / 廃止・移行 / retirement

2026-08-18 [Retirement: Azure VMware Solution License-included service will be retired August 30, 2027](https://azure.microsoft.com/updates?id=569535)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (62) — AZURE / 廃止・移行 / retirement

2026-09-30 [Retirement: NVv4-series Azure Virtual Machines](https://azure.microsoft.com/updates?id=573415)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (62) — AWS / 生成AI / ga

2026-09-28 [Grok 4.7 is now available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-bedrock-grok-4-7/)

- 設計観点: 「now available、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (61) — GCP / ネットワーク / ga

2026-09-29 [Network Connectivity Center — Feature: Network Connectivity Center (NCC) support for Partner Cross-Cloud Interconnect for Amazon Web Services (AWS) is Generally Available .](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、general availability、network、interconnect」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (61) — GCP / 生成AI / ga

2026-09-24 [Gemini Enterprise Agent Platform — Feature: Gemini 3.8 Live](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、introduces、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (58) — AWS / ネットワーク / ga

2026-09-29 [Amazon Route 53 Resolver DNS Firewall support for Palo Alto Networks Advanced DNS Security is now Generally Available (GA)](https://aws.amazon.com/about-aws/whats-new/2026/09/route-53-dns-firewall-panw-dns-security-generally-available)

- 設計観点: 「generally available、network、vpc、dns」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (58) — AWS / セキュリティ / ga

2026-09-24 [AWS Network Security Manager is now generally available in US East (N. Virginia) Region](https://aws.amazon.com/about-aws/whats-new/2026/09/network-security-manager-us-east-va/)

- 設計観点: 「generally available、general availability、security、firewall」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今週確認 (58) — GCP / 生成AI / update

2026-09-21 [Gemini Enterprise — Feature: Gemini Enterprise: Transfer ownership of shared agents](https://docs.cloud.google.com/release-notes)

- 設計観点: 「agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — AWS / 生成AI / update

2026-09-30 [OpenAI GPT-6 Astra now supports UltraFast mode on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-astra-ultrafast-on-amazon-bedrock/)

- 設計観点: 「agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — GCP / ネットワーク / ga

2026-09-30 [Cloud Load Balancing — Feature: A new quota system governing the configuration size of Application Load Balancers is now generally available](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、vpc、load balancer」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (57) — AWS / 生成AI / ga

2026-09-29 [OpenAI GPT-6.1 Sol is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-1-sol-on-amazon-bedrock/)

- 設計観点: 「generally available、general availability、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — GCP / データ / ga

2026-09-28 [BigQuery — Feature: The BigQuery Data Transfer Service MCP server is now Generally Available (GA).](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、lakehouse、bigquery」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (57) — AWS / 運用・信頼性 / ga

2026-09-23 [Amazon CloudWatch Omni: AI-first observability for agents and applications](https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-cloudwatch-omni-ai/)

- 設計観点: 「general availability、agent、observability、reliability」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (57) — AWS / 生成AI / ga

2026-09-22 [OpenAI GPT-6 Sol and GPT-6 Luna are now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-sol-luna-on-amazon-bedrock/)

- 設計観点: 「generally available、general availability、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (56) — OCI / 生成AI / ga

2026-09-25 [Use xAI Grok 4.7 in OCI Generative AI](https://docs.oracle.com/iaas/releasenotes/generative-ai/xai-grok-4-7.htm)

- 設計観点: 「now available、agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — AWS / 生成AI / ga

2026-09-30 [AWS Marketplace launches an AI agent skill for usage-based metering integration](https://aws.amazon.com/about-aws/whats-new/2026/09/marketplace-ai-agent-metering/)

- 設計観点: 「general availability、launches、agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AWS / 生成AI / ga

2026-09-18 [Kimi K3 by Moonshot AI is now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/09/moonshot-ai-kimi-k3-on-amazon-bedrock/)

- 設計観点: 「generally available、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (53) — AWS / 生成AI / ga

2026-09-18 [The new AgentCore Runtime is now available in Amazon Bedrock AgentCore](https://aws.amazon.com/about-aws/whats-new/2026/09/new-agentcore-runtime-generally-available)

- 設計観点: 「now available、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (53) — OCI / 生成AI / ga

2026-09-10 [Use xAI Grok 4.6 in OCI Generative AI](https://docs.oracle.com/iaas/releasenotes/generative-ai/xai-grok-4-6.htm)

- 設計観点: 「now available、agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (52) — AWS / 生成AI / update

2026-09-30 [Amazon S3 Vectors introduces metadata pre-filtering for up to 5x higher recall on filtered search](https://aws.amazon.com/about-aws/whats-new/2026/09/s3-vectors-introduces-metadata-pre-filtering/)

- 設計観点: 「introduces、agent、rag」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

## 判定方式

小型Naive Bayes分類器と期限・GA・セキュリティ等の明示ルールを併用し、設計・運用・cross-cloudの観点を付与する。最終判断はリンク先の公式情報で確認する。
