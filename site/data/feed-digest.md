# Cloud Hub release intelligence

生成日時: 2026-11-24T21:21:57.729469Z
取得元: 4/4、分析件数: 48

## 優先項目

### 今週確認 (71) — GCP / セキュリティ / security

2026-11-19 [Dataform — Security: A path traversal vulnerability in workspace directory handling and Git integration was discovered in Dataform, BigQuery Studio, and Colab En](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability、security」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今週確認 (68) — AZURE / 廃止・移行 / retirement

2026-11-23 [Retirement: Azure AI Content Safety selected features will be retired on April 30, 2027](https://azure.microsoft.com/updates?id=577474)

- 設計観点: 「retired、retirement、azure ai」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (66) — AWS / 生成AI / ga

2026-11-23 [AWS WAF announces automated discovery and protection for LLM, MCP, and A2A endpoints using Amazon Bedrock Guardrails](https://aws.amazon.com/about-aws/whats-new/2026/11/waf-ai-endpoint-discovery-protection/)

- 設計観点: 「generally available、guardrails、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (65) — GCP / 生成AI / ga

2026-11-23 [Gemini Enterprise Agent Platform — Feature: Gemini 4 Neon in CodeMender (Preview)](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (65) — AZURE / 廃止・移行 / retirement

2026-11-20 [Retirement: Support for Azure Functions OpenAI Extension ends on April 20, 2027](https://azure.microsoft.com/updates?id=579952)

- 設計観点: 「retirement、azure ai」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (64) — GCP / 廃止・移行 / security

2026-11-19 [Managed Service for Apache Airflow — Security: Managed Airflow service is preparing a fix for the CVE-2026-114938 vulnerability. This fix will be published in an upcoming Managed Airflow ](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (62) — GCP / 生成AI / ga

2026-11-16 [Gemini Enterprise Agent Platform — Feature: Deferred tier for autonomous agent scheduling is generally available](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、general availability、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (61) — AWS / 生成AI / preview

2026-11-21 [Web Search on Amazon Bedrock expands language support and country-aware search](https://aws.amazon.com/about-aws/whats-new/2026/11/web-search-amazon-bedrock/)

- 設計観点: 「agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (61) — GCP / 生成AI / preview

2026-11-19 [Gemini Enterprise Agent Platform — Feature: Gemini 4 Hydrogen in CodeMender (Preview)](https://docs.cloud.google.com/release-notes)

- 設計観点: 「introduces、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (61) — GCP / 廃止・移行 / deprecation

2026-11-18 [Cloud Asset Inventory — Deprecated: Support for the dataplex.googleapis.com/Environment resource type in Cloud Asset Inventory is deprecated because Dataplex Explore is depreca](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (61) — GCP / 生成AI / ga

2026-11-18 [Gemini Enterprise Agent Platform — Feature: Gemini 4 Neon (GA)](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (60) — AWS / 生成AI / update

2026-11-23 [Amazon Connect Customer expands automated performance evaluations to 45 new languages](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-customer-expands-automated-performance-evaluations-new-languages/)

- 設計観点: 「agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (60) — AWS / 生成AI / ga

2026-11-23 [AgentCore runtime instances are now generally available in the AWS GovCloud (US-West) Region](https://aws.amazon.com/about-aws/whats-new/2026/11/agentcore-runtime-instances-govcloud)

- 設計観点: 「generally available、now available、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (59) — AZURE / 生成AI / ga

2026-11-24 [[Launched] Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ](https://azure.microsoft.com/updates?id=581303)

- 設計観点: 「generally available、agent、azure ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (58) — AWS / 生成AI / update

2026-11-23 [Amazon OpenSearch Service now supports OpenSearch version 3.9](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-opensearch-3-9)

- 設計観点: 「agent、rag、vector」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (58) — GCP / 生成AI / ga

2026-11-19 [BigQuery — Feature: You can now enable agent observability with the Data Engineering Agent to monitor the agent's token consumption, request volume, and model l](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、embedding」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — AWS / 運用・信頼性 / update

2026-11-24 [AWS CloudFormation makes resource coverage comprehensive with 206 new types](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-coverage-expansion/)

- 設計観点: 「agent、bedrock、workflow」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (57) — AZURE / 生成AI / ga

2026-11-21 [[Launched] Generally Available: Governance policy guidance in Foundry Canvas and VS Code](https://azure.microsoft.com/updates?id=581463)

- 設計観点: 「generally available、now available、guardrails、agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — AWS / ネットワーク / preview

2026-11-20 [AWS Network Firewall introduces automated Internet firewall in public preview](https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-automated-internet/)

- 設計観点: 「introduces、network、vpc」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (56) — AZURE / 運用・信頼性 / ga

2026-11-17 [[Launched] Generally Available: Geo-redundant backup and restore for Azure HorizonDB](https://azure.microsoft.com/updates?id=574168)

- 設計観点: 「generally available、now available、deployment、backup」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (55) — GCP / 生成AI / ga

2026-11-20 [Gemini Enterprise Agent Platform — Feature: Supervised fine-tuning for Gemini 3.8 Flash is available in General Availability](https://docs.cloud.google.com/release-notes)

- 設計観点: 「general availability、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — AZURE / 運用・信頼性 / preview

2026-11-17 [[In preview] Public Preview: New integration, hybrid deployment, and observability capabilities in Azure Logic Apps](https://azure.microsoft.com/updates?id=580589)

- 設計観点: 「introduces、observability、deployment、workflow」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (55) — GCP / コスト / ga

2026-11-15 [Looker — Announcement: Beginning February 1, 2027, billing will be in effect for usage of Gemini-assisted features that exceeds their instance token allocation. Ge](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、gemini、pricing」が検出されました。継続費用または価格性能比を変える可能性がある更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 料金表、commitment、データ転送、運用工数を確認し、代表ワークロードで総費用差を試算します。

### 今週確認 (54) — AWS / 運用・信頼性 / update

2026-11-21 [Amazon CloudWatch Omni now supports Microsoft Azure platform logs, metrics and traces](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cloudwatch-omni-microsoft-azure)

- 設計観点: 「monitor、metric、reliability」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (54) — AWS / 運用・信頼性 / update

2026-11-20 [Amazon CloudWatch Observability EKS add-on now supports custom OpenTelemetry and Prometheus telemetry](https://aws.amazon.com/about-aws/whats-new/2026/11/cloudwatch-eks-addon-custom-telemetry/)

- 設計観点: 「agent、metric、observability」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (54) — GCP / 生成AI / ga

2026-11-19 [Document AI — Feature: Custom extractor model pretrained-foundation-model-v3.1-lite-2026-10-08 powered by Gemini 3.1 Flash Lite LLM is available in General Availab](https://docs.cloud.google.com/release-notes)

- 設計観点: 「general availability、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — GCP / 生成AI / ga

2026-11-18 [Gemini Enterprise — Feature: Gemini Enterprise: Gemini 4 Neon available in web app, mobile app, Workflow Builder, and AI developer tools](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AZURE / 運用・信頼性 / ga

2026-11-17 [[Launched] Generally Available: Azure Policy support for Azure HorizonDB](https://azure.microsoft.com/updates?id=581180)

- 設計観点: 「generally available、now available、observability、deployment」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (53) — AZURE / 運用・信頼性 / ga

2026-11-24 [[Launched] Generally Available: Azure Site Recovery support for zonal disaster recovery for Ultra disks](https://azure.microsoft.com/updates?id=582171)

- 設計観点: 「generally available、disaster recovery」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (53) — AWS / 生成AI / update

2026-11-23 [Amazon Connect Customer now lets you test AI model version upgrades for automated evaluations](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-customer-test-ai-model-version-upgrades-automated-evaluations)

- 設計観点: 「agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (53) — OCI / 生成AI / ga

2026-10-20 [Use Sandboxes in OCI Generative AI](https://docs.oracle.com/iaas/releasenotes/generative-ai/sandboxes.htm)

- 設計観点: 「now available、agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (52) — AWS / データ / update

2026-11-23 [Amazon Aurora serverless for MySQL now supports up to 384 ACUs](https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-serverless-mysql-supports-384-acu/)

- 設計観点: 「agent、database、sql、aurora」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (52) — AWS / 生成AI / update

2026-11-23 [Amazon Connect Customer AI agents now fill in step-by-step guides](https://aws.amazon.com/about-aws/whats-new/2026/11/connect-ai-agents-fill-guides/)

- 設計観点: 「agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (52) — AZURE / ネットワーク / ga

2026-11-17 [[In preview] Generally Available: Private endpoint support for Azure HorizonDB clusters](https://azure.microsoft.com/updates?id=574153)

- 設計観点: 「generally available、network、dns」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (52) — AZURE / 生成AI / ga

2026-11-17 [[Launched] Generally Available: Azure AI Gateway](https://azure.microsoft.com/updates?id=580080)

- 設計観点: 「generally available、agent、azure ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (52) — AZURE / 運用・信頼性 / ga

2026-11-17 [[Launched] Generally Available: Azure Monitor Health Models](https://azure.microsoft.com/updates?id=580261)

- 設計観点: 「generally available、monitor、metric」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (52) — AZURE / 生成AI / ga

2026-11-17 [[Launched] Generally Available: Microsoft Agent 365 integration with Azure API Management and Azure AI Gateway](https://azure.microsoft.com/updates?id=580055)

- 設計観点: 「generally available、agent、azure ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

## 判定方式

小型Naive Bayes分類器と期限・GA・セキュリティ等の明示ルールを併用し、設計・運用・cross-cloudの観点を付与する。最終判断はリンク先の公式情報で確認する。
