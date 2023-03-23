# @Time: 2023/3/22 20:23
# @Author: gxh
from time import sleep

from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage
from page.account_page import AccountPage
from config.driver_config import DriverConfig


class TestAccount:

    def test_account(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, '账户设置')
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver, '个人资料')
        sleep(2)
        AccountPage().update_account_info(driver, "search.png", "14527859984", "女", "14454125441@qq.com",
                                          "中国农业大学")
        sleep(3)
        driver.quit()
