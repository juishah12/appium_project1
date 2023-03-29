import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that
import pytest


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {

            "app": "bs://ece177ba09585bc8d4023e306cbdd4ab42604a6b",
            "platformVersion": "13",
            "deviceName": "iphone 11",
            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": "juishah_JyHv4Q",
                "accessKey": "HkbsaxAwGzRWptpkw56D"
            }
}
        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestSampleApp(AppiumIosConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.NAME,"test-Username").send_keys("admin")
        self.driver.find_element(AppiumBy.XPATH,"//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys("admin123")
        self.driver.find_element(AppiumBy.IOS_PREDICATE,"name=='test-LOGIN'").click()
        actual_error=self.driver.find_element(AppiumBy.XPATH,"//XCUIElementTypeStaticText[contains(@name,'not match')]").text
        assert_that(actual_error).contains("Username and password do not match")

    def test_add_to_cart(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()
        #add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH,"//XCUIElementTypeOther[@name='test-Cart']").click()
        #swipe and click on checkout