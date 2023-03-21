# @Time: 2023/3/21 10:59
# @Author: gxh
class LoginBase:

    def login_input(self, input_placeholder):
        #
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_span):
        return "//span[text()='" + button_span + "']/parent::button"


if __name__ == '__main__':
    print(LoginBase().login_input("用户名"))
    print(LoginBase().login_button("登录"))