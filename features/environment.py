from datetime import datetime

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utils import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    context.driver.quit()


'''def after_step(contex, step):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    if step.status == 'failed':
        allure.attach(contex.driver.get_screenshot_as_png(),
                      name=step.text + ". TIME: " + time_stamp,
                      attachment_type=AttachmentType.PNG)'''
