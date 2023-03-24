# @Time: 2023/3/22 0:39
# @Author: gxh
import json
from time import sleep

import pytest
from logs.log import log
from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage
from page.goods_page import GoodsPage
from testcases.conftest import case_data


class TestAddGoods:
    @pytest.mark.parametrize("goods_info_list",
                             case_data["goods_info_list"])
    def test_add_goods(self, driver, goods_info_list):
        LoginPage().login(driver, 'jay')
        sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver=driver, menu_name="新增二手商品")
        sleep(2)
        for goods_info in goods_info_list:
            GoodsPage().add_new_goods(driver, goods_info["goods_title"], goods_info["goods_details"],
                                      goods_info["goods_num"], goods_info["goods_images"], goods_info["goods_price"],
                                      goods_info["goods_status"],
                                      goods_info["goods_submit"])
        sleep(2)
