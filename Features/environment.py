from selenium.webdriver import Chrome

def before_all(context):
    context.driver = Chrome(executable_path="C:\\Driver\\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    context.driver.get("https://www.thetestingworld.com/testings")

def after_all(context):
    context.driver.close()
