# @Time: 2023/3/21 11:13
# @Author: gxh
from time import sleep

from config.driver_config import DriverConfig
from page.login_page import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig().driver_config()
        driver.get("http://www.tcpjwtester.top/")
        sleep(3)
        LoginPage().login_input_value( driver, "用户名", "周杰伦")
        sleep(3)
        LoginPage().login_input_value(driver, "密码", "123456")
        sleep(3)
        LoginPage().login_click(driver, "登录")
        sleep(2)
        driver.quit()
