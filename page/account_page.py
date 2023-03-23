# @Time: 2023/3/22 14:05
# @Author: gxh
from time import sleep

from selenium.webdriver.common.by import By

from base.account_base import AccountBase
from base.object_map import ObjectMap
from common.utils import get_image_path


class AccountPage(AccountBase, ObjectMap):

    def upload_account_image(self, driver, image_name):
        """
        上传头像
        :param driver:
        :param image_name:
        :return:
        """
        image_path = get_image_path(image_name)
        account_xpath = AccountBase().account_image()
        return ObjectMap().upload(driver, By.XPATH, account_xpath, image_path)

    def input_account_phone(self, driver, input_value):
        """
        修改手机号
        :param driver:
        :param input_value:
        :return:
        """
        account_xpath = AccountBase().account_phone()
        return ObjectMap().element_fill_value(driver, By.XPATH, account_xpath, input_value)

    def input_account_email(self, driver, input_value):
        """
        修改邮箱
        :param driver:
        :param input_value:
        :return:
        """
        account_xpath = AccountBase().account_email()
        return ObjectMap().element_fill_value(driver, By.XPATH, account_xpath, input_value)

    def input_account_university(self, driver, input_value):
        """
        修改大学
        :param driver:
        :param input_value:
        :return:
        """
        account_xpath = AccountBase().account_university()
        return ObjectMap().element_fill_value(driver, By.XPATH, account_xpath, input_value)

    def input_account_sex(self, driver, sex):
        """
        修改性别
        :param sex:
        :param driver:
        :return:
        """
        account_xpath = AccountBase().account_sex(sex)
        return ObjectMap().element_click(driver, By.XPATH, account_xpath)

    def input_account_submit(self, driver):
        """
        提交
        :param driver:
        :return:
        """
        account_xpath = AccountBase().account_submit_button()
        return ObjectMap().element_click(driver, By.XPATH, account_xpath)

    def update_account_info(self, driver, account_image, phone, sex, email, university):
        self.upload_account_image(driver, account_image)
        sleep(2)
        self.input_account_phone(driver, phone)
        sleep(2)
        self.input_account_sex(driver, sex)
        sleep(2)
        self.input_account_email(driver, email)
        sleep(2)
        self.input_account_university(driver, university)
