import pandas as pd
from argparse import Namespace


def get_test_data(arguments, columns):
    car_params = Namespace(**arguments)
    test_data = pd.DataFrame(data=[[int(car_params.year),
                                    car_params.transmission,
                                    car_params.brand,
                                    float(car_params.capacity),
                                    car_params.drive,
                                    float(car_params.mileage),
                                    car_params.wheel,
                                    car_params.carcass,
                                    car_params.fuel,
                                    car_params.color]],
                             columns=columns)
    return test_data
