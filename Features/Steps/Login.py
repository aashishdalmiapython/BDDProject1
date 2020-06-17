from selenium.webdriver import Chrome
from behave import *
import time

@given(u'user is on Login page')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@id='tab2']/following-sibling::label").click()

@when(u'user enters Login ID')
def step_impl(context):
    context.driver.find_element_by_name("_txtUserName").clear()
    context.driver.find_element_by_name("_txtUserName").send_keys("test")


@when(u'user enters Login Password')
def step_impl(context):
    context.driver.find_element_by_name("_txtPassword").clear()
    context.driver.find_element_by_name("_txtPassword").send_keys("test")

@when(u'user click on SignIn button')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@class='btn']/input[2][@value='Login']").click()

@then(u'user should get redirected to Dashboard')
def step_impl(context):
    welcome = context.driver.find_element_by_xpath("//div[@id='navbar-brand-centered']/ul/li[6]/a").text
    print(welcome)
    assert welcome == 'Welcome Mr. test'

@then(u'user should get logout on clicking logout button')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element_by_xpath("//a[text()='logout']").click()