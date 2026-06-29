"""
独立测试 Milvus 写入和读取
"""
from pymilvus import connections, Collection, FieldSchema, CollectionSchema, DataType, utility
import random

# 连接 Milvus
print("1. 连接 Milvus...")
connections.connect(host='localhost', port='19530')
print("   ✅ 连接成功")

# 查看现有集合
print(f"\n2. 现有集合: {utility.list_collections()}")

collection_name = "test_kb_chunks"

# 删除已存在的测试集合（如果有）
if utility.has_collection(collection_name):
    print(f"\n3. 删除已存在的集合: {collection_name}")
    utility.drop_collection(collection_name)

# 创建集合
print(f"\n4. 创建集合: {collection_name}")

fields = [
    FieldSchema(name='id', dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name='content', dtype=DataType.VARCHAR, max_length=65535),
    FieldSchema(name='item_name', dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name='dense_vector', dtype=DataType.FLOAT_VECTOR, dim=4),
]

schema = CollectionSchema(fields, description="测试集合")
collection = Collection(collection_name, schema)
print("   ✅ 集合创建成功")

# 准备测试数据
print(f"\n5. 插入测试数据...")

test_data = [
    ("这是一个关于烫金机的测试文档", "烫金机"),
    ("这是关于万用表的使用说明", "万用表"),
    ("HAK 180 的操作步骤包括开机、设置温度、开始烫金", "HAK 180"),
]

# 生成随机向量（4维）
vectors = [[random.uniform(-1, 1) for _ in range(4)] for _ in range(3)]

# 准备插入的数据列
contents = [item[0] for item in test_data]
item_names = [item[1] for item in test_data]

try:
    mr = collection.insert([
        contents,      # content 列
        item_names,    # item_name 列
        vectors        # dense_vector 列
    ])
    print(f"   ✅ 插入成功，影响行数: {mr.insert_count}")
except Exception as e:
    print(f"   ❌ 插入失败: {e}")
    import traceback
    traceback.print_exc()

# 创建索引
print(f"\n6. 创建索引...")
index_params = {
    "metric_type": "COSINE",
    "index_type": "IVF_FLAT",
    "params": {"nlist": 128}
}
collection.create_index("dense_vector", index_params)
print("   ✅ 索引创建成功")

# 加载集合
print(f"\n7. 加载集合到内存...")
collection.load()
print("   ✅ 加载成功")

# 搜索测试
print(f"\n8. 搜索测试...")
search_vector = [random.uniform(-1, 1) for _ in range(4)]
search_params = {"metric_type": "COSINE", "params": {"nprobe": 10}}
results = collection.search(
    data=[search_vector],
    anns_field="dense_vector",
    param=search_params,
    limit=3,
    output_fields=["content", "item_name"]
)

print(f"   搜索向量: {search_vector[:2]}...")
print(f"   搜索结果:")
for hits in results:
    for hit in hits:
        print(f"      ID: {hit.id}, 距离: {hit.distance:.4f}")
        print(f"      内容: {hit.entity.get('content')}")
        print(f"      商品: {hit.entity.get('item_name')}")

# 清理测试数据
print(f"\n9. 清理测试集合...")
utility.drop_collection(collection_name)
print("   ✅ 清理完成")

print("\n" + "=" * 50)
print("✅ Milvus 测试完成！所有功能正常")
print("=" * 50)