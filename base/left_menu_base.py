# @Time: 2023/3/21 16:13
# @Author: gxh

class LeftMenuBase:

    def level_one_menu(self, menu_name):
        return "//aside//span[text()='" + menu_name + "']/parent::div"

    def level_two_menu(self, menu_name):
        return "//aside//span[text()='" + menu_name + "']/parent::li"
