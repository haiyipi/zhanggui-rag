# 导入核心依赖：数据类、环境变量读取
from dataclasses import dataclass
import os
from dotenv import load_dotenv

# 提前加载.env配置文件
load_dotenv()


# 定义MongoDB配置类
@dataclass
class MongoConfig:
    mongo_url: str      # MongoDB连接地址
    db_name: str        # 数据库名称


# 实例化MongoDB配置对象
mongo_config = MongoConfig(
    mongo_url=os.getenv("MONGO_URL"),
    db_name=os.getenv("MONGO_DB_NAME")
)


# 测试代码
if __name__ == "__main__":
    print(f"MongoDB URL: {mongo_config.mongo_url}")
    print(f"Database Name: {mongo_config.db_name}")