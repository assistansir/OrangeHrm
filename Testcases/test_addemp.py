import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Pageobject.Add_EmpPage import Add_Emp
from Pageobject.Loginpage import OrangeHrm_Login
from utilities.ReadConfig import Readconfig
from utilities.logger import LogGenerator


class Test_ADDEMP:
    Username = Readconfig.GetUserName()
    Password = Readconfig.GetPassword()

    log = LogGenerator.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    @allure.title("page title test case")
    @allure.issue("ABC123")
    @allure.story("This is story#1")
    def test_add_emp_003(self, setup):
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
        self.ad.click_add_emp()
        self.log.info("Clicking on Add button")
        self.ad.enter_first_name("karan")
        self.log.info("Enter firstname")
        self.ad.enter_middle_name("arjun")
        self.log.info("Enter middlename")
        self.ad.enter_last_name("rahul")
        self.log.info("Enter lasttname")
        time.sleep(2)
        Id= (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/i[1]")
        path="D:\Screenshot 2023-03-18 233735.png"
        self.driver.find_element(By.XPATH,"//input[@type='file']").send_keys(path)
        print(Id)
        time.sleep(3)
        self.ad.click_save_button()
        self.log.info("Click on savebutton")
        time.sleep(3)
        if self.ad.success_massage() == True:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_add_emp_003_pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_add_emp_003_pass.PNG")
            self.log.info("Taking screenshot")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_add_emp_003_fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\OrangeHrm\\Screenshoot\\test_add_emp_003_fail.PNG")
            self.log.info("Taking screenshot")
            assert False
        self.log.info("Testcase test_add_emp_003_pass is completed\n")
