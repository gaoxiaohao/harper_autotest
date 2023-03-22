# @Time: 2023/3/21 15:40
# @Author: gxh
from base.home_base import HomeBase


class HomePage(HomeBase):

    def tr_td(self, driver):
        xpath = HomeBase().get_money()
        return driver.find_element_by_xpath(xpath)
