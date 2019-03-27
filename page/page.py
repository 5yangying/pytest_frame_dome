# from page.page_search import SearchPageAction


# 统一page入口
class Page(object):
    def __init__(self, driver):
        self.driver = driver

    # @property
    # def initSearchPage(self):
    #     return SearchPageAction(self.driver)
