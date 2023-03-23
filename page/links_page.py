# @Time: 2023/3/22 9:35
# @Author: gxh
from base.object_map import ObjectMap


class LinkPage(ObjectMap):

    def goto_link(self, driver):
        self.switch_window_latest_handle(driver)
        return driver.title
