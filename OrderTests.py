from TestEngine import TestEngine
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class OrderTests:

    def __init__(self):
        self.engine = TestEngine()
        self.engine.start()

    def navOrderManager(self):
        self.engine.driver.get("https://srviqap18:12100/#/installpointcare")
        self.engine.wait.until(
            EC.presence_of_element_located((By.ID, "spanicon")))

    def makeNewOrder(driver):
        driver.find_element_by_id("spanicon").click()
        driver.find_element_by_id("INSbtnAddPoint").click()


if __name__ == "__main__":
    manager = OrderTests()
    manager.navOrderManager()
