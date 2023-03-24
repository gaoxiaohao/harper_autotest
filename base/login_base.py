# @Time: 2023/3/21 10:59
# @Author: gxh
class LoginBase:

    def login_input(self, input_placeholder):
        #
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_span):
        return "//span[text()='" + button_span + "']/parent::button"

    def login_success(self):
        return "//p[text()='登录成功']"

    def is_identify_code(self):
        return "//span[text()='是否需要验证码']"

    def login_input_code(self):
        return "//input[@placeholder='请输入验证码']"

    def identify_code_pic(self):
        return "//img[@class='el-image__inner']"
