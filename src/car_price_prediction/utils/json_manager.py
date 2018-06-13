import pandas as pd


def get_test_data(arguments, columns):
    year = int(arguments['year'])
    trmn = arguments['transmission']
    brand = arguments['brand']
    urgency = arguments['urgency']
    capacity = float(arguments['capacity'])
    drive = arguments['drive']
    mileage = float(arguments['mileage'])
    wheel = arguments['wheel']
    carcass = arguments['carcass']
    fuel = arguments['fuel']
    color = arguments['color']
    test_data = pd.DataFrame(data=[[year, trmn, brand, capacity,
                                    drive, mileage, wheel, urgency, 
                                    carcass, fuel, color]], columns=columns)
    return test_data
