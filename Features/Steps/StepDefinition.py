from behave import *
from selenium.webdriver import Chrome

@given(u'user is on Registration page')
def step_impl(context):
    context.driver.get("https://www.thetestingworld.com/testings")


@when(u'user enters username')
def step_impl(context):
    context.driver.find_element_by_name("fld_username").send_keys("aashish")


@when(u'user enters email id')
def step_impl(context):
    context.driver.find_element_by_name("fld_email").send_keys("abc@gmail.com")


@when(u'user enters password')
def step_impl(context):
    context.driver.find_element_by_name("fld_password").send_keys("abc@123")


@when(u'user click on sign up button')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Sign up']").click()


@then(u'user should get registered sucessfully')
def step_impl(context):
    print("User gets registered")


@when(u'user enters duplicate username')
def step_impl(context):
    context.driver.find_element_by_name("fld_username").send_keys("aashish")


@when(u'user enters duplicate email id')
def step_impl(context):
    context.driver.find_element_by_name("fld_email").send_keys("abc@gmail.com")
