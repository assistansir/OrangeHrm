import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrangeHrm_Login:

    Text_Username_XPATH = (By.NAME,"username")
    Text_Password_XPATH = (By.NAME,"password")
    Click_Login_button_XPATH = (By.XPATH,"//button[@type='submit']")
    Click_menu_XPATH = (By.XPATH,"//img[@class='oxd-userdropdown-img']")
    Click_Logout_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)


    def LOGIN_URL(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_Username(self,username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_XPATH))
        self.driver.find_element(*OrangeHrm_Login.Text_Username_XPATH).send_keys(username)

    def enter_Password(self,password):
        self.driver.find_element(*OrangeHrm_Login.Text_Password_XPATH).send_keys(password)

    def click_login_button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Login_button_XPATH))
        self.driver.find_element(*OrangeHrm_Login.Click_Login_button_XPATH).click()


    def click_menu_button(self):
        self.driver.find_element(*OrangeHrm_Login.Click_menu_XPATH).click()


    def click_logout(self):
        self.driver.find_element(*OrangeHrm_Login.Click_Logout_XPATH).click()


    def Login_status(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Click_menu_XPATH))
            self.driver.find_element(*OrangeHrm_Login.Click_menu_XPATH)
            return True
        except:
            return False






