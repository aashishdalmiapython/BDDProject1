from selenium.webdriver import Chrome

def before_all(context):
    context.driver = Chrome(executable_path="C:\\Driver\\chromedriver.exe")
    context.driver.maximize_window()

def after_all(context):
    context.driver.close()
