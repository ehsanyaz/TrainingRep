#DigiKala Scraping Using Puppeteer

from bs4 import BeautifulSoup

# asynchronous example:
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        url = "https://www.digikala.com/search/category-book/"
        await page.goto(url)
        await page.wait_for_selector('h1')
        return url, await page.content()
url , html = asyncio.run(run())
soup = BeautifulSoup(html,"html.parser")
content = soup.find("h1")
print(content.text)