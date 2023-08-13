#DigiKala Scraping Using Puppeteer

from bs4 import BeautifulSoup

# asynchronous example:
import asyncio
from playwright.async_api import async_playwright

async def func():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        url = "https://www.digikala.com/search/category-book/"
        await page.goto(url)
        await page.wait_for_selector('h1')
        return url, await page.content()
url , html = asyncio.run(func())
soup = BeautifulSoup(html,"html.parser")
content = soup.find("h3", attrs = {"class" : "ellipsis-2 text-body2-strong color-700 styles_VerticalProductCard__productTitle__6zjjN"})
print(content.text)