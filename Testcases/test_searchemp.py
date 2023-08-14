import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pageobject.Add_EmpPage import Add_Emp
from Pageobject.Loginpage import OrangeHrm_Login
from Pageobject.Search_Emp import Search_Emp
from utilities.ReadConfig import Readconfig
from utilities.logger import LogGenerator


class Test_EMP_SEARCH:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()

    log = LogGenerator.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("page title test case")
    @allure.issue("ABC123")
    @allure.story("This is story#1")



    @pytest.mark.skip
    def test_search_emp_004(self,setup):
        self.log.info("Testcase test_add_emp_001 is started ")
        self.log.info("Opening Browser")
        self.driver = setup
        self.log.info("page title is" + self.driver.title)
        self.lp = OrangeHrm_Login(self.driver)
        self.lp.LOGIN_URL()
        self.log.info("Enter username")
        self.lp.enter_Username(self.Username)
        self.log.info("Enter password" + self.Username)
        self.lp.enter_Password(self.Password)
        self.log.info("Click on login button" + self.Password)
        self.lp.click_login_button()
        self.ad = Add_Emp(self.driver)
        self.ad.click_pim_button()
        self.log.info("Clicking on pim button")
        self.SC = Search_Emp(self.driver)
        self.SC.Enter_id_number("0273")
        self.log.info("Enter search no")
        self.SC.click_search_button()
        if self.SC.search_result()==True:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_add_emp_003_pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_add_emp_003_pass.PNG")
            self.log.info("Taking screenshot")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_add_emp_003_fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_add_emp_003_fail.PNG")
            self.log.info("Taking screenshot og fail")
            assert False
        self.log.info("Testcase test_addEmp_003_fail is completed\n")


