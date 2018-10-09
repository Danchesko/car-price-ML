rename_cols= {'URL':'Url',
'Активность':'Expiration',
'Год выпуска':'Year',
'Дата рекламы':'Publication',
'КПП':'Transmission',
'Марка':'Brand',
'Модель':'Model',
'Мощность':'Power',
'Объём':'Capacity',
'Привод':'Drive',
'Пробег':'Mileage',
'Руль':'Wheel',
'Тип кузова':'Carcass',
'Топливо':'Fuel',
'Фото':'Photo_Urls',
'Цвет':'Color',
'Цена':'Price'}

class Car():
    MAX_PRICE = 250000
    MIN_PRICE = 500
    MAX_POWER = 600
    MIN_POWER = 50
    MAX_CAPACITY = 6.5
    MIN_CAPACITY = 0.7
    MAX_MILEAGE = 800000
    MIN_YEAR_MAX_PRICE = {2000:20000, 2005:40000, 2010:50000, 2014:80000}
    MIN_YEAR_FOR_MILEAGE = 2010
    MIN_MILEAGE_FOR_YEAR = 50000
