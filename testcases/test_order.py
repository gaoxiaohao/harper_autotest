# @Time: 2023/3/22 10:27
# @Author: gxh
from time import sleep

import pytest

from config.driver_config import DriverConfig
from page.order_page import OrderPage
from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
page_list = ["10条/页", "20条/页", "30条/页", "50条/页"]


class TestOrder:
    @pytest.mark.parametrize()
    def test_order(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(1)
        OrderPage().order_list(driver, ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"],
                               ["10条/页", "20条/页", "30条/页", "50条/页"], 2)
        sleep(1)
        driver.quit()
