import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import re
from car_price_prediction.constants import Car

PAGE_URL = "https://cars.kg/offers/%d.html"
PARAMS_TO_CLEAN = [Car.YEAR, Car.MILEAGE, Car.CAPACITY, Car.POWER, Car.PRICE]
failed_pages = []


def get_scraped_dataset(start, stop):
    """Start, stop arguments are arguments for building an url
    path for scraping. Function returns scraped data in df and 
    failed pages addresses, so if needed you can scrape them again"""
    cars_data = get_cars_data(start, stop)
    df = pd.DataFrame(cars_data)
    return df, failed_pages


def get_cars_data(start, stop):
    cars_data = []
    for page in tqdm(range(start, stop, 1)):
        data = get_car_data(page)
        if data is not None:
            cars_data.append(data)
    return cars_data


def get_car_data(address):
    page_contents = open_page(PAGE_URL % address)
    if page_contents is not None:
        return analyze_contents(page_contents)


def open_page(page):
    try:
        page = urlopen(page)
        page_contents = page.read().decode("utf-8")
        return page_contents
    except urllib.error.HTTPError:
        # returns None if page doesn't exist
        return None
    except Exception as excpt:
        failed_pages.append(page)
        return None


def analyze_contents(page_contents):
    soup = BeautifulSoup(page_contents, "html.parser")
    data = get_car_info(soup.find_all("dl", "chars-item"))
    data[Car.BRAND] = get_model(soup)
    data[Car.PRICE] = get_price(soup)
    return clean_info(data)


def get_car_info(samples):
    parameters = {}
    for sample in samples:
        parameter_name = sample.dt.text
        parameter_value = sample.dt.find_next_sibling(
            "dt").text.strip().lower()
        parameters[parameter_name] = parameter_value
    return parameters


def get_model(soup):
    model = soup.find_all("li", "breadcrumbs-item")
    return model[2].span.text.strip().lower()


def get_price(soup):
    price = soup.find('span', attrs={'class': 'card-price-main'}).text.strip()
    return price


def clean_info(car_info):
    params_to_clean = PARAMS_TO_CLEAN
    for param in params_to_clean:
        if param in car_info.keys():
            car_info[param] = float(
                re.findall(r"[-+]?\d*\.\d+|\d+", car_info[param])[0])
    return car_info
