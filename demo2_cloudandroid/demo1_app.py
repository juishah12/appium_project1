from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap={
    "app":"bs://2847652278840254af52d4312451c4313d1774ee",
    "platformVersion":"9.0",
    "deviceName":"Google Pixel 3",
    "bstack:options": {
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",
        # Set your access credentials
        "userName": "einfochipsshah_WXQDRT",
        "accessKey": "poHrFr5ruP5gBvD73WyH"
    }
}

driver=webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

print(driver.page_source)

driver.quit()