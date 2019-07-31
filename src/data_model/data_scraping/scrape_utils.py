import re
from .scrape_constants import CarTemp


PARAMS_TO_CLEAN = [
    CarTemp.YEAR,
    CarTemp.MILEAGE,
    CarTemp.CAPACITY,
    CarTemp.POWER,
    CarTemp.PRICE
    ]


def clean_ad(car_info):
    car_info = clean_num_params(car_info)
    car_info = clean_model_name(car_info)
    return car_info


def clean_num_params(car_info):
    params_to_clean = PARAMS_TO_CLEAN
    for param in params_to_clean:
        if param in car_info.keys():
            try:
                car_info[param] = float(
                    re.findall(r"[-+]?\d*\.\d+|\d+", car_info[param])[0])
            except IndexError:
                continue
    return car_info


def clean_model_name(car_info):
    try:
        car_info[CarTemp.MODEL] = car_info[CarTemp.MODEL].replace(
            car_info[CarTemp.BRAND], "").strip()
        return car_info
    except KeyError:
        return car_info
