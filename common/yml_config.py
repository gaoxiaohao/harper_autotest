# @Time: 2023/3/21 9:20
# @Author: gxh
import yaml

from common.utils import get_project_path, sep


class YmlConfig:

    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yml"], sep_before=True), "r",
                  encoding="utf-8") as files:
            self.env = yaml.load(files, Loader=yaml.FullLoader)

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]


if __name__ == '__main__':
    print(YmlConfig().get_username_password("jay"))
