from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('http://www.airindia.in/contact-details.htm')

doc = driver.page_source

emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for eamil in emails:
	print(email)