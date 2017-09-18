from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class expected_url_reached:
    """ An expectation for checking that the driver is at a certain URL.
    This does not necessarily mean that the element is visible.
    locator - expected url
    returns true when the url is reached
    """

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        return driver.current_url == self.locator


class TestEngine:
    """docstring for TestEngine"""

    """
    inicia el motor del browser, navegua a la página, llenas los campos de
    log in, espera a input de CAPTCHA y logeo... culmina cuando se presenta
    la página de inicio de IQCM.
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)

    def start(self):
        self.driver.get("https://srviqap18:12100/#/login")
        self.wait.until(EC.presence_of_element_located((By.ID, "txtUser")))
        self.driver.find_element_by_id(
            "txtUser").find_element_by_class_name(
            "dx-texteditor-input").send_keys("vlara")
        self.driver.find_element_by_id(
            "txtPassword").find_element_by_class_name(
            "dx-texteditor-input").send_keys("123456")
        self.driver.find_element_by_id(
            "txtCaptcha").find_element_by_class_name(
            "dx-texteditor-input").click()
        self.wait.until(expected_url_reached((
            "https://srviqap18:12100/#/repo0021")))


if __name__ == "__main__":
    engine = TestEngine()
    engine.start()
