# Digikala Web Scarping Using PlayWright Asynco

from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright
import requests

# from playwright.sync_api import sync_playwright
# import time
# import json
# import os
# import concurrent

save_directory = 'images'
counter = 0

# Create the directory if it doesn't exist
# os.makedirs(save_directory, exist_ok=True)

# def func(url, selector):
#     with sync_playwright() as pw:
#         browser = pw.chromium.launch()
#         context = browser.new_context()
#         page = context.new_page()
#         page.goto(url, timeout=100000)
#         page.wait_for_selector(selector)
#         content = page.content()
#         return content


async def func(url, selector):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url, timeout=100000)
        await page.wait_for_selector(selector)
        return await page.content()


def save_image(div_gallery):
    response = requests.get(div_gallery['src'], headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    if response.status_code == 200:
        file_path = str(counter) + '.jpg'
        counter = counter + 1
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f'The image has been saved to {file_path}')
    else:
        print('error', response.status_code)


def image_export(url):
    result_img = asyncio.run(func(url, 'h3'))
    soup_gallery = BeautifulSoup(result_img, "html.parser")
    divs_gallery = soup_gallery.find_all('img', src=lambda value: value and value.startswith(
        'https://dkstatics-public.digikala.com/digikala-products/'))
    for div_gallery in divs_gallery:
        save_image(div_gallery)


def getProductUrls(i):
    html = asyncio.run(func("https://www.digikala.com/search/category-kids-bodysuit/?page=" + str(i) + "&sort=7", 'h3'))
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all("div", attrs={"class": "product-list_ProductList__item__LiiNI"})
    for div in divs:
        a_tag = div.find('a')

        if a_tag:
            href = a_tag.get('href')
            href = 'https://digikala.com' + href + '#gallery'
            print('*********************')
            print('product ID :' + href.split('/')[4])
            image_export(href)
            # products.append('https://digikala.com'+href+'#gallery')
    # return products


if __name__ == "__main__":
    products = []

    for i in range(1, 101):
        print('+++++++++++ page number:' + str(i) + '+++++++++++')
        products = getProductUrls(i)

    # with concurrent.futures.ThreadPoolExecutor(10) as executor:
    #     results = [executor.submit(getProductUrls, i) for i in range(1,11)]

    # print(len(products))

    # # for url in products :
    # #     image_export(url)
    # with concurrent.futures.ThreadPoolExecutor(5) as executor:
    #     results = [executor.submit(image_export, url) for url in products]
