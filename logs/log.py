# @Time: 2023/3/23 11:47
# @Author: gxh
import logging
import os.path
import time

from common.utils import get_project_path, sep


def get_log(logger_name):
    # 创建logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    # 设置日志存放日志，日志文件名
    # 获取本地时间
    local_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # 设置日志存放路径
    all_log_path = get_project_path() + sep(["logs", "all_logs"], sep_before=True, sep_after=True)
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)
    # 设置文件名
    all_log_name = all_log_path + local_time + ".log"
    # 创建handler，写入所有日志
    file_handler = logging.FileHandler(all_log_name,encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    # 文件输出格式
    all_log_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s -%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    # 定义好的输出形式添加到handler
    file_handler.setFormatter(all_log_formatter)
    # 给logger添加handler
    logger.addHandler(file_handler)
    return logger


log = get_log("自动化测试")
