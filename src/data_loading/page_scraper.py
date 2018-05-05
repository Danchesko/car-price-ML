from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd 
import os


def open_page(page):
    try:
        page = urlopen(page)
        page_contents=page.read().decode("utf-8")
        return page_contents
    except:
        return None
    
def create_dict(samples):
    parameters={}
    for sample in samples:
        parameter_name = sample.dt.text
        parameter_value = sample.dt.find_next_sibling("dt").text.strip().lower()
        parameters[parameter_name] = parameter_value
    return parameters

def clean_dict(dictionary):
    params_to_clean = ['Год выпуска','Пробег','Объём','Мощность','Цена']
    for i in params_to_clean:
        if i in dictionary.keys():
            dictionary[i] =float(re.findall(r"[-+]?\d*\.\d+|\d+", dictionary[i])[0])
    return dictionary

def get_dict(address):    
    page_contents = open_page("https://cars.kg/offers/%d.html"%address) 
    if page_contents!=None:
        soup = BeautifulSoup(page_contents,"html.parser")
        data = create_dict(soup.find_all("dl","chars-item"))
        price = soup.find('span', attrs={'class':'card-price-main'}).text.strip()
        data["Цена"] = price
        data=clean_dict(data)
        return data
    
def make_list_of_dicts(start,stop):
    list_of_dicts = []
    for i in range(start,stop,1):
        try:
            data = get_dict(i)
            if data!=None:
                list_of_dicts.append(data)
        except:
            continue
    return list_of_dicts
   
def make_data_frame(list_of_dicts):  
    df = pd.DataFrame(list_of_dicts)
    return df

if __name__=="__main__":
    if not os.path.isfile("cars_raw_data.csv"):
        df = make_data_frame(make_list_of_dicts(865000,865002))
        df.to_csv("cars_raw_data.csv", index=False,encoding="utf-8-sig")
    else:
        print("File already exists")
        
        
        
        