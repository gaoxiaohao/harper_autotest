# @Time: 2023/3/22 10:18
# @Author: gxh
from time import sleep

from selenium.webdriver.common.by import By

from base.order_base import OrderBase
from base.object_map import ObjectMap


class OrderPage(OrderBase, ObjectMap):

    def click_order_tab(self, driver, tab):
        tab_order_xpath = OrderBase().order_tab(tab)
        return self.element_click(driver, By.XPATH, tab_order_xpath)

    def select_order_page(self, driver, num):
        select_page = OrderBase().order_select_page()
        self.element_click(driver, By.XPATH, select_page)
        sleep(2)
        order_xpath = OrderBase().order_select_num_page(num)
        return self.element_click(driver, By.XPATH, order_xpath)

    def click_order_page(self, driver):
        click_order_xpath = OrderBase().order_click_page()
        return self.element_click(driver, By.XPATH, click_order_xpath)

    def input_order_page(self, driver, input_value):
        input_order_xpath = OrderBase().order_input_page()
        return self.element_fill_value(driver, By.XPATH, input_order_xpath, input_value)

    def order_list(self, driver, tab_list, select_list, input_value):
        for selectz in tab_list:
            self.click_order_tab(driver, selectz)
            sleep(2)
        for selectz in select_list:
            self.select_order_page(driver, selectz)
            sleep(2)
        self.click_order_page(driver)
        sleep(2)
        self.input_order_page(driver,input_value)
