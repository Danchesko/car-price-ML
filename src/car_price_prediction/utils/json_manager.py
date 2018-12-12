import pandas as pd
from argparse import Namespace
from dateutil.parser import parse


def get_test_data(arguments, columns):
    car_params = Namespace(**arguments)
    test_data = pd.DataFrame(data=[[int(car_params.year),
                                    parse(car_params.publication).toordinal(),
                                    car_params.transmission,
                                    car_params.brand,
                                    car_params.model,
                                    float(car_params.capacity),
                                    car_params.drive,
                                    float(car_params.mileage),
                                    car_params.wheel,
                                    car_params.carcass,
                                    car_params.fuel,
                                    car_params.color]],
                             columns=columns)
    return test_data