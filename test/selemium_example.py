# -*- coding: utf-8 -*-

from lxml import html
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver):
    driver.get("http://www.sportbirmingham.org/directory?sport=&radius=15&postcode=B16+8QG&submit=Search")
    try:
        for link in driver.find_elements_by_xpath('//h2[@class="heading"]/a'):
            link.click()
            emailAdress = driver.find_element_by_xpath('//div[@id="widget-contact"]//a‌​').get_attribute('hr‌​ef')
            print emailAdress
    except TimeoutException:
        print "not found"


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()