# @Time: 2023/3/21 11:13
# @Author: gxh
from time import sleep

from config.driver_config import DriverConfig
from page.login_page import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(2)
        driver.quit()
