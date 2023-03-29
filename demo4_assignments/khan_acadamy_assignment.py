import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Users\148592\OneDrive - Arrow Electronics, Inc\Desktop\python\khan-academy-7-3-2.apk",
            "noReset": True
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(15)
        yield
        self.driver.quit()


class TestAppNotification(AppiumConfig):

    def test_handle_notification(self):
        if self.driver.is_app_installed("org.khanacademy.android"):
            self.driver.remove_app("org.khanacademy.android")

        # install,open app and allow notification
        self.driver.install_app(r"D:\Python_Trainning_Material\khan-academy-7-3-2.apk")
        self.driver.activate_app("org.khanacademy.android")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Allow']").click()

        # if loop for clicking on dismiss.
        if len(self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")')) == 1:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Dismiss")').click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Math"]').click()

        # scroll till class 12 math appear
        self.driver.implicitly_wait(2)

        while len(self.driver.find_elements(AppiumBy.XPATH,
                                            '//android.widget.TextView[@text="Class 12 math (India)"]')) == 0:
            self.driver.swipe(500, 1600, 500, 500, 600)

        self.driver.find_element(AppiumBy.XPATH,
                                 '//android.widget.TextView[@text="Class 12 math (India)"]').click()

        while len(self.driver.find_elements(AppiumBy.XPATH,
                                            '//android.widget.TextView[@text="Take Course Challenge"]')) == 0:
            self.driver.swipe(500, 1600, 500, 500, 600)
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Take Course Challenge"]').click()