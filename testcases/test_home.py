# @Time: 2023/3/21 15:42
# @Author: gxh
from time import sleep

from config.driver_config import DriverConfig
from page.home_page import HomePage
from page.login_page import LoginPage


class TestHome:

    def test_get_money(self):
        driver = DriverConfig().driver_config()
        driver.get("http://www.tcpjwtester.top/")
        sleep(1)
        LoginPage().login_input_value(driver, "用户名", "周杰伦")
        sleep(1)
        LoginPage().login_input_value(driver, "密码", "123456")
        sleep(1)
        LoginPage().login_click(driver, "登录")
        sleep(2)
        HomePage().tr_td(driver)
        print(HomePage().tr_td(driver))
        sleep(2)
        driver.quit()
