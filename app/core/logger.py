"""
项目日志工具类
基于loguru实现，支持.env配置控制台/文件双输出
"""
import sys
from pathlib import Path
import os
from dotenv import load_dotenv
from loguru import logger

# 加载环境变量
load_dotenv()

# ===================== 配置读取（带默认值） =====================
LOG_CONSOLE_ENABLE = os.getenv("LOG_CONSOLE_ENABLE", "true").lower() == "true"
LOG_CONSOLE_LEVEL = os.getenv("LOG_CONSOLE_LEVEL", "INFO").upper()
LOG_FILE_ENABLE = os.getenv("LOG_FILE_ENABLE", "true").lower() == "true"
LOG_FILE_LEVEL = os.getenv("LOG_FILE_LEVEL", "INFO").upper()
LOG_FILE_RETENTION = os.getenv("LOG_FILE_RETENTION", "7 days")

# ===================== 路径配置 =====================
# 获取项目根目录（app/core/logger.py -> 向上3级到项目根）
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE_PATH = LOG_DIR / "app_{time:YYYYMMDD}.log"

# ===================== 日志格式 =====================
# 简洁版格式（推荐）
LOG_FORMAT_SIMPLE = "<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

# 详细版格式（包含函数名）
LOG_FORMAT_DETAIL = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

# 使用详细版格式
LOG_FORMAT = LOG_FORMAT_DETAIL


def setup_logger():
    """
    配置全局日志器
    """
    # 移除默认的handler
    logger.remove()

    # 1. 控制台输出
    if LOG_CONSOLE_ENABLE:
        logger.add(
            sys.stdout,
            format=LOG_FORMAT,
            level=LOG_CONSOLE_LEVEL,
            colorize=True,
            enqueue=True,  # 异步安全
            backtrace=False,  # 生产环境关闭，减少开销
            diagnose=False,
        )
        print(f"[Logger] 控制台日志已启用，级别: {LOG_CONSOLE_LEVEL}")

    # 2. 文件输出
    if LOG_FILE_ENABLE:
        # 确保日志目录存在
        LOG_DIR.mkdir(parents=True, exist_ok=True)

        logger.add(
            LOG_FILE_PATH,
            format=LOG_FORMAT,
            level=LOG_FILE_LEVEL,
            rotation="00:00",  # 每天午夜轮转
            retention=LOG_FILE_RETENTION,  # 保留天数
            compression="gz",  # 压缩旧日志
            encoding="utf-8",
            enqueue=True,
            backtrace=True,  # 文件日志保留堆栈信息，便于调试
            diagnose=True,
        )
        print(f"[Logger] 文件日志已启用，目录: {LOG_DIR}")

    return logger


# 初始化日志器
try:
    setup_logger()
    logger.info("日志系统初始化成功")
except Exception as e:
    print(f"日志系统初始化失败: {e}")
    # 降级方案：使用最简单的控制台输出
    logger.remove()
    logger.add(sys.stdout, format="{time} | {level} | {message}")
    logger.warning(f"使用降级日志模式: {e}")


# 导出便捷函数
def get_logger():
    """获取配置好的logger实例"""
    return logger


# ===================== 测试代码 =====================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("测试日志模块")
    print("=" * 50)

    logger.debug("这是 DEBUG 级别日志")
    logger.info("这是 INFO 级别日志")
    logger.warning("这是 WARNING 级别日志")
    logger.error("这是 ERROR 级别日志")

    print("\n" + "=" * 50)
    print(f"日志文件目录: {LOG_DIR}")
    print("=" * 50)