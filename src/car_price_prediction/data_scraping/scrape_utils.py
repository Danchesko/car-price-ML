import re
from src.car_price_prediction.data_scraping.scrape_constants import Car


PARAMS_TO_CLEAN = [Car.YEAR, Car.MILEAGE, Car.CAPACITY, Car.POWER, Car.PRICE]


def clean_ad(car_info):
    car_info = clean_num_params(car_info)
    car_info = clean_model_name(car_info)
    return car_info


def clean_num_params(car_info):
    params_to_clean = PARAMS_TO_CLEAN
    for param in params_to_clean:
        if param in car_info.keys():
            car_info[param] = float(
                re.findall(r"[-+]?\d*\.\d+|\d+", car_info[param])[0])
    return car_info


def clean_model_name(car_info):
    try:
        car_info[Car.MODEL] = car_info[Car.MODEL].replace(car_info[Car.BRAND], "").strip()
        return car_info
    except KeyError:
        return car_info