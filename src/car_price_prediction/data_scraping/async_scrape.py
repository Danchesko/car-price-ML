import pandas as pd
import asyncio
from aiohttp import ClientSession
from src.car_price_prediction.data_scraping import scrape_constants
from src.car_price_prediction.data_scraping.page_scraper import analyze_contents


cars = []

def parse(start, end):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(start, end))
    return loop.run_until_complete(future)  


async def run(start, end):
    tasks = []
    sem = asyncio.Semaphore(500)
    async with ClientSession() as session:
        for i in range(start, end):
            task = asyncio.ensure_future(fetch(sem, scrape_constants.PAGE_URL.format(i), session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        return await responses
    
        
async def fetch(sem, url, session):
    async with sem:
        async with session.get(url) as response:
            try:
                data = await response.read()
                contents = analyze_contents(data.decode('utf-8'))
                contents[scrape_constants.URL_COL_NAME] = url
                return contents
            except TypeError:
                return None


if __name__=="__main__":
    data = pd.DataFrame(list(filter(None, parse(700000,901000))))
    writer = pd.ExcelWriter('../../../data/raw/new_raw_data.xlsx')
    data.to_excel(writer, 'Sheet1', index = False)
    writer.save()    
