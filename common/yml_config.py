# @Time: 2023/3/21 9:20
# @Author: gxh
import yaml

from common.utils import get_project_path, sep


class YmlConfig:

    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yml"], sep_before=True), "r",
                  encoding="utf-8") as files:
            self.env = yaml.load(files, Loader=yaml.FullLoader)
            print(self.env)

    def get_username_password(self):
        return self.env["username"], self.env["password"]


if __name__ == '__main__':
    YmlConfig().get_username_password()
