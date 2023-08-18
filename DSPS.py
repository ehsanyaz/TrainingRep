# DigiKala Scraping Using PlayWright Synco

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def func():
    with sync_playwright() as sp:
        browser = sp.chromium.launch()
        page    = browser.new_page()
        url     = "https://www.digikala.com/search/category-book/"
        page.goto(url)
        page.wait_for_selector('h3')
        return page.content()


html = func()
soup = BeautifulSoup(html, "html.parser")
book_names = soup.find_all("h3", attrs={
    "class": "ellipsis-2 text-body2-strong color-700 styles_VerticalProductCard__productTitle__6zjjN"})
for book_name in book_names:
    print(book_name.text)
