from bs4 import BeautifulSoup
from src.car_price_prediction.data_scraping import scrape_utils
from src.car_price_prediction.data_scraping.scrape_constants import Car


def analyze_contents(page_contents):
    soup = BeautifulSoup(page_contents, "html.parser")
    try:
        data = scrape_utils.clean_ad(get_car_ad(soup))
        return data
    except Exception:
        return None
        
    


def get_car_ad(soup):
    car_ad = get_car_params(soup)
    car_ad.update(get_ad_info(soup))
    return car_ad


def get_car_params(soup):
    parameters = {}
    for sample in soup.find_all("dl", "chars-item"):
        parameters[sample.dt.text] = (sample.dt.
                  find_next_sibling("dt").text.strip().lower())
    return parameters


def get_ad_info(soup):    
    ad_info = {}
    for detail, get_detail in {Car.PRICE:get_price, Car.PHOTO_URLS:get_photos_urls,
                               Car.EXPIRED:get_expiration_status, Car.PUBLISHED_AT:get_publish_date,
                               Car.BRAND:get_brand, Car.MODEL:get_model}.items():
        try:
            ad_info[detail]=get_detail(soup)
        except (AttributeError, TypeError, IndexError):
            continue
    return ad_info
    

def get_price(soup):
    price = soup.find('span', attrs={'class': 'card-price-main'})
    return price.text.strip()


def get_photos_urls(soup):
    photos_urls=[]
    for photo in soup.find_all("img", "catalog-item-cover-img"):
        photos_urls.append(photo['src'])
    return photos_urls


def get_expiration_status(soup):
    expiration = soup.find("div", {'id':'expired'})
    if expiration:
        return "Expired"
    else:
        return "Active"
    

def get_publish_date(soup):
    return soup.find("div", "stat-date").text


def get_brand(soup):
    brand = soup.find_all("li", "breadcrumbs-item")
    return brand[2].span.text.strip().lower()


def get_model(soup):
    model = soup.find("div", "useful-links").find_all('li')[1]
    return " ".join(model.a.text.strip().lower().split()[2:])