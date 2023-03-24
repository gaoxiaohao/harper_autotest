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


def add_image_path_report(image_path, step_name):
    """
    将图片插入allure报告
    :param image_path:
    :param step_name:
    :return:
    """
    allure.attach.file(image_path, step_name, allure.attachment_type.PNG)
