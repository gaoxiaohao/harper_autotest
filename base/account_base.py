# @Time: 2023/3/22 13:46
# @Author: gxh

class AccountBase:

    def account_image(self):
        return "//input[@type='file']"

    def account_phone(self):
        return "//label[text()='手机号']/following-sibling::div//input[@class='el-input__inner']"

    def account_sex(self, sex):
        return "//input[@value='" + sex + "']/parent::span"

    def account_email(self):
        return "//label[text()='邮箱']/following-sibling::div//input[@class='el-input__inner']"

    def account_university(self):
        return "//label[text()='所属大学']/following-sibling::div//input[@class='el-input__inner']"

    def account_submit_button(self):
        return "//span[text()='保存']/parent::button"
