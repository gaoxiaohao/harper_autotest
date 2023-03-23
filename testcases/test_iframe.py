# @Time: 2023/3/22 21:12
# @Author: gxh
from time import sleep

from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage
from page.iframe_page import IframePage
from config.driver_config import DriverConfig


class TestIframe:

    def test_iframe_baidu_map(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, 'iframe测试')
        sleep(2)
        IframePage().switch_into_baidu_iframe(driver)
        sleep(2)
        IframePage().get_baidu_map_button(driver)
        sleep(2)
        IframePage().switch_into_content_out(driver)
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, '首页')
        sleep(2)
        driver.quit()
