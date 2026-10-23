# Cloud Hub release intelligence

生成日時: 2026-10-23T23:52:15.596615Z
取得元: 4/4、分析件数: 48

## 優先項目

### 今週確認 (71) — GCP / 運用・信頼性 / security

2026-10-23 [Cloud Monitoring — Fixed: Ops Agent version 2.73.0 includes patches for a Go vulnerability involving system root certificates, CVE-2026-111943 . For more information,](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability、agent、monitor」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (71) — GCP / セキュリティ / security

2026-10-14 [Application Integration — Security: An Incorrect Authorization vulnerability in the AuthConfig validation and integration execution runtime in Application Integration versions ](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability、security」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今週確認 (69) — AZURE / 廃止・移行 / retirement

2026-10-08 [Retirement: Azure Deployment Environments will be retired on February 22, 2027](https://azure.microsoft.com/updates?id=567934)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (69) — AZURE / 廃止・移行 / retirement

2026-10-06 [Retirement: Azure App Service on Azure Stack Hub](https://azure.microsoft.com/updates?id=568178)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (69) — AZURE / 廃止・移行 / retirement

2026-10-01 [Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029](https://azure.microsoft.com/updates?id=569592)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (69) — AZURE / 廃止・移行 / retirement

2026-09-29 [Retirement: Microsoft HPC Pack](https://azure.microsoft.com/updates?id=570046)

- 設計観点: 「retirement、end of support」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (69) — AZURE / 廃止・移行 / retirement

2026-09-24 [Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028](https://azure.microsoft.com/updates?id=557117)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (68) — AZURE / 廃止・移行 / retirement

2026-09-16 [Retirement Update: SAP container images removed October 14, 2026](https://azure.microsoft.com/updates?id=571342)

- 設計観点: 「retired、retirement、agent」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (67) — AZURE / 廃止・移行 / retirement

2026-10-08 [Retirement: Microsoft Dev Box will be retired on September 18, 2028](https://azure.microsoft.com/updates?id=567933)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (67) — AZURE / 廃止・移行 / retirement

2026-09-29 [Retirement: Azure IoT Central will be retired on September 20, 2029](https://azure.microsoft.com/updates?id=569914)

- 設計観点: 「retired、retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (66) — GCP / 廃止・移行 / deprecation

2026-10-15 [Video Intelligence API — Deprecated: We are deprecating the emotion label response in the API. Going forward, the API will return UNKNOWN for all emotion related labels.](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-10-06 [Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027](https://azure.microsoft.com/updates?id=568585)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-09-23 [Retirement: Support for PowerShell 7.4 ends on November 10, 2026](https://azure.microsoft.com/updates?id=572770)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-09-23 [Retirement: Support for .NET 8 and .NET 9 ends on November 10, 2026—upgrade your apps to .NET 10](https://azure.microsoft.com/updates?id=572838)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-09-22 [Retirement: Support for Node.js 22 ends on April 30, 2027](https://azure.microsoft.com/updates?id=572771)

- 設計観点: 「retirement」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (62) — GCP / 生成AI / update

2026-10-16 [Vertex AI Search — Change: Agent Search: Update to the stable model](https://docs.cloud.google.com/release-notes)

- 設計観点: 「agent、gemini、vertex ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (62) — GCP / 生成AI / ga

2026-10-13 [Gemini Enterprise Agent Platform — Feature: Gemini 4 Argon in CodeMender (Preview)](https://docs.cloud.google.com/release-notes)

- 設計観点: 「general availability、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (61) — AWS / 生成AI / update

2026-10-22 [AgentCore Gateway now supports Bedrock InvokeModel APIs and model fallback](https://aws.amazon.com/about-aws/whats-new/2026/10/agentcore-gateway-invokemodel-fallback/)

- 設計観点: 「agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (61) — AWS / 生成AI / ga

2026-10-15 [Web Search on Amazon Bedrock AgentCore expands to AWS GovCloud and 3 Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-agentcore/)

- 設計観点: 「now available、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (60) — GCP / 生成AI / ga

2026-10-14 [Gemini Enterprise Agent Platform — Feature: Priority PayGo support for Gemini Nano Banana 2.1](https://docs.cloud.google.com/release-notes)

- 設計観点: 「general availability、introduces、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (59) — OCI / 生成AI / ga

2026-10-20 [Use Sandboxes in OCI Generative AI](https://docs.oracle.com/iaas/releasenotes/generative-ai/sandboxes.htm)

- 設計観点: 「now available、agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (58) — AWS / 生成AI / ga

2026-10-19 [Grok 4.7 is now available on Amazon Bedrock in AWS GovCloud (US)](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-bedrock-grok-4-7-govcloud/)

- 設計観点: 「now available、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (58) — AWS / 運用・信頼性 / ga

2026-10-15 [AWS Lambda Durable Execution SDK for Go is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/)

- 設計観点: 「generally available、general availability、deployment、workflow」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (58) — GCP / 廃止・移行 / deprecation

2026-10-15 [Cloud Vision — Deprecated: Face detection model update](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (57) — AWS / 生成AI / ga

2026-10-21 [Beam model by Reflection is now available on Amazon SageMaker JumpStart and AWS Trainium](https://aws.amazon.com/about-aws/whats-new/2026/01/reflection-beam-on-sagemaker-jumpstart-and-aws-trainium/)

- 設計観点: 「now available、agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — AWS / 生成AI / update

2026-10-20 [Amazon Bedrock Advanced Prompt Optimization now supports prompt shortening](https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-prompt-optimization-shortening/)

- 設計観点: 「bedrock、prompt」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (56) — AWS / 生成AI / update

2026-10-20 [Amazon Bedrock Guardrails now supports Standard tier for contextual grounding checks](https://aws.amazon.com/about-aws/whats-new/2026/10/bedrock-guardrails-grounding-standard/)

- 設計観点: 「guardrails、bedrock、guardrail」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (56) — AWS / 運用・信頼性 / ga

2026-10-19 [Amazon CloudWatch Omni is now available in additional AWS Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-cloudwatch-omni-8-regions/)

- 設計観点: 「now available、agent、observability、reliability」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (56) — AWS / 生成AI / ga

2026-10-16 [Nemotron 3.5 Super VL model now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/nvidia-nemotron-3.5-super-vl-on-sagemaker-jumpstart/)

- 設計観点: 「now available、agent、foundation model」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (56) — AWS / 運用・信頼性 / ga

2026-10-15 [Amazon Managed Service for Prometheus Collector now available in Asia Pacific (New Zealand) Region](https://aws.amazon.com/about-aws/whats-new/2026/10/ams-prometheus-collector-apac-nz/)

- 設計観点: 「now available、agent、monitor、metric」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (56) — OCI / 生成AI / ga

2026-10-14 [Priority processing is now available for Grok 4.20 and Grok 4.3](https://docs.oracle.com/iaas/releasenotes/generative-ai/xai-grok-priority-processing.htm)

- 設計観点: 「now available、agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — AWS / コスト / update

2026-10-23 [Amazon EMR on EKS reduces EMR charge by 30 percent](https://aws.amazon.com/about-aws/whats-new/2026/10/emr-eks-reduces-emr-charge-30-percent/)

- 設計観点: 「action required、pricing、price、cost」が検出されました。継続費用または価格性能比を変える可能性がある更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 料金表、commitment、データ転送、運用工数を確認し、代表ワークロードで総費用差を試算します。

### 今週確認 (55) — OCI / 生成AI / update

2026-10-20 [Global Generative AI availability](https://docs.oracle.com/iaas/releasenotes/generative-ai/expanded-on-demand-model-access.htm)

- 設計観点: 「agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — OCI / 生成AI / update

2026-10-20 [GoldenGate adds support for new connection types](https://docs.oracle.com/iaas/releasenotes/goldengate/r12connections.htm)

- 設計観点: 「gemini、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — GCP / データ / ga

2026-10-19 [AlloyDB for PostgreSQL — Feature: Lakehouse federation in AlloyDB is generally available ( GA ). This feature lets you query live data in BigQuery directly from AlloyDB using](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、sql、lakehouse、bigquery」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (54) — GCP / 廃止・移行 / deprecation

2026-10-18 [Google SecOps SOAR — Announcement: Release 6.3.103 is being rolled out to the first phase of regions as listed here .](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、deprecation」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (54) — AWS / 生成AI / ga

2026-10-15 [Muse Spark Open model now available on Amazon SageMaker JumpStart](https://aws.amazon.com/about-aws/whats-new/2026/01/muse-spark-open-on-sagemaker-jumpstart/)

- 設計観点: 「now available、agent、foundation model」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — GCP / 生成AI / ga

2026-10-13 [Gemini Enterprise — Feature: Gemini Enterprise: Gemini 4 Argon available in web app, mobile app, and AI developer tools](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — GCP / データ / ga

2026-10-12 [BigQuery — Feature: Incremental data transfers for the BigQuery Data Transfer Service for PostgreSQL and ServiceNow are now generally available (GA).](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、sql、bigquery」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (53) — GCP / データ / update

2026-10-22 [Data Studio — Feature: You can connect Data Studio to a BigQuery Graph or query a graph by using a custom SQL query in the BigQuery connector, which imports graph ](https://docs.cloud.google.com/release-notes)

- 設計観点: 「sql、bigquery」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (53) — OCI / データ / update

2026-10-20 [SQL Tracing for Application Workloads](https://docs.oracle.com/iaas/releasenotes/autonomous-database-serverless/2026-10-sql-tracing.htm)

- 設計観点: 「database、sql」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (53) — OCI / データ / update

2026-10-20 [Use in-place upgrades to move database systems to newer PostgreSQL major versions](https://docs.oracle.com/iaas/releasenotes/postgresql/inplace-upgrade.htm)

- 設計観点: 「database、sql」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (53) — OCI / 生成AI / update

2026-10-13 [Select AI Support for Gemini Enterprise Agent Platform](https://docs.oracle.com/iaas/releasenotes/autonomous-database-serverless/2026-10-select-ai-gemini.htm)

- 設計観点: 「agent、gemini、embedding」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

## 判定方式

小型Naive Bayes分類器と期限・GA・セキュリティ等の明示ルールを併用し、設計・運用・cross-cloudの観点を付与する。最終判断はリンク先の公式情報で確認する。
