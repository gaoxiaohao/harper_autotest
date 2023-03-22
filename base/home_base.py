# @Time: 2023/3/21 15:31
# @Author: gxh

class HomeBase:

    def get_money(self):
        return "//tbody//tr[2]//td[1]"

    def wallet_switch(self):
        return "//span[contains(@class,'switch')]"

    def logo(self):
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_time(self):
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_logo(self):
        return "//span[starts-with(text(),'欢迎您回来')]/parent::div/preceding-sibling::div"


if __name__ == '__main__':
    print(HomeBase().get_money())
