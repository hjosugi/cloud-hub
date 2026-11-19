# Cloud Hub release intelligence

生成日時: 2026-11-19T21:21:23.900696Z
取得元: 4/4、分析件数: 48

## 優先項目

### 今すぐ確認 (74) — GCP / セキュリティ / security

2026-11-19 [Dataform — Security: A path traversal vulnerability in workspace directory handling and Git integration was discovered in Dataform, BigQuery Studio, and Colab En](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability、security」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今すぐ確認 (72) — GCP / 廃止・移行 / retirement

2026-11-12 [Policy Controller — Deprecated: Policy Controller is deprecated as of November 12, 2026, and reaches end of support on December 31, 2027. Starting January 31, 2027, you can](https://docs.cloud.google.com/release-notes)

- 設計観点: 「deprecated、end of support」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (67) — GCP / 廃止・移行 / security

2026-11-19 [Managed Service for Apache Airflow — Security: Managed Airflow service is preparing a fix for the CVE-2026-114938 vulnerability. This fix will be published in an upcoming Managed Airflow ](https://docs.cloud.google.com/release-notes)

- 設計観点: 「vulnerability」が検出されました。互換性喪失や期限付き移行につながるため、通常の新機能より優先度が高い更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 終了日、影響inventory、代替手段、移行検証、rollbackを公式情報で確認し、ownerと期限付きIssueを作成します。

### 今週確認 (65) — AWS / 生成AI / update

2026-11-19 [AWS AppConfig launches support for managing native AI model and AI prompt configuration](https://aws.amazon.com/about-aws/whats-new/2026/11/aws-appconfig-native-ai-model-invocation-prompt-configurations/)

- 設計観点: 「launches、introduces、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (65) — GCP / 生成AI / ga

2026-11-16 [Gemini Enterprise Agent Platform — Feature: Deferred tier for autonomous agent scheduling is generally available](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、general availability、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (64) — GCP / 生成AI / ga

2026-11-18 [Gemini Enterprise Agent Platform — Feature: Gemini 4 Neon (GA)](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (63) — GCP / 生成AI / ga

2026-11-13 [Gemini Enterprise — Feature: Gemini Enterprise: 3-legged OAuth authentication with Agent Identity auth manager for A2A agents](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (61) — AWS / 運用・信頼性 / ga

2026-11-19 [AWS Lambda Durable Execution SDK for Rust is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/11/lambda-durable-execution-sdk-rust/)

- 設計観点: 「generally available、general availability、deployment、workflow」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (61) — GCP / 生成AI / ga

2026-11-19 [BigQuery — Feature: You can now enable agent observability with the Data Engineering Agent to monitor the agent's token consumption, request volume, and model l](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、embedding」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (60) — AZURE / ネットワーク / ga

2026-11-17 [[Launched] Generally Available: Azure Multicloud Interconnect new cloud service provider support](https://azure.microsoft.com/updates?id=579766)

- 設計観点: 「generally available、general availability、now available、interconnect」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (59) — AZURE / 運用・信頼性 / ga

2026-11-17 [[Launched] Generally Available: Geo-redundant backup and restore for Azure HorizonDB](https://azure.microsoft.com/updates?id=574168)

- 設計観点: 「generally available、now available、deployment、backup」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (59) — AWS / セキュリティ / security

2026-11-17 [AWS Security Hub extends unified security management to Google Cloud Platform](https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-gcp/)

- 設計観点: 「vulnerability、security」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今週確認 (58) — AZURE / 運用・信頼性 / preview

2026-11-17 [[In preview] Public Preview: New integration, hybrid deployment, and observability capabilities in Azure Logic Apps](https://azure.microsoft.com/updates?id=580589)

- 設計観点: 「introduces、observability、deployment、workflow」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (58) — GCP / 生成AI / ga

2026-11-12 [Google Kubernetes Engine — Feature: Agent Sandbox on GKE is generally available and runs on any supported GKE version. Agent Sandbox on GKE is optimized for running isolated, s](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、now available、agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — GCP / 生成AI / ga

2026-11-18 [Gemini Enterprise — Feature: Gemini Enterprise: Gemini 4 Neon available in web app, mobile app, Workflow Builder, and AI developer tools](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、gemini」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — AZURE / 運用・信頼性 / ga

2026-11-17 [[Launched] Generally Available: Azure Policy support for Azure HorizonDB](https://azure.microsoft.com/updates?id=581180)

- 設計観点: 「generally available、now available、observability、deployment」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (57) — AWS / 生成AI / update

2026-11-17 [Amazon Bedrock AgentCore now offers free monthly web search queries](https://aws.amazon.com/about-aws/whats-new/2026/11/bedrock-agentcore-free-web-search-queries/)

- 設計観点: 「agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (57) — GCP / データ / ga

2026-11-16 [Config Connector — Announcement: Config Connector version 1.161.0 is now available.](https://docs.cloud.google.com/release-notes)

- 設計観点: 「now available、agent、gemini、analytics」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (56) — AWS / 運用・信頼性 / update

2026-11-19 [Amazon EC2 launches performance status checks and new utilization metrics for EC2 Detailed Monitoring](https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-performance-status-checks/)

- 設計観点: 「launches、monitor、metric」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (56) — AZURE / 運用・信頼性 / ga

2026-11-17 [[Launched] Generally Available: Azure HorizonDB Monitoring via Alerts](https://azure.microsoft.com/updates?id=579933)

- 設計観点: 「generally available、monitor、metric」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (56) — AWS / 生成AI / ga

2026-11-17 [OpenAI GPT-6.2 Astra, and GPT-6.2 Sol are now generally available on Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/11/openai-gpt-6-2-astra-sol-amazon-bedrock/)

- 設計観点: 「generally available、general availability、agent、bedrock」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (56) — GCP / データ / ga

2026-11-12 [BigQuery — Feature: You can track table-level data lineage in Knowledge Catalog for BigQuery pipelines. For more information, see Track data lineage . This feat](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、gemini、generative ai、bigquery」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (55) — AWS / 運用・信頼性 / ga

2026-11-19 [Amazon Connect launches Resolutions, an agentic solution for high-volume operational work](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-connect-resolutions/)

- 設計観点: 「general availability、launches、agent、reliability」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (55) — AWS / 生成AI / ga

2026-11-18 [Amazon OpenSearch Memory is now generally available](https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-memory-generally-available/)

- 設計観点: 「generally available、general availability、agent」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — AZURE / ネットワーク / ga

2026-11-17 [[In preview] Generally Available: Private endpoint support for Azure HorizonDB clusters](https://azure.microsoft.com/updates?id=574153)

- 設計観点: 「generally available、network、dns」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (55) — AZURE / 生成AI / ga

2026-11-17 [[Launched] Generally Available: Azure AI Gateway](https://azure.microsoft.com/updates?id=580080)

- 設計観点: 「generally available、agent、azure ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — AZURE / 運用・信頼性 / ga

2026-11-17 [[Launched] Generally Available: Azure Monitor Health Models](https://azure.microsoft.com/updates?id=580261)

- 設計観点: 「generally available、monitor、metric」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (55) — AZURE / データ / ga

2026-11-17 [[Launched] Generally Available: Database Hub in Microsoft Fabric](https://azure.microsoft.com/updates?id=579216)

- 設計観点: 「generally available、agent、database、sql」が検出されました。保存、処理、検索、移行の選択肢または性能・運用特性に関わる更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: データ領域の比較起点: AWS: S3 / Glue / Redshift / Aurora / AZURE: ADLS / Fabric / Azure SQL / GCP: Cloud Storage / BigQuery / Spanner / OCI: Object Storage / Autonomous Database / MySQL HeatWave。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 対象ワークロード、整合性、上限、互換性、移行と復旧方法を確認し、データ設計の差分をADRへ反映します。

### 今週確認 (55) — AZURE / 生成AI / ga

2026-11-17 [[Launched] Generally Available: Microsoft Agent 365 integration with Azure API Management and Azure AI Gateway](https://azure.microsoft.com/updates?id=580055)

- 設計観点: 「generally available、agent、azure ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (55) — AZURE / セキュリティ / ga

2026-11-17 [[Launched] Generally Available: Symmetric keys on Azure Key Vault Premium](https://azure.microsoft.com/updates?id=579374)

- 設計観点: 「generally available、encryption、key vault」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今週確認 (55) — GCP / コスト / ga

2026-11-15 [Looker — Announcement: Beginning February 1, 2027, billing will be in effect for usage of Gemini-assisted features that exceeds their instance token allocation. Ge](https://docs.cloud.google.com/release-notes)

- 設計観点: 「generally available、agent、gemini、pricing」が検出されました。継続費用または価格性能比を変える可能性がある更新です。 GCPでは「project境界、global platform、managed data、SRE原則から設計する」前提で、Organization / Folder / Projectとzonal・regional・global resource scopeのどこが変わるかを確認します。
- 運用観点: Cloud Operations・Audit Logs・quotaとlaunch stage、model/API versionを確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: コスト領域の比較起点: AWS: Cost Explorer / Savings Plans / AZURE: Cost Management / Reservations / GCP: Cloud Billing / CUD / OCI: Cost Analysis / Universal Credits。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 料金表、commitment、データ転送、運用工数を確認し、代表ワークロードで総費用差を試算します。

### 今週確認 (54) — AWS / ネットワーク / update

2026-11-19 [Amazon Route 53 now supports health checks for private endpoints](https://aws.amazon.com/about-aws/whats-new/2026/11/route-53-private-endpoint-health-checks/)

- 設計観点: 「subnet、load balancer、dns」が検出されました。接続経路、到達性、負荷分散、名前解決またはハイブリッド接続に関わる更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: ネットワーク領域の比較起点: AWS: VPC / Transit Gateway / PrivateLink / AZURE: VNet / Virtual WAN / Private Link / GCP: VPC / Network Connectivity Center / Private Service Connect / OCI: VCN / DRG / Private Endpoint。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 通信経路、名前解決、到達性、障害ドメインを図にし、同等機能との差と切戻し方法を更新します。

### 今週確認 (54) — AWS / 生成AI / update

2026-11-19 [Amazon Connect Customer now provides AI chat summaries in the CCP](https://aws.amazon.com/about-aws/whats-new/2026/11/connect-ai-chat-summaries-ccp/)

- 設計観点: 「agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

### 今週確認 (54) — AWS / セキュリティ / update

2026-11-18 [AWS IAM account access manager is now even easier to deploy and use](https://aws.amazon.com/about-aws/whats-new/2026/11/iam-account-access-manager-easier/)

- 設計観点: 「iam、identity、kms」が検出されました。権限境界、データ保護、プライベート接続または監査設計を変える可能性があります。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: セキュリティ領域の比較起点: AWS: Security Hub / GuardDuty / IAM / AZURE: Defender for Cloud / Entra / Policy / GCP: Security Command Center / Cloud IAM / OCI: Cloud Guard / Security Zones / IAM。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 既存構成への適用範囲、既定値、監査証跡を確認し、必要なら統制と例外手順を更新します。

### 今週確認 (54) — AWS / 運用・信頼性 / update

2026-11-18 [Amazon SageMaker HyperPod now supports higher pod density on EKS-orchestrated clusters](https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-hyperpod-higher-pod-density/)

- 設計観点: 「monitor、logging、autoscaling」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AWSでは「service primitivesをaccount/Region境界で組み合わせる」前提で、Account / OU / Region / VPCとservice固有resource policyのどこが変わるかを確認します。
- 運用観点: CloudWatch・CloudTrail・Configとservice quota、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (54) — AZURE / 運用・信頼性 / ga

2026-11-17 [[In preview] Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB](https://azure.microsoft.com/updates?id=574163)

- 設計観点: 「generally available、deployment、backup」が検出されました。可観測性、自動化、デプロイ、復旧またはスケーリングの運用負荷に影響する更新です。 AZUREでは「Entra・ARM・Policyによるenterprise control planeへworkloadを統合する」前提で、Entra tenant / Management Group / Subscription / Resource Groupのどこが変わるかを確認します。
- 運用観点: Azure Monitor・Activity Log・PolicyとSKU/API version、subscription展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 運用・信頼性領域の比較起点: AWS: CloudWatch / CloudTrail / Config / AZURE: Azure Monitor / Activity Log / Policy / GCP: Cloud Operations / Cloud Audit Logs / OCI: Monitoring / Logging / Audit。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: SLI、ログ、失敗時動作、quota、料金を確認し、監視とランブックの変更要否を記録します。

### 今週確認 (53) — OCI / 生成AI / ga

2026-10-20 [Use Sandboxes in OCI Generative AI](https://docs.oracle.com/iaas/releasenotes/generative-ai/sandboxes.htm)

- 設計観点: 「now available、agent、generative ai」が検出されました。生成AIの設計選択肢、モデル連携、RAGまたはエージェント構成に影響する更新です。 OCIでは「compartment governanceとdatabase-centered enterprise workloadを明示的に構成する」前提で、Tenancy / Compartment / Region / Availability Domain / Fault Domainのどこが変わるかを確認します。
- 運用観点: Monitoring・Logging・Audit・Cloud GuardとDB version、shape、Region展開を確認。既存resourceへの適用、既定値、Region、quota、metric、料金、rollbackを確認します。
- Cross-cloud: 生成AI領域の比較起点: AWS: Amazon Bedrock / AgentCore / AZURE: Azure AI Foundry / GCP: Vertex AI / Gemini Enterprise / OCI: OCI Generative AI。同等性を示す一覧ではありません。resource scope、IAM、HA、運用者責任を個別に比較します。
- 次の行動: 成熟度、対応リージョン、データ境界、評価方法、料金を確認し、採用ADRと運用手順への影響を記録します。

## 判定方式

小型Naive Bayes分類器と期限・GA・セキュリティ等の明示ルールを併用し、設計・運用・cross-cloudの観点を付与する。最終判断はリンク先の公式情報で確認する。
