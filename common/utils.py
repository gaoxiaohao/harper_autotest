# @Time: 2023/3/21 9:44
# @Author: gxh
import os.path

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 获取项目绝对路径
def get_project_path():
    # 项目名称
    # project_name = "harper_autotest"
    # file_path = os.path.dirname(__file__)
    # return file_path[:file_path.find(project_name) + len(project_name)]
    return BASE_PATH


# 给路径添加分隔符
def sep(path, sep_before=False, sep_after=False):
    all_path = os.sep.join(path)
    if sep_before:
        all_path = os.sep + all_path
    if sep_after:
        all_path = all_path + os.sep
    return all_path


def get_image_path(image_name):
    image_path = get_project_path() + sep(["images", image_name], sep_before=True)
    return image_path


if __name__ == '__main__':
    # print(get_project_path())
    # print(sep(["config", "environment.yml"], sep_before=True))
    print(get_project_path())