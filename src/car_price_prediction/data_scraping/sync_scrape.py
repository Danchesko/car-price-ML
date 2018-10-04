from tqdm import tqdm
import urllib
import pandas as pd
from urllib.request import urlopen
from src.car_price_prediction.data_scraping import page_scraper, scrape_constants

failed_pages = []


def get_scraped_dataset(start, stop):
    """Start, stop arguments are arguments for building an url
    path for scraping. Function returns scraped data in df and
    failed pages addresses, so if needed you can scrape them again."""
    cars_data = get_cars_data(start, stop)
    df = pd.DataFrame(cars_data)
    return df, failed_pages


def get_cars_data(start, stop):
    return [get_car_data(page) for page in tqdm(range(start, stop))
            if get_car_data(page) is not None]


def get_car_data(address):
    url = scrape_constants.PAGE_URL.format(address)
    page_contents = open_page(url)
    if page_contents:
        car_data = page_scraper.analyze_contents(page_contents)
        car_data[scrape_constants.Car.URL] = url
        return car_data
            
            

def open_page(page):
    try:
        page_contents = urlopen(page).read().decode("utf-8")
        return page_contents
    except urllib.error.HTTPError:
        return None
    except Exception as excpt:
        failed_pages.append(page)
        return None