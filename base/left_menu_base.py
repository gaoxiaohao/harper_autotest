# @Time: 2023/3/21 16:13
# @Author: gxh

class LeftMenuBase:

    def level_one_menu(self, menu_name):
        if menu_name == "我的订单" or menu_name == "产品" or menu_name == "账户设置":
            return "//aside//span[text()='" + menu_name + "']/parent::div"
        else:
            return "//aside//span[text()='" + menu_name + "']/parent::li"

    def level_two_menu(self, menu_name):
        return "//aside//span[text()='" + menu_name + "']/parent::li"
