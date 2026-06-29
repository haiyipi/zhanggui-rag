# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# 项目配置和环境验证脚本
# 运行方式: python test_setup.py
# """
#
# import sys
# import os
#
# # 添加项目根目录到路径
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
#
# print("=" * 60)
# print("🔧 掌柜智库 RAG 项目 - 环境配置验证")
# print("=" * 60)
#
# # ==================== 1. 测试路径工具 ====================
# print("\n📁 1. 测试路径工具...")
# try:
#     from app.utils.path_util import PROJECT_ROOT, get_project_root
#
#     print(f"   ✅ 项目根目录: {PROJECT_ROOT}")
#     print(f"   ✅ 路径工具导入成功")
# except Exception as e:
#     print(f"   ❌ 路径工具导入失败: {e}")
#
# # ==================== 2. 测试日志模块 ====================
# print("\n📝 2. 测试日志模块...")
# try:
#     from app.core.logger import logger
#
#     logger.info("日志模块测试消息")
#     print(f"   ✅ 日志模块正常工作")
#     print(f"   📂 日志目录: {PROJECT_ROOT}/logs")
# except Exception as e:
#     print(f"   ❌ 日志模块失败: {e}")
#
# # ==================== 3. 测试配置加载 ====================
# print("\n⚙️  3. 测试配置加载...")
#
# # 3.1 大模型配置
# try:
#     from app.conf.lm_config import lm_config
#
#     print(f"   ✅ 大模型配置:")
#     print(f"      - 模型: {lm_config.llm_model}")
#     print(f"      - Base URL: {lm_config.base_url}")
#     print(f"      - API Key: {'已配置' if lm_config.api_key else '未配置'}⚠️")
# except Exception as e:
#     print(f"   ❌ 大模型配置失败: {e}")
#
# # 3.2 Milvus配置
# try:
#     from app.conf.milvus_config import milvus_config
#
#     print(f"   ✅ Milvus配置:")
#     print(f"      - URL: {milvus_config.milvus_url}")
#     print(f"      - Chunks集合: {milvus_config.chunks_collection}")
#     print(f"      - ItemNames集合: {milvus_config.item_name_collection}")
# except Exception as e:
#     print(f"   ❌ Milvus配置失败: {e}")
#
# # 3.3 MongoDB配置
# try:
#     from app.conf.mongo_config import mongo_config
#
#     print(f"   ✅ MongoDB配置:")
#     print(f"      - URL: {mongo_config.mongo_url}")
#     print(f"      - DB Name: {mongo_config.db_name}")
# except Exception as e:
#     print(f"   ❌ MongoDB配置失败: {e}")
#
# # 3.4 MinIO配置
# try:
#     from app.conf.minio_config import minio_config
#
#     print(f"   ✅ MinIO配置:")
#     print(f"      - Endpoint: {minio_config.endpoint}")
#     print(f"      - Bucket: {minio_config.bucket_name}")
#     print(f"      - Secure: {minio_config.minio_secure}")
# except Exception as e:
#     print(f"   ❌ MinIO配置失败: {e}")
#
# # 3.5 Embedding配置
# try:
#     from app.conf.embedding_config import embedding_config
#
#     print(f"   ✅ Embedding配置:")
#     print(f"      - 模型路径: {embedding_config.bge_m3_path}")
#     print(f"      - 设备: {embedding_config.bge_device}")
#     print(f"      - FP16: {embedding_config.bge_fp16}")
# except Exception as e:
#     print(f"   ❌ Embedding配置失败: {e}")
#
# # 3.6 Reranker配置
# try:
#     from app.conf.reranker_config import reranker_config
#
#     print(f"   ✅ Reranker配置:")
#     print(f"      - 模型路径: {reranker_config.bge_reranker_large}")
#     print(f"      - 设备: {reranker_config.bge_reranker_device}")
# except Exception as e:
#     print(f"   ❌ Reranker配置失败: {e}")
#
# # 3.7 MCP配置
# try:
#     from app.conf.bailian_mcp_config import mcp_config
#
#     print(f"   ✅ MCP配置:")
#     print(f"      - URL: {mcp_config.mcp_base_url}")
# except Exception as e:
#     print(f"   ❌ MCP配置失败: {e}")
#
# # ==================== 4. 测试客户端连接 ====================
# print("\n🔌 4. 测试外部服务连接...")
#
# # 4.1 测试Milvus连接
# try:
#     from app.clients.milvus_utils import get_milvus_client
#
#     client = get_milvus_client()
#     if client:
#         print(f"   ✅ Milvus连接成功")
#         # 尝试列出集合
#         try:
#             collections = client.list_collections()
#             print(f"      - 已有集合: {collections}")
#         except:
#             pass
#     else:
#         print(f"   ❌ Milvus连接失败")
# except Exception as e:
#     print(f"   ❌ Milvus连接异常: {e}")
#
# # 4.2 测试MongoDB连接
# try:
#     from pymongo import MongoClient
#     from app.conf.mongo_config import mongo_config
#
#     mongo_client = MongoClient(mongo_config.mongo_url)
#     mongo_client.admin.command('ping')
#     print(f"   ✅ MongoDB连接成功")
#     mongo_client.close()
# except Exception as e:
#     print(f"   ❌ MongoDB连接失败: {e}")
#
# # 4.3 测试MinIO连接
# try:
#     from app.clients.minio_utils import get_minio_client
#
#     minio_client = get_minio_client()
#     if minio_client:
#         # 尝试列出桶
#         buckets = minio_client.list_buckets()
#         print(f"   ✅ MinIO连接成功")
#         print(f"      - 桶列表: {[b.name for b in buckets]}")
#     else:
#         print(f"   ❌ MinIO连接失败")
# except Exception as e:
#     print(f"   ❌ MinIO连接异常: {e}")
#
# # ==================== 5. 测试大模型客户端 ====================
# print("\n🤖 5. 测试大模型客户端...")
# try:
#     from app.lm.lm_utils import get_llm_client
#
#     llm = get_llm_client()
#     print(f"   ✅ 大模型客户端创建成功")
#     print(f"      - 模型: {llm.model_name}")
# except Exception as e:
#     print(f"   ❌ 大模型客户端失败: {e}")
#
# # ==================== 6. 测试向量化工具 ====================
# print("\n🔢 6. 测试向量化工具...")
# try:
#     from app.lm.embedding_utils import get_bge_m3_ef, generate_embeddings
#
#     model = get_bge_m3_ef()
#     if model:
#         print(f"   ✅ BGE-M3模型加载成功")
#         # 测试简单向量化
#         try:
#             result = generate_embeddings(["测试文本"])
#             if result and "dense" in result:
#                 print(f"      - 向量化测试成功 (维度: {len(result['dense'][0])})")
#         except Exception as e:
#             print(f"      - 向量化测试失败: {e}")
#     else:
#         print(f"   ❌ BGE-M3模型加载失败")
# except Exception as e:
#     print(f"   ❌ 向量化工具失败: {e}")
#
# # ==================== 7. 测试重排序工具 ====================
# print("\n📊 7. 测试重排序工具...")
# try:
#     from app.lm.reranker_utils import get_reranker_model
#
#     reranker = get_reranker_model()
#     if reranker:
#         print(f"   ✅ Reranker模型加载成功")
#     else:
#         print(f"   ❌ Reranker模型加载失败")
# except Exception as e:
#     print(f"   ❌ 重排序工具失败: {e}")
#
# # ==================== 8. 测试提示词加载 ====================
# print("\n📄 8. 测试提示词加载...")
# try:
#     from app.core.load_prompt import load_prompt, list_prompts
#
#     prompts = list_prompts()
#     if prompts:
#         print(f"   ✅ 找到 {len(prompts)} 个提示词文件:")
#         for p in prompts:
#             print(f"      - {p}.prompt")
#     else:
#         print(f"   ⚠️  未找到提示词文件 (需要创建 prompts/ 目录)")
# except Exception as e:
#     print(f"   ❌ 提示词加载失败: {e}")
#
# # ==================== 9. 测试工具函数 ====================
# print("\n🛠️  9. 测试工具函数...")
# try:
#     from app.utils.escape_milvus_string_utils import escape_milvus_string
#
#     test_str = 'test"string'
#     escaped = escape_milvus_string(test_str)
#     print(f"   ✅ 字符串转义工具正常")
#
#     from app.utils.normalize_sparse_vector import normalize_sparse_vector
#
#     print(f"   ✅ 稀疏向量归一化工具正常")
#
#     from app.utils.rate_limit_utils import apply_api_rate_limit
#     from collections import deque
#
#     print(f"   ✅ 速率限制工具正常")
# except Exception as e:
#     print(f"   ❌ 工具函数测试失败: {e}")
#
# # ==================== 10. 测试SSE工具 ====================
# print("\n📡 10. 测试SSE工具...")
# try:
#     from app.utils.sse_utils import create_sse_queue, push_to_session, SSEEvent
#
#     test_queue = create_sse_queue("test_session")
#     push_to_session("test_session", SSEEvent.READY, {})
#     print(f"   ✅ SSE工具正常")
# except Exception as e:
#     print(f"   ❌ SSE工具失败: {e}")
#
# # ==================== 11. 测试任务工具 ====================
# print("\n📋 11. 测试任务工具...")
# try:
#     from app.utils.task_utils import add_running_task, add_done_task, get_task_status
#
#     add_running_task("test_task", "test_node")
#     add_done_task("test_task", "test_node")
#     status = get_task_status("test_task")
#     print(f"   ✅ 任务工具正常")
# except Exception as e:
#     print(f"   ❌ 任务工具失败: {e}")
#
# # ==================== 总结 ====================
# print("\n" + "=" * 60)
# print("📊 验证总结")
# print("=" * 60)
#
# # 检查关键配置
# issues = []
#
# if not lm_config.api_key:
#     issues.append("⚠️  大模型API Key未配置 (OPENAI_API_KEY)")
#
# if not os.path.exists(embedding_config.bge_m3_path):
#     issues.append(f"⚠️  BGE-M3模型路径不存在: {embedding_config.bge_m3_path}")
#
# if not os.path.exists(reranker_config.bge_reranker_large):
#     issues.append(f"⚠️  Reranker模型路径不存在: {reranker_config.bge_reranker_large}")
#
# if issues:
#     print("\n❗ 发现以下问题:")
#     for issue in issues:
#         print(f"   {issue}")
# else:
#     print("\n✅ 所有配置验证通过！")
#
# print("\n💡 下一步建议:")
# print("   1. 运行 python app/core/logger.py 测试日志")
# print("   2. 运行 python app/lm/lm_utils.py 测试大模型")
# print("   3. 运行 python app/lm/embedding_utils.py 测试向量化")
# print("   4. 开始实现导入流程节点")
#
# print("\n" + "=" * 60)
# test_llm.py
# test_torch.py
import torch

print(f"PyTorch 版本: {torch.__version__}")
print(f"CUDA 可用: {torch.cuda.is_available()}")

# 测试基本运算
x = torch.tensor([1, 2, 3])
print(f"测试张量: {x}")
print("✅ PyTorch 工作正常")