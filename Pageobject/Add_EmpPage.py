from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Add_Emp:
    Click_Pim_XPATH = (By.XPATH,"//span[normalize-space()='PIM']")
    Click_Add_emp_XPATH_Button = (By.XPATH,"//button[normalize-space()='Add']")
    Text_First_Name_XPATH = (By.XPATH,"//input[@placeholder='First Name']")
    Text_Middle_Name_XPATH = (By.XPATH,"//input[@placeholder='Middle Name']")
    Text_Last_Name_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_Save_Button_XPATH = (By.XPATH,"//button[@type='submit']")
    Upload_img_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]/i[1]")
    AddEmp_Success_Massage = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")





    def __init__(self,driver):
        self.driver = driver


    def click_pim_button(self):
        self.driver.find_element(*Add_Emp.Click_Pim_XPATH).click()


    def click_add_emp(self):
        self.driver.find_element(*Add_Emp.Click_Add_emp_XPATH_Button).click()


    def enter_first_name(self,firstname):
        self.driver.find_element(*Add_Emp.Text_First_Name_XPATH).send_keys(firstname)


    def enter_middle_name(self,middlename):
        self.driver.find_element(*Add_Emp.Text_Middle_Name_XPATH).send_keys(middlename)



    def enter_last_name(self,lastname):
        self.driver.find_element(*Add_Emp.Text_Last_Name_XPATH).send_keys(lastname)


    def upload_image(self,path):
        self.driver.find_element(*Add_Emp.Upload_img_XPATH).send_keys(path)


    def click_save_button(self):
        self.driver.find_element(*Add_Emp.Click_Save_Button_XPATH).click()


    def success_massage(self):
        try:
            self.driver.find_element(*Add_Emp.AddEmp_Success_Massage)
            return True
        except NoSuchElementException:
            return False











