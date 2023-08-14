import time

import allure
from allure_commons.types import AttachmentType

from Pageobject.Loginpage import OrangeHrm_Login
from utilities.ReadConfig import Readconfig
from utilities.logger import LogGenerator


class Test_Login:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()


    log = LogGenerator.loggen()


    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("page title test case")
    @allure.issue("ABC123")
    @allure.story("This is story#1")
    def test_page_title_001(self,setup):
        self.log.info("Testcase test_page_title_001 is started ")
        self.log.info("Opening Browser")
        self.driver = setup
        self.log.info("page title is" + self.driver.title)
        self.lp = OrangeHrm_Login(self.driver)
        self.lp.LOGIN_URL()
        time.sleep(3)
        if self.driver.title == "OrangeHRM":
            self.log.info("opening browser")
            time.sleep(3)
            allure.attach(self.driver.get_screenshot_as_png(),name="test_page_title_001_pass",attachment_type = AttachmentType.PNG )
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_page_title_001_pass.PNG")
            self.log.info("Taking screenshot")
            # self.driver.close()
            self.log.info("Testcase test_page_title_001 is passed")
            assert True
        else:
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_page_title_001_fail.PNG")
            self.log.info("Taking screenshot")
            # self.driver.close()
            self.log.info("Testcase test_page_title_001 is failed")
            assert False




    def test_login_002(self,setup):
        self.log.info("Testcase test_page_title_001 is started ")
        self.log.info("Opening Browser")
        self.driver = setup
        self.lp = OrangeHrm_Login(self.driver)
        self.log.info("Opening Browser")
        self.lp.LOGIN_URL()
        self.log.info("Enter username")
        self.lp.enter_Username(self.Username)
        self.log.info("Enter password"+self.Username)
        self.lp.enter_Password(self.Password)
        self.log.info("Click on login button" + self.Password)
        self.lp.click_login_button()
        if self.lp.Login_status()== True:
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_login_002_pass.PNG")
            self.log.info("Click on menu button")
            self.lp.click_menu_button()
            self.log.info("Click on logoutbutton button")
            self.lp.click_logout()
            # self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_login_002_fail.PNG")
            # self.driver.close()
            self.log.info("Testcase test_page_title_001 is failed")
            assert False
        self.log.info("Testcase test_login_002_ is completed\n")

