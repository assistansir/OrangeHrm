import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("headlessmode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()


# use parameter when you have small data set
@pytest.fixture(params=[
    ("Credencetest@test.com", "Credence@123"),
    ("Credencetest@test.com1", "Credence@123"),
    ("Credencetest@test.com", "Credence@1231"),
    ("Credencetest@test.com1", "Credence@1231")
])
def getDataforLogin(request):
    return request.param

