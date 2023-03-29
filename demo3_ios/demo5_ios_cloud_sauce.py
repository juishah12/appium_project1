import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


class AppiumIosConfig:
      @pytest.fixture(scope="function", autouse=True)
      def launch_app(self):
         des_cap = {
            "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
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
    def test_text_box(self):
        self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="test-Username"]').send_keys("John")
        self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeSecureTextField[@name="test-Password"]').send_keys(
            "John123")
        self.driver.find_element(AppiumBy.XPATH, '//XCUIElementTypeOther[@name="test-LOGIN"]').click()
        actual_text = self.driver.find_element(AppiumBy.XPATH,
                                               '//XCUIElementTypeStaticText[@name="Username and password do not match any user in this service."]').text
        assert_that('Username and password do not match any user in this service.').is_equal_to(actual_text)

    def test_add_to_cart(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()
        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        # swipe and click on checkout
        print(len(self.driver.find_elements(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']")))
        print(self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed())
        # swipe based on visiblity
        while not self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed():
            self.driver.execute_script("mobile: scroll", {"direction": "down"})
        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()