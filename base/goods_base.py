# @Time: 2023/3/21 23:06
# @Author: gxh

class GoodsBase:

    def goods_title(self):
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_details(self):
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_numbers(self, types=True):
        if types:
            return "//form[@class='el-form']//i[@class='el-icon-plus']/parent::span"
        else:
            return "//form[@class='el-form']//input[@placeholder='商品数量']"

    def goods_image(self):
        return "//input[@type='file']"

    def goods_price(self):
        return "//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        return "//input[@placeholder='请选择商品状态']"

    def goods_select_status(self, status):
        return "//span[text()='" + status + "']/parent::li"

    def submit_button(self, span):
        return "//span[text()='" + span + "']/parent::button"
