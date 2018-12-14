from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, FloatField, validators
import pandas as pd

from src.car_price_prediction.utils.dataset_manager import get_cleaned_outliers_dataset

data = get_cleaned_outliers_dataset()

ALTERNATIVE_OPTION = 'другое'

class PredictionForm(FlaskForm):

    brand = SelectField('Марка', choices=sorted([(brand, brand.capitalize()) for brand in data.Brand.unique()]), default = 'toyota')
    year = IntegerField('Год выпуска',  [validators.DataRequired()])
    mileage = IntegerField('Пробег')
    capacity = FloatField('Объем')
    wheel = SelectField('Руль', choices=[(wheel, wheel.capitalize()) for wheel in data.Wheel.dropna().unique()])
    fuel = SelectField('Тип топлива', choices=[(fuel, fuel.capitalize()) for fuel in data.Fuel.fillna(ALTERNATIVE_OPTION).unique()], default = ALTERNATIVE_OPTION)
    color = SelectField('Цвет', choices=[(color, color.capitalize()) for color in data.Color.fillna(ALTERNATIVE_OPTION).unique()], default = ALTERNATIVE_OPTION)
    carcass = SelectField('Тип кузова ', choices=[(carcass, carcass.capitalize()) for carcass in data.Carcass.dropna().unique()])
    drive = SelectField('Привод ', choices=[(drive, drive.capitalize()) for drive in data.Drive.dropna().unique()])
    transmission = SelectField('Привод ', choices=[(transmission, transmission.capitalize()) for transmission in data.Transmission.dropna().unique()])
    submit = SubmitField('Предсказание')