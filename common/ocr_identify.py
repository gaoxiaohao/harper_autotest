# @Time: 2023/3/23 17:15
# @Author: gxh

import ddddocr


class OcrIdentify:

    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def identify(self, pic_path):
        with open(pic_path, 'rb') as f:
            image = f.read()
        res = self.ocr.classification(image)
        return res
