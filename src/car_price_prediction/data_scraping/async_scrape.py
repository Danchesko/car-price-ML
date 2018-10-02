import pandas as pd
import asyncio
from aiohttp import ClientSession
from src.car_price_prediction.data_scraping.page_scraper import analyze_contents

PAGE_URL = "https://cars.kg/offers/{}.html"
cars = []

def parse(start, end):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(start, end))
    return loop.run_until_complete(future)  


async def run(start, end):
    tasks = []
    sem = asyncio.Semaphore(100)
    async with ClientSession() as session:
        for i in range(start, end):
            task = asyncio.ensure_future(fetch(sem, PAGE_URL.format(i), session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        return await responses
    
    
async def fetch(sem, url, session):
    async with sem:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.read()
                contents = analyze_contents(data.decode('utf-8'))
                return contents


#if __name__=="__main__":
#    data = pd.DataFrame(list(filter(None, parse(920000,920040))))
#    data.to_csv("test.csv", index = False)
    