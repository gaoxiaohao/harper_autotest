# @Time: 2023/3/22 0:39
# @Author: gxh

from time import sleep

from config.driver_config import DriverConfig
from page.login_page import LoginPage
from page.left_menu_page import LeftMenuPage
from page.goods_page import GoodsPage


class TestAddGoods:

    def test_add_goods(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver=driver, menu_name="新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(driver, "谷歌", "google", 2, ["00004-7.png", "00005-998.png"], 400, "下架",
                                  "重置")
        sleep(10)
        driver.quit()
