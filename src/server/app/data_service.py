class DataService:

    DEFAULT_VALUE = ''
    ALTERNATIVE_CHOICE = ('другое', 'другое')

    
    def __init__(self, data):
        self.data = data

    @staticmethod
    def add_defaults(elements, default_message):
        return [(DataService.DEFAULT_VALUE, default_message)] + elements
    
    @staticmethod
    def add_alternative(elements):
        elements.append(DataService.ALTERNATIVE_CHOICE)
        return elements

    @staticmethod
    def add_values(elements, default_message):
        return DataService.add_alternative(DataService.add_defaults(elements, default_message))
    
    
    def get_brands(self):
        brands = sorted([(brand, brand.capitalize()) for brand in self.data.Brand.dropna().unique()])
        return DataService.add_values(brands, 'Введите марку машины')
    
    
    def get_models(self, brand):
        models = sorted([(model, model.capitalize()) for model in 
                         self.data[self.data.Brand == brand].Model.dropna().unique()])
        return DataService.add_values(models, 'Введите модель машины')
    
    
    def get_wheel_types(self):
        wheel_choices = [(wheel, wheel.capitalize()) for wheel in self.data.Wheel.dropna().unique()]
        return wheel_choices
    
    
    def get_fuel_types(self):
        fuel_types = [(fuel, fuel.capitalize()) for fuel in self.data.Fuel.dropna().unique()]
        return DataService.add_alternative(fuel_types)
        
    
    def get_colors(self):
        colors = sorted([(color, color.capitalize()) for color in self.data.Color.dropna().unique()])
        return DataService.add_alternative(colors)

    def get_carcass_types(self):
        carcass_types = sorted([(carcass, carcass.capitalize()) for carcass in self.data.Carcass.dropna().unique()])
        return DataService.add_alternative(carcass_types)
    
    def get_drive_types(self):
        drive_types = sorted([(drive, drive.capitalize()) for drive in self.data.Drive.dropna().unique()])
        return drive_types

    def get_transmission_types(self):
        transmission_types = [(transmission, transmission.capitalize()) for transmission in self.data.Transmission.dropna().unique()]
        return DataService.add_alternative(transmission_types)