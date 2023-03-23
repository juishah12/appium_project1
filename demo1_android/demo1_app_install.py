import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\Users\148592\OneDrive - Arrow Electronics, Inc\Desktop\python\khan-academy-7-3-2.apk",
    # "udid":"emulator-5557"
}


def test_invalid_login(self):
    self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
    self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
    self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
    self.driver.find_element(AppiumBy.XPATH,
                             "//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys(
        "dina")
    self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc,'Pass')]").send_keys(
        "dina123")
    # click on sign in
    self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
    # get the text "There was an issue signing in" and print it
    actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
    print(actual_error)
    actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
    print(actual_error)