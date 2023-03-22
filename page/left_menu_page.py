# @Time: 2023/3/21 22:53
# @Author: gxh
from selenium.webdriver.common.by import By

from base.left_menu_base import LeftMenuBase
from base.object_map import ObjectMap


class LeftMenuPage(LeftMenuBase, ObjectMap):

    def click_level_one_menu(self, driver, menu_name):
        """
        点击一级菜单
        :param driver: 浏览器驱动
        :param menu_name: 菜单名称
        :return:
        """
        menu_xpath = self.level_one_menu(menu_name)
        return self.element_click(driver, By.XPATH, menu_xpath)

    def click_level_two_menu(self, driver, menu_name):
        """
        点击二级菜单
        :param driver: 浏览器驱动
        :param menu_name: 菜单名称
        :return:
        """
        menu_xpath = self.level_two_menu(menu_name)
        return self.element_click(driver, By.XPATH, menu_xpath)
