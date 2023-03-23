# @Time: 2023/3/22 21:05
# @Author: gxh
from selenium.webdriver.common.by import By

from base.iframe_base import IframeBase
from base.object_map import ObjectMap


class IframePage(IframeBase, ObjectMap):

    def get_baidu_map_button(self, driver):
        """
        获取百度地图按钮
        :param driver:
        :return:
        """
        button_xpath = self.search_button()
        return self.get_element(driver, By.XPATH, button_xpath)

    def switch_into_baidu_iframe(self, driver):
        """
        切换到百度地图iframe
        :param driver:
        :return:
        """
        iframe_path = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_path)

    def switch_into_content_out(self, driver):
        return self.switch_from_iframe_to_content(driver)
