from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):
    def __init__(self, driver):
        self.driver = driver

    # 二次封装find_element方法,实际上是按照自定义的特征调用原来find_element方法
    def find_element(self, feature):
        # 添加元素等待
        wait = WebDriverWait(self.driver, 5, 1)
        if feature[0] == By.XPATH:
            return wait.until(lambda x: x.find_element(feature[0], self.mark_xpath(feature[1])))
        else:
            return wait.until(lambda x: x.find_element(feature[0], feature[1]))

    # 二次封装find_elements方法
    def find_elements(self, feature):
        return self.driver.find_elements(feature[0], feature[1])

    # 对外提供，使用自定义的特征就可以查找元素并点击
    def click(self, feature):
        return self.find_element(feature).click()

    # 对外提供
    def send_keys(self, feature, value):
        return self.find_element(feature).send_keys(value)

    def __mark_one_path(self, s):
        rule_list = s.split(',')
        if len(rule_list) == 2:  # 情况一
            res_path = 'contains(@%s,"%s")' % (rule_list[0], rule_list[1])
        elif len(s.split(',')) == 3:  # 情况二
            res_path = '@%s="%s"' % (rule_list[0], rule_list[1])
        else:
            raise Exception
        return res_path

    def mark_xpath(self, rule):
        if rule.startswith('//*['):
            return rule
        start_path = '//*['
        end_path = ']'
        res_path = ''

        if isinstance(rule, str):  # 情况 1 或 2
            res_path = self.__mark_one_path(rule)
            return start_path + res_path + end_path
        else:  # 情况三
            li = []
            for i in rule:
                s = self.__mark_one_path(i)
                li.append(s)
            res_path = start_path + ' and '.join(li) + end_path
        return res_path
