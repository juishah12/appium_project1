import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig():
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        desc_cap = {
            "platformName": "android",
            "deviceName": "onePlus",
            "app": r"C:\Users\148592\OneDrive - Arrow Electronics, Inc\Desktop\python\com.bsl.hyundai_2021-08-09.apk",
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=desc_cap)
        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()


class TestAndroid(AppiumConfig):

    def test_def(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Don’t allow']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SIGN UP!']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Name*']").send_keys("ravi")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email ID*']").send_keys("ravi@123")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Mobile Number*']").send_keys("1108")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Password*']").send_keys("pass")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Confirm Password*']").send_keys(
            "Hello")
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[@resource-id='com.bsl.hyundai:id/checkAcceptTermsCondition']").click()