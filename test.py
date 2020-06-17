from selenium.webdriver import Chrome
from behave import *
import time

driver = Chrome(executable_path="C:\\Driver\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.thetestingworld.com/testings")
driver.find_element_by_xpath("//input[@id='tab2']/following-sibling::label").click()
driver.find_element_by_name("_txtUserName").clear()
driver.find_element_by_name("_txtUserName").send_keys("test")
driver.find_element_by_name("_txtPassword").clear()
driver.find_element_by_name("_txtPassword").send_keys("test")
driver.find_element_by_xpath("//div[@class='btn']/input[2][@value='Login']").click()
welcome = driver.find_element_by_xpath("//div[@id='navbar-brand-centered']/ul/li[6]/a").text
print(welcome)
