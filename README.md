# 🏨 掌柜智库 — 企业级 RAG 知识库系统

> 让业务专员用自然语言提问，3 秒内从 30,000+ 份酒店文档中找到精准答案

## 📌 项目背景

会小二业务专员在为客户推荐会议场地时，需快速查阅酒店手册、价目表等非结构化文档（PDF、Word、图片等）。传统方式平均查找耗时 5-10 分钟，严重影响客户体验与成单转化。

## 🎯 项目目标

- 支持多格式文档（PDF、MD、图片）自动解析入库
- 实现秒级智能问答，替代人工翻阅文档
- 覆盖 50,000+ 家合作酒店

## 🧠 核心流程

1. 用户上传 PDF/MD 文档
2. MinerU 解析 → VLM 图片理解 → 文档切分
3. BGE-M3 生成稠密+稀疏向量 → 存入 Milvus
4. 用户提问 → 商品确认 + 问题改写
5. BGE-M3 混合检索 + HyDE + RRF + Rerank
6. LLM 生成答案 → SSE 流式输出

## 🛠️ 技术栈

- **AI 框架**：LangChain + LangGraph
- **向量数据库**：Milvus
- **Embedding**：BGE-M3（稠密+稀疏混合）
- **Rerank**：BGE-Reranker
- **LLM**：Qwen-Flash（通义千问）
- **文档解析**：MinerU + Qwen-VL
- **Web 框架**：FastAPI + SSE
- **部署**：Docker Compose

## 📊 项目成果

| 指标 | 数据 |
|------|------|
| 覆盖酒店 | 50,000+ 家 |
| 处理文档 | 30,000+ 份 |
| 信息查找耗时 | 5-10 分钟 → **< 3 秒** |
| 答案准确率 | > 90% |

## 🚀 快速启动

```bash
# 1. 配置环境变量
cp .env.example .env
# 填写 OPENAI_API_KEY、MINERU_API_TOKEN 等

# 2. 启动 Docker 服务
docker-compose up -d

# 3. 启动导入服务
python app/import_process/api/file_import_service.py

# 4. 启动查询服务
python app/query_process/api/query_service.py
