# @Time: 2023/3/23 1:00
# @Author: gxh
from time import sleep

import allure


def add_images_report(driver, step_name, need_sleep=True):
    """
    截图并插入报告
    :param driver:
    :param step_name: 步骤名称
    :param need_sleep: 是否需要休眠
    :return:
    """
    if need_sleep:
        sleep(1)
    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)
