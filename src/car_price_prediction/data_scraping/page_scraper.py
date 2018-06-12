import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import re
from car_price_prediction.constants import Car

PAGE_URL = "https://cars.kg/offers/%d.html"
PARAMS_TO_CLEAN = [Car.YEAR, Car.MILEAGE, Car.CAPACITY, Car.POWER, Car.PRICE]
PARAM_PRICE, PARAM_BRAND, PARAM_URGENCY = Car.PRICE, Car.BRAND, Car.URGENCY
failed_pages = []


def make_data_frame(start, stop):
    """Start, stop arguments are arguments for building an url
    path for scraping. Function returns scraped data and failed
    pages addresses, so if needed you can scrape them again"""
    list_of_dicts = make_list_of_dicts(start, stop)
    df = pd.DataFrame(list_of_dicts)
    return df, failed_pages


def make_list_of_dicts(start, stop):
    list_of_dicts = []
    for page in tqdm(range(start, stop, 1)):
        try:
            data = get_dict(page)
            if data is not None:
                list_of_dicts.append(data)
        except BaseException:
            continue
    return list_of_dicts


def get_dict(address):
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
    data = create_dict(soup.find_all("dl", "chars-item"))
    data[PARAM_BRAND] = get_model(soup)
    data[PARAM_PRICE] = get_price(soup)
    data[PARAM_URGENCY] = get_urgency(soup)
    return clean_dict(data)


def get_urgency(soup):
    temp_data = soup.find_all("span", "tag is-red")
    if len(temp_data) == 0:
        return None
    return temp_data[0].text.strip().lower()


def get_model(soup):
    temp_data = soup.find_all("li", "breadcrumbs-item")
    return temp_data[2].span.text.strip().lower()


def get_price(soup):
    price = soup.find('span', attrs={'class': 'card-price-main'}).text.strip()
    return price


def create_dict(samples):
    parameters = {}
    for sample in samples:
        parameter_name = sample.dt.text
        parameter_value = sample.dt.find_next_sibling(
            "dt").text.strip().lower()
        parameters[parameter_name] = parameter_value
    return parameters


def clean_dict(dictionary):
    params_to_clean = PARAMS_TO_CLEAN
    for param in params_to_clean:
        if param in dictionary.keys():
            dictionary[param] = float(
                re.findall(r"[-+]?\d*\.\d+|\d+", dictionary[param])[0])
    return dictionary
