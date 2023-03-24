# @Time: 2023/3/22 22:33
# @Author: gxh
import pytest
import yaml

from common.report_add_images import add_images_report
from common.utils import get_project_path, sep
from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    global driver
    driver = DriverConfig().driver_config()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)
    if report.when == "call":
        if report.failed:
            # 失败了截图
            add_images_report(driver, "失败截图", False)


def get_data():
    """
    读取yml文件数据
    :return:
    """
    yml_path = get_project_path() + sep(["data", "testcase_data.yml"], sep_before=True)
    with open(yml_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


case_data = get_data()

if __name__ == '__main__':
    print(case_data)
