import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap={

    "app":"bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
    "platformVersion":"13",
    "deviceName":"iphone 11",
    "bstack:options": {
        "projectName" : "First Python project",
        "buildName" : "browserstack-build-1",
        "sessionName" : "BStack first_test",
        # Set your access credentials
        "userName": "juishah_JyHv4Q",
        "accessKey": "HkbsaxAwGzRWptpkw56D"
    }
}

driver=webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)
print(driver.page_source)
time.sleep(5)
