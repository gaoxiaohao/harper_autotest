# @Time: 2023/3/21 11:08
# @Author: gxh
from base.login_base import LoginBase


class LoginPage(LoginBase):

    def login_input_value(self, driver, input_placeholder, input_value):
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def login_click(self, driver, button_span):
        button_xpath = self.login_button(button_span)
        return driver.find_element_by_xpath(button_xpath).click()
