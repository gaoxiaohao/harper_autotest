# @Time: 2023/3/21 11:13
# @Author: gxh
from time import sleep

import allure
import pytest

from common.report_add_images import add_images_report
from page.login_page import LoginPage


class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login(self, driver):
        """使用错误账号登录"""
        with allure.step("登录"):
            LoginPage().login(driver, "gxh")
            sleep(2)
            add_images_report(driver, "登录")
