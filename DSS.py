# DigiKala Scraping Using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from bs4 import BeautifulSoup

browser = webdriver.Firefox()  # start a web browser
browser.get("https://www.digikala.com/search/category-book/")  # navigate to URL
# wait for page to load
# by waiting for <h3> element to appear on the page
title = (
    WebDriverWait(driver=browser, timeout=10)
    .until(visibility_of_element_located((By.CSS_SELECTOR, "h3")))
    .text
)
# retrieve fully rendered HTML content
content = browser.page_source
browser.close()

soup = BeautifulSoup(content, "html.parser")
print(soup.find("h3", attrs = {"class":"ellipsis-2 text-body2-strong color-700 styles_VerticalProductCard__productTitle__6zjjN"}).text)