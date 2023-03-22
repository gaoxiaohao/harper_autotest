# @Time: 2023/3/21 11:08
# @Author: gxh
from base.login_base import LoginBase
from base.object_map import ObjectMap
from selenium.webdriver.common.by import By

from common.yml_config import YmlConfig


class LoginPage(LoginBase, ObjectMap):

    def login_input_value(self, driver, input_placeholder, input_value):
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def login_click(self, driver, button_span):
        button_xpath = self.login_button(button_span)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        self.element_to_url(driver, "/login")
        username, password = YmlConfig().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.login_click(driver, "登录")
