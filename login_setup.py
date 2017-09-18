from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import OrderTests





class TestEngine(object):
    """docstring for TestEngine"""

    def __init__(self, arg):
        super(TestEngine, self).__init__()
        self.arg = arg


driver = webdriver.Chrome()
driver.get("https://srviqap18:12100/#/login")
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.ID, "txtUser")))
user_input = driver.find_element_by_id(
    "txtUser").find_element_by_class_name("dx-texteditor-input")
password_input = driver.find_element_by_id(
    "txtPassword").find_element_by_class_name("dx-texteditor-input")
captcha_input = driver.find_element_by_id(
    "txtCaptcha").find_element_by_class_name("dx-texteditor-input")

user_input.send_keys("vlara")
password_input.send_keys("123456")
captcha_input.click()

wait.until(expected_url_reached(("https://srviqap18:12100/#/repo0021")))

OrderTests.navOrderManager(driver)
OrderTests.makeNewOrder(driver)
