from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, FloatField, validators



class PredictionForm(FlaskForm):
    from src.server import data_service
    brand = SelectField('Марка', [validators.Required()], choices=data_service.get_brands(), default = data_service.DEFAULT_VALUE)
    model = SelectField('Модель',choices=[])
    year = IntegerField('Год выпуска',  [validators.DataRequired()])
    mileage = IntegerField('Пробег')
    capacity = FloatField('Объем')
    wheel = SelectField('Руль', choices=data_service.get_wheel_types(), default = 'левый')
    fuel = SelectField('Тип топлива', choices=data_service.get_fuel_types(), default = 'бензин')
    color = SelectField('Цвет', choices=data_service.get_colors(), default = 'белый')
    carcass = SelectField('Тип кузова ', choices=data_service.get_carcass_types())
    drive = SelectField('Привод ', choices=data_service.get_drive_types())
    transmission = SelectField('Привод ', choices=data_service.get_transmission_types())


        
    