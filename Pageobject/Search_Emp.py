from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Search_Emp:


    Emp_Id_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]")
    Click_Search_button_XPATH = (By.XPATH,"//button[@type='submit']")
    Search_Result_CSS = (By.CSS_SELECTOR,"div[class='oxd-table-card'] div:nth-child(3) div:nth-child(1)")



    def __init__(self,driver):
        self.driver = driver

    def Enter_id_number(self,number):
        self.driver.find_element(*Search_Emp.Emp_Id_XPATH).send_keys(number)


    def click_search_button(self):
        self.driver.find_element(*Search_Emp.Click_Search_button_XPATH).click()


    def search_result(self):
        try:
            self.driver.find_element(*Search_Emp.Search_Result_CSS)
            return True
        except NoSuchElementException:
            return False
