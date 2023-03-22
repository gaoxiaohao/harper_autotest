# @Time: 2023/3/22 0:16
# @Author: gxh
from time import sleep

from selenium.webdriver.common.by import By

from base.goods_base import GoodsBase
from base.object_map import ObjectMap
from common.utils import get_image_path


class GoodsPage(GoodsBase, ObjectMap):

    def input_goods_title(self, driver, input_value):
        """
        输入商品标题
        :param driver:
        :param input_value:
        :return:
        """
        goods_xpath = self.goods_title()
        return self.element_fill_value(driver, By.XPATH, goods_xpath, input_value)

    def input_goods_details(self, driver, input_value):
        """
        输入商品详情
        :param driver:
        :param input_value:
        :return:
        """
        goods_xpath = self.goods_details()
        return self.element_fill_value(driver, By.XPATH, goods_xpath, input_value)

    def click_goods_num(self, driver, nums):
        """
        输入商品数量
        :param driver:
        :param nums:
        :return:
        """
        goods_xpath = self.goods_numbers(True)
        for i in range(nums):
            self.element_click(driver, By.XPATH, goods_xpath)
            sleep(0.5)

    def upload_goods_image(self, driver, image_name):
        """
        文件上传
        :param driver:
        :param image_name:
        :return:
        """
        image_path = get_image_path(image_name)
        upload_xpath = self.goods_image()
        return self.upload(driver, By.XPATH, upload_xpath, image_path)

    def input_goods_price(self, driver, input_value):
        """
        输入商品价格
        :param driver:
        :param input_value:
        :return:
        """
        goods_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, goods_xpath, input_value)

    def select_goods_status(self, driver, select_name):
        """
        选择商品状态
        :param driver:
        :param select_name:
        :return:
        """
        goods_xpath = self.goods_status()
        self.element_click(driver, By.XPATH, goods_xpath)
        sleep(1)
        goods_select_xpath = self.goods_select_status(select_name)
        return self.element_click(driver, By.XPATH, goods_select_xpath)

    def click_bottom_button(self, driver, button_name):
        """
        点击提交按钮
        :param driver:
        :param button_name:
        :return:
        """
        button_xpath = self.submit_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)

    def add_new_goods(self, driver, title, details, numbers, images, price, status, submit):
        self.input_goods_title(driver, title)
        self.input_goods_details(driver, details)
        self.click_goods_num(driver, numbers)
        for image in images:
            self.upload_goods_image(driver, image)
            sleep(3)
        self.input_goods_price(driver, price)
        self.select_goods_status(driver, status)
        self.click_bottom_button(driver, submit)
