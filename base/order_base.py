# @Time: 2023/3/22 9:51
# @Author: gxh


class OrderBase:

    def order_tab(self, tab_name):
        return "//div[@role='tablist']//div[text()='" + tab_name + "']"

    def order_select_page(self):
        return "//input[@placeholder='请选择']/parent::div"

    def order_select_num_page(self, num):
        return "//span[text()='" + num + "']/parent::li"

    def order_click_page(self):
        return "//button[@class='btn-next']"

    def order_input_page(self):
        return "//span[@class='el-pagination__jump']//input[@class='el-input__inner']"
