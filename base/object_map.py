# @Time: 2023/3/21 16:38
# @Author: gxh
import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.yml_config import YmlConfig


class ObjectMap:
    # 获取基础地址
    base_url = YmlConfig().get_url()

    def get_element(self, driver, locate_type, locator_expression, timeout=10, must_show=False):
        """
                获取元素
                :param driver: 浏览器驱动
                :param locate_type:  定位方式类型
                :param locator_expression: 定位表达式
                :param timeout: 超时时间
                :param must_show: 元素是否必须可见，True可见
                :return:
                """
        start_time = time.time() * 1000
        end_time = start_time + (timeout * 1000)
        for i in range(int(timeout * 10)):
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                if not must_show:
                    return element
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_time = time.time()
                if now_time >= end_time:
                    break
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式" + locate_type + "定位表达式" + locator_expression)

    def wait_ready_state_complete(self, driver, timeout=30):
        """
        等待页面加载完成
        :param driver: 浏览器驱动
        :param timeout:  超时时间
        :return:
        """
        start_time = time.time() * 1000
        end_time = start_time + (timeout * 1000)
        for i in range(int(timeout * 10)):
            try:
                read_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                return True
            if read_state == 'complete':
                time.sleep(0.1)
                return True
            else:
                now_time = time.time() * 1000
                if now_time >= end_time:
                    break
                time.sleep(0.1)
        raise Exception("打开页面未在%s秒加载完成" % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        :param driver: 浏览器驱动
        :param locate_type:  元素定位方式类型
        :param locator_expression:  元素定位表达式
        :param timeout:  超时时间
        :return:
        """
        if locate_type:
            start_time = time.time() * 1000
            end_time = start_time + (timeout * 1000)
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_time = time.time() * 1000
                        if now_time >= end_time:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式" + locate_type + "")
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待元素出现
        :param driver: 浏览器驱动
        :param locate_type:  定位方式
        :param locator_expression:  定位表达式
        :param timeout:  超时时间
        :return:
        """
        if locate_type:
            start_time = time.time() * 1000
            end_time = start_time + (timeout * 1000)
            for i in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_time = time.time() * 1000
                    if now_time >= end_time:
                        break
                    pass
            raise ElementNotVisibleException("元素没有出现")
        else:
            pass

    def element_to_url(self,
                       driver,
                       url,
                       locate_type_disappear=None,
                       locator_expression_disappear=None,
                       locate_type_appear=None,
                       locator_expression_appear=None):
        """
                跳转地址
                :param driver: 浏览器驱动
                :param url: 跳转地址
                :param locate_type_disappear:  等待页面元素消失的定位方式
                :param locator_expression_disappear: 等待页面元素消失的定位方式
                :param locate_type_appear: 等待页面元素消失的定位表达式
                :param locator_expression_appear: 等待页面元素消失的定位表达式
                :return:
                """
        try:
            driver.get(self.base_url + url)
            # 等待页面元素加载完成
            self.wait_ready_state_complete(driver)
            # 跳转地址后等待元素消失
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
            # 跳转地址后等待元素出现
            self.element_appear(driver, locate_type_appear, locator_expression_appear)
        except Exception as e:
            print("跳转异常，异常原因：%s" % e)
            return False
        return True

    def element_is_display(self, driver,
                           locate_type,
                           locator_expression):
        """
        元素是否显示
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException as e:
            print(e)
            return False

    def element_fill_value(self, driver,
                           locate_type,
                           locator_expression,
                           fill_value, timeout=20):
        """
                元素填值
                :param driver:  浏览器驱动
                :param locate_type:  定位方式
                :param locator_expression:  定位表达式
                :param fill_value:  填入的值
                :param timeout:  超时时间
                :return:
                """
        # 元素先出现
        element = self.element_appear(driver, locate_type, locator_expression, timeout)
        try:
            # 清空原有值
            element.clear()
        # 页面元素没有刷新出来，抛出异常
        except StaleElementReferenceException:
            self.wait_ready_state_complete(driver)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        # 填入的值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
        try:
            # 不是回车结尾，填入值
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_ready_state_complete(driver)
            else:
                #
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_ready_state_complete(driver)
        except StaleElementReferenceException:
            self.wait_ready_state_complete(driver)
            time.sleep(0.1)
            element = self.element_appear(driver, locate_type, locator_expression)
            element.clear()
            # 不是回车结尾，填入值
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_ready_state_complete(driver)
            else:
                #
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_ready_state_complete(driver)
        except Exception:
            raise Exception("元素填值失败")
        return True

    def element_click(self,
                      driver,
                      locate_type,
                      locator_expression,
                      locate_type_disappear=None,
                      locator_expression_disappear=None,
                      locate_type_appear=None,
                      locator_expression_appear=None,
                      timeout=30):
        """
                元素点击
                :param driver: 浏览器驱动
                :param locate_type:  定位方式
                :param locator_expression: 定位表达式
                :param locate_type_disappear: 等待元素消失定位方式
                :param locator_expression_disappear: 等待元素消失定位表达式
                :param locate_type_appear: 等待元素出现定位方式
                :param locator_expression_appear: 等待元素出现定位表达式
                :param timeout: 超时时间
                :return:
                """
        element = self.element_appear(driver, locate_type, locator_expression, timeout)
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_ready_state_complete(driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type, locator_expression, timeout)
            element.click()
        except Exception as e:
            print("页面出现异常，无法点击")
            return False
        # 点击元素后元素出现或者消失
        try:
            self.element_appear(driver, locate_type_appear, locator_expression_appear)
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
        except Exception as e:
            print("等待元素消失或者出现失败", e)
        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        文件上传
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param file_path:
        :return:
        """
        element = self.get_element(driver, locate_type, locator_expression)
        return element.send_keys(file_path)
