# DigiKala Scraping Using PlayWright Asynco

import threading
import time
from random import random

from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


async def get_screenshot(url):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        print("1")
        page = await browser.new_page()
        print("1.5")
        await page.goto(url)
        print("2")

        await page.wait_for_selector('h3')
        print("3")

        time.sleep(2)
        print("4")

        p = "imgs//" + str(int(random() * 100000000000)) + ".png"


        await page.screenshot(path=p)
        print("5")
        #await browser.close()
        #return await page.content()


def htmlcoder(url):
    html = asyncio.run(get_screenshot(url))
    '''soup = BeautifulSoup(html, "html.parser")
    pic_urls = soup.find_all("img", attrs={
        "class": "w-full bg-neutral-000 inline-block"})
    for pic_url in pic_urls:
        print(pic_url.source)
        print(pic_url.text)'''


def func(url, selector):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url, timeout=100000)
        page.wait_for_selector(selector)
        content = page.content()
        browser.close()
        return content


products = []

for i in range(51, 52):
    time.sleep(5)
    html = func("https://www.digikala.com/search/category-intellectual/?page=" + str(i) + "&sort=7", 'h3')
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all("div", attrs={"class": "product-list_ProductList__item__LiiNI"})
    for div in divs:
        a_tag = div.find('a')
        if a_tag:
            #time.sleep(5)
            href = a_tag.get('href')
            htmlcoder('https://digikala.com' + href + '#gallery')
            #products.append('https://digikala.com' + href + '#gallery')
    '''print("list done")
    trds = []
    for pr in products:
        trds.append(threading.Thread(target=htmlcoder, args=(pr,)))

    for trd in trds:
        trd.start()

    for trd in trds:
        trd.join()'''

