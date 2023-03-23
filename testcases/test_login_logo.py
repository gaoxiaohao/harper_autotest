# @Time: 2023/3/23 16:20
# @Author: gxh
from time import sleep

from common.report_add_images import add_images_report
from page.login_page import LoginPage


class TestLoginLogo:

    def test_login_logo(self, driver):
        LoginPage().login(driver, 'jay')
        sleep(2)
        assert LoginPage().assert_login_logo(driver, "img_1.png") > 0.9
