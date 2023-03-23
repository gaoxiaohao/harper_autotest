# @Time: 2023/3/22 23:26
# @Author: gxh

import aircv as ac

from common.utils import *


class FindImage:
    def image_read(self, image_path):
        """
        读取照片
        :param image_path:
        :return:
        """
        return ac.imread(image_path)

    def get_confidence(self, source_path, search_path):
        """
        查找图片
        :param source_path: 原图路径
        :param search_path: 查找图路径
        :return:
        """
        image_src = self.image_read(source_path)
        image_search = self.image_read(search_path)
        result = ac.find_template(image_src, image_search)
        print(result)
        return result["confidence"]


