import asyncio
import pandas as pd
from aiohttp import ClientSession
from src.car_price_prediction.data_scraping import scrape_constants
from src.car_price_prediction.data_scraping.page_scraper import analyze_contents

failed_pages = []

def get_scraped_dataset(start, end):
    """Start, stop arguments are arguments for building an url path
    for scraping. Function returns scraped data in df and list of
    failed pages. This function is asynchoronous, you can customize
    the number of semaphores, but considerations should be given"""
    car_data= pd.DataFrame(list(filter(None, parse(start,end))))
    return car_data, failed_pages


def parse(start, end):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(start, end))
    return loop.run_until_complete(future)


async def run(start, end):
    tasks = []
    sem = asyncio.Semaphore(500)
    async with ClientSession() as session:
        for i in range(start, end):
            tasks.append(asyncio.ensure_future(fetch(
                    sem, scrape_constants.PAGE_URL.format(i), session)))
        responses = asyncio.gather(*tasks)
        return await responses


async def fetch(sem, url, session):
    async with sem:
        async with session.get(url) as response:
            if response.status < 300:
                data = await response.read()
                contents = analyze_contents(data.decode('utf-8'))
                contents[scrape_constants.CarTemp.URL] = url
                return contents
            elif (int(response.status/100)!=4):
                failed_pages.append(url)