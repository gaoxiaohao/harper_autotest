# @Time: 2023/3/21 11:08
# @Author: gxh
from time import sleep

from base.login_base import LoginBase
from base.object_map import ObjectMap
from selenium.webdriver.common.by import By

from common.ocr_identify import OcrIdentify
from common.report_add_images import add_image_path_report
from logs.log import log
from common.yml_config import YmlConfig


class LoginPage(LoginBase, ObjectMap):

    def login_input_value(self, driver, input_placeholder, input_value):
        """
        用户信息输入
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        log.info("输入" + input_placeholder + "为：" + str(input_value))
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def login_click(self, driver, button_span):
        """
        点击登录按钮
        :param driver:
        :param button_span:
        :return:
        """
        log.info("点击登录")
        button_xpath = self.login_button(button_span)
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user, is_identify=False):
        self.element_to_url(driver, "/login")
        # 勾选验证码，识别验证图片，填写文本
        if is_identify:
            log.info("需要验证码")
            self.login_identify(driver)
            code_xpath = self.identify_code_pic()
            code_image_path = self.element_screenshot(driver, By.XPATH, code_xpath)
            add_image_path_report(code_image_path,"图像验证码")
            res = OcrIdentify().identify(code_image_path)
            log.info("验证码是"+str(res))
            self.login_input_value(driver, "请输入验证码", res)
            sleep(2)
        username, password = YmlConfig().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.login_click(driver, "登录")
        self.assert_login_success(driver)

    def assert_login_success(self, driver):
        """
        验证是否登录成功
        :param driver:
        :return:
        """
        success_xpath = self.login_success()
        self.element_appear(driver, By.XPATH, success_xpath)

    def assert_login_logo(self, driver, image_name):
        """
        判断头像
        :param driver:
        :param image_name:
        :return:
        """
        return self.find_image_in_source(driver, image_name)

    def login_identify(self, driver):
        """
        点击开启验证码
        :param driver:
        :return:
        """
        xpath = self.is_identify_code()
        return self.element_click(driver, By.XPATH, xpath)
