import time

from selenium.webdriver.common.by import By

from base.baseaction import BaseAction

class HomePageAction(BaseAction):
    enter_btn_feature = By.ID,"com.tpshop.mails:id/start_Button"
    home_btn_feature = By.XPATH,("text,首页,1","resource-id,com.tpshop.malls:id/tab_txtv,1")
    def enter_home(self):
        time.sleep(3)
        try:
            self.find_element(self.home_btn_feature)
            print("第二次进入")
        except Exception:
            for i in range(3):
                self.swipe_left()
                time.sleep(1)
            self.click(self.enter_btn_feature)
