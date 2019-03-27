from appium import webdriver


# 初始化driver驱动对象
def initDriver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': '127.0.0.1:62025',
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
    }
    # 实例化driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
