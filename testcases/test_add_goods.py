# @Time: 2023/3/22 0:39
# @Author: gxh

from time import sleep

import pytest

from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage
from page.goods_page import GoodsPage

goods_info_list = [{
    "goods_title": "谷歌",
    "goods_details": "google",
    "goods_num": 2,
    "goods_images": ["search.png", "00005-998.png"],
    "goods_price": 400,
    "goods_status": "下架",
    "goods_submit": "重置"

}]


class TestAddGoods:
    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_goods(self, driver, goods_info):
        LoginPage().login(driver, 'jay')
        sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver=driver, menu_name="新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(driver, goods_info["goods_title"], goods_info["goods_details"],
                                  goods_info["goods_num"], goods_info["goods_images"], goods_info["goods_price"],
                                  goods_info["goods_status"],
                                  goods_info["goods_submit"])
        sleep(2)
