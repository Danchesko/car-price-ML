import re
from bs4 import BeautifulSoup
from src.car_price_prediction.constants import Car

PARAMS_TO_CLEAN = [Car.YEAR, Car.MILEAGE, Car.CAPACITY, Car.POWER, Car.PRICE]


def analyze_contents(page_contents):
    soup = BeautifulSoup(page_contents, "html.parser")
    try:
        data = clean_num_params(get_car_info(soup))
    except Exception:
        return None
    return data


def get_car_info(soup):
    car_info = get_car_params(soup)
    car_info[Car.BRAND] = get_brand(soup)
    car_info[Car.PRICE] = get_price(soup)
    car_info[Car.AD_DATE] = get_ad_date(soup)
    car_info[Car.MODEL] = get_model(soup, car_info[Car.BRAND])
    return car_info


def get_car_params(soup):
    parameters = {}
    for sample in soup.find_all("dl", "chars-item"):
        parameters[sample.dt.text] = (sample.dt.
                  find_next_sibling("dt").text.strip().lower())
    return parameters


def get_brand(soup):
    brand = soup.find_all("li", "breadcrumbs-item")
    return brand[2].span.text.strip().lower()


def get_price(soup):
    price = soup.find('span', attrs={'class': 'card-price-main'})
    return price.text.strip()


def get_model(soup, brand):
    model = soup.find_all("div", "useful-links")[0].ul.li.find_next_sibling(
        "li").a.text.strip().lower().split()[2:]
    return " ".join(model).replace(brand, "").strip()


def get_ad_date(soup):
    return soup.find("div", "stat-date").text
    

def clean_num_params(car_info):
    params_to_clean = PARAMS_TO_CLEAN
    for param in params_to_clean:
        if param in car_info.keys():
            car_info[param] = float(
                re.findall(r"[-+]?\d*\.\d+|\d+", car_info[param])[0])
    return car_info