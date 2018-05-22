from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd 
import os

PAGE_URL = "https://cars.kg/offers/%d.html"
REL_PATH_FOR_CSV = "../../data/raw/cars_test_data.csv"
FILE_EXISTS_MESSAGE = "File already exists"
PARAMS_TO_CLEAN=['Год выпуска','Пробег','Объём','Мощность','Цена']
PARAM_PRICE = "Цена"

def main(start = 866000, stop = 867500):
    if not os.path.isfile(REL_PATH_FOR_CSV):
        write_to_csv(start,stop)
    else:
        print(FILE_EXISTS_MESSAGE)
        
def write_to_csv(start,stop):
    df = make_data_frame(start,stop)
    df.to_csv(REL_PATH_FOR_CSV, index=False,encoding="utf-8-sig")
    
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

        
if __name__=="__main__":
    main()
        
        
        
        