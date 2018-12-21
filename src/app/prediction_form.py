from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, FloatField, validators
from wtforms.widgets import Input


class PredictionForm(FlaskForm):
    from src.server import data_service
    brand = SelectField('Марка', [validators.InputRequired()], choices=data_service.get_brands(), default = data_service.DEFAULT_VALUE)
    model = SelectField('Модель',[validators.InputRequired()], choices=[])
    year = IntegerField('Год выпуска', [validators.InputRequired()], widget=Input('number'))
    mileage = IntegerField('Пробег', [validators.InputRequired()], widget=Input('number'))
    capacity = FloatField('Объем', [validators.InputRequired()], widget=Input('number'))
    wheel = SelectField('Руль', choices=data_service.get_wheel_types(), default = 'левый')
    fuel = SelectField('Тип топлива', choices=data_service.get_fuel_types(), default = 'бензин')
    color = SelectField('Цвет', choices=data_service.get_colors(), default = 'белый')
    carcass = SelectField('Тип кузова ', choices=data_service.get_carcass_types())
    drive = SelectField('Привод ', choices=data_service.get_drive_types())
    transmission = SelectField('Коробка передач ', choices=data_service.get_transmission_types())


        
    