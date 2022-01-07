from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
driver = webdriver.Chrome()
def lookup(driver):
   driver.get("http://www.sportbirmingham.org/directory?sport=&radius=15&postcode=B16+8QG&submit=Search")
links = [link.get_attribute('href') for link in driver.find_elements_by_xpath('//h2[@class="heading"]/a')]
page_counter = 1
while True:
    try:
        page_counter += 1
        driver.find_element_by_link_text(str(page_counter)).click()
        links.extend([link.get_attribute('href') for link in driver.find_elements_by_xpath('//h2[@class="heading"]/a')])
    except NoSuchElementException:
        break
    try:
        for link in links:
            driver.get(link)
            try:
                emailAdress = driver.find_element_by_xpath('//div[@id="widget-contact"]//a').text
                print (emailAdress)
            except NoSuchElementException:
                print ("No email specified")
    except TimeoutException:
        print ("not found")