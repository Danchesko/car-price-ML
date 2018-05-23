from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd 
import sys
sys.path.append("../data_extraction")
import load_or_save_dataset

PAGE_URL = "https://cars.kg/offers/%d.html"
PARAMS_TO_CLEAN=['Год выпуска','Пробег','Объём','Мощность','Цена']
PARAM_PRICE = "Цена"

def write_to_csv(start=865990,stop=866000,path = None):
    """Function return True if data was saved in a given or 
    default file with 'xlsx' extension, False otherwise.
    Start, stop arguments are arguments for building an html path
    for scraping. There are default, although can be adjusted,but 
    webpage content knowledge(cars.kg) is needed to change start, stop arguments
    """
    df = make_data_frame(start,stop)
    if path==None:
        return load_or_save_dataset.save_raw_dataset(df)
    else:
        return load_or_save_dataset.save_raw_dataset(df,path)
    
def make_data_frame(start,stop):  
    list_of_dicts = make_list_of_dicts(start,stop)
    df = pd.DataFrame(list_of_dicts)
    return df

def make_list_of_dicts(start,stop):
    list_of_dicts = []
    for page in range(start,stop,1):
        try:
            data = get_dict(page)
            if data!=None:
                list_of_dicts.append(data)
        except:
            continue
    return list_of_dicts

def get_dict(address):    
    page_contents = open_page(PAGE_URL%address) 
    if page_contents!=None:
        return analyze_contents(page_contents)
    
def open_page(page):
    try:
        page = urlopen(page)
        page_contents=page.read().decode("utf-8")
        return page_contents
    except:
        return None
    
def analyze_contents(page_contents):
    soup = BeautifulSoup(page_contents,"html.parser")
    data = create_dict(soup.find_all("dl","chars-item"))
    price = soup.find('span', attrs={'class':'card-price-main'}).text.strip()
    data[PARAM_PRICE] = price
    return clean_dict(data)
    
def create_dict(samples):
    parameters={}
    for sample in samples:
        parameter_name = sample.dt.text
        parameter_value = sample.dt.find_next_sibling("dt").text.strip().lower()
        parameters[parameter_name] = parameter_value
    return parameters

def clean_dict(dictionary):
    params_to_clean = PARAMS_TO_CLEAN
    for param in params_to_clean:
        if param in dictionary.keys():
            dictionary[param] =float(re.findall(r"[-+]?\d*\.\d+|\d+", dictionary[param])[0])
    return dictionary

        
        
        
        