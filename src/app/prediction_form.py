from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
import pandas as pd

from src.car_price_prediction.utils.dataset_manager import get_cleaned_outliers_dataset

data = get_cleaned_outliers_dataset()

class PredictionForm(FlaskForm):

    brand = SelectField('Марка', choices=sorted([(brand, brand.capitalize()) for brand in data.Brand.unique()]), default = 'toyota')
    submit = SubmitField('Предсказание')