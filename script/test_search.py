import pytest
from base import initDriver
from base.analysis import get_data
from page.page import Page

pytestmark = pytest.mark.skip('跳过')


class TestDome(object):

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    # 添加你的测试用例
    @pytest.mark.parametrize('value', get_data('test_search'))
    def test_search(self, value):
        # self.page.initSearchPage.click_search()
        # self.page.initSearchPage.input_value(value[0])
        # self.page.initSearchPage.click_black()
        pass

    def teardown(self):
        self.driver.close_app()
        self.driver.quit()
