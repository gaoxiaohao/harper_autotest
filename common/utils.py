# @Time: 2023/3/21 9:44
# @Author: gxh
import os.path


# 获取项目绝对路径
def get_project_path():
    # 项目名称
    project_name = "harper_autotest"
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name) + len(project_name)]


# 给路径添加分隔符
def sep(path, sep_before=False, sep_after=False):
    all_path = os.sep.join(path)
    if sep_before:
        all_path = os.sep + all_path
    if sep_after:
        all_path = all_path + os.sep
    return all_path


if __name__ == '__main__':
    # print(get_project_path())
    print(sep(["config", "environment.yml"], sep_before=True))
