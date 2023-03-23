# @Time: 2023/3/22 20:55
# @Author: gxh

class IframeBase:

    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"