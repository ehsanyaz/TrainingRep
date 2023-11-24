# DigiKala Scraping Using PlayWright Asynco

import threading
import time
from random import random

from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


async def func(url):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()

        await page.goto(url)
        await page.wait_for_selector('h3')
        print("doooooo")
        time.sleep(5)
        p = str(int(random() *10000000000))  + ".png"
        print(p)
        await page.screenshot(path=p)


        return await page.content()


def htmlcoder(url):
    print("starting")
    html = asyncio.run(func(url))
    soup = BeautifulSoup(html, "html.parser")

    '''pic_urls = soup.find_all("img", attrs={
        "class": "w-full bg-neutral-000 inline-block"})
    for pic_url in pic_urls:
        print(pic_url.source)
        print(pic_url.text)'''


def func1(url, selector):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()

        context = browser.new_context()

        page = context.new_page()
        page.goto(url, timeout=100000)
        page.wait_for_selector(selector)
        content = page.content()
        return content


products = []
for i in range(51, 52):
    html = func1("https://www.digikala.com/search/category-intellectual/?page={i}&sort=7", 'h3')
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all("div", attrs={"class": "product-list_ProductList__item__LiiNI"})

    for div in divs:
        a_tag = div.find('a')

        if a_tag:
            href = a_tag.get('href')
            products.append('https://digikala.com' + href + '#gallery')



print(products)
trds = []


for pr in products:
    trds.append(threading.Thread(target=htmlcoder,args=(pr,)))

for trd in trds:
    trd.start()

for trd in trds:
    trd.join()
