# @Time: 2023/3/22 9:37
# @Author: gxh
from time import sleep

import allure
import pytest

from config.driver_config import DriverConfig
from page.left_menu_page import LeftMenuPage
from page.links_page import LinkPage
from page.login_page import LoginPage
from common.report_add_images import add_images_report


class TestLink:
    @allure.description("窗口句柄")
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    def test_link(self, driver):
        """
        外链
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(driver, 'gxh')
            sleep(3)
            add_images_report(driver, "登录")
        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver, '外链')
            sleep(1)
            add_images_report(driver, "点击外链")
        with allure.step("断言title"):
            title = LinkPage().goto_link(driver)
            assert title == "慕课网-程序员的梦工厂"
