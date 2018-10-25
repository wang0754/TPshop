from base.initDriver import initDriver
from page.page import Page
class TestDemo:
    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_enterhome(self):
        self.page.inithomepage().enter_home()
