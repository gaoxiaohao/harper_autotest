# @Time: 2023/3/21 0:01
# @Author: gxh

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class DriverConfig:
    @staticmethod
    def driver_config():
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        # 设置窗口大小
        options.add_argument("window-size=1920,1080")
        # 无头模式
        # options.add_argument("--headless")
        # 关闭硬件加速
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sanbox")
        options.add_argument("--disable-dev-shm-usage")
        # 解决selenium无法访问https
        options.add_argument("--ignore-certificate-errors")
        # 忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 无痕模式
        options.add_argument("--incognito")
        # 去除“chrome正在受到自动测试软件的控制”
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 实例化浏览器驱动
        driver = webdriver.Chrome(ChromeDriverManager(url="https://registry.npmmirror.com/-/binary/chromedriver",
                                                      latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                                                      cache_valid_range=365).install(),
                                  options=options)
        # 隐形等待时间
        driver.implicitly_wait(3)
        # 删除所有cookies
        driver.delete_all_cookies()
        return driver


if __name__ == '__main__':
    DriverConfig().driver_config()
