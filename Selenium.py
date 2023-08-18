from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

browser = webdriver.Firefox()  # start a web browser
browser.get("https://fa.wikipedia.org/wiki/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86")  # navigate to URL
# wait for page to load
# by waiting for <h3> element to appear on the page
WebDriverWait(driver=browser, timeout=10).until(visibility_of_element_located((By.CSS_SELECTOR, "h3")))

# retrieve fully rendered HTML content
content = browser.page_source

# Title
print("************")
title = browser.find_element(By.ID, "firstHeading")
print(title.text)
print("************")

# ScreenShot
browser.save_screenshot("ScreenShot.png")
print("ScreenShot Taken")

# links
links = browser.find_elements(By.CLASS_NAME,"mw-redirect")
print("************")
print("Links")
counter = 0
for link in links:
    counter = counter + 1
    print(counter, end="- \n")
    print(link.text)
    print(link.get_attribute("href"))
print("************")


# Content
print("************")
print("Content")
par = browser.find_elements(By.TAG_NAME, "p")
for p in par:
    print(p.text)
print("************")



browser.close()
