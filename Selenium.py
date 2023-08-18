from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

browser = webdriver.Firefox()  # start a web browser
browser.get("https://en.wikipedia.org/wiki/Pok%C3%A9mon")  # navigate to URL
# wait for page to load
# by waiting for <h3> element to appear on the page
WebDriverWait(driver=browser, timeout=10).until(visibility_of_element_located((By.CSS_SELECTOR, "h3")))

# retrieve fully rendered HTML content
content = browser.page_source
print("************")
title = browser.find_elements(By.ID,"firstHeading")
for t in title:
    print(t.text)
print("************")

browser.save_screenshot("ScreenShot.png")
'''links = browser.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.get_attribute("href"))'''
'''par = browser.find_elements(By.TAG_NAME,"p")
for p in par:
    print(p.text)'''
browser.close()