from bs4 import BeautifulSoup
from src.car_price_prediction.data_scraping import scrape_utils
from src.car_price_prediction.data_scraping.scrape_constants import CarTemp


def analyze_contents(page_contents):
    soup = BeautifulSoup(page_contents, "html.parser")
    data = scrape_utils.clean_ad(get_car_ad(soup))
    return data


def get_car_ad(soup):
    car_ad = get_car_params(soup)
    car_ad.update(get_ad_info(soup))
    return car_ad


def get_car_params(soup):
    parameters = {}
    try:
        for sample in soup.find_all("dl", "chars-item"):
            parameters[sample.dt.text] = (
                sample.dt.find_next_sibling("dt").text.strip().lower())
        return parameters
    except (TypeError, AttributeError):
        return parameters


def get_ad_info(soup):
    ad_info = {}
    for detail, get_detail in {CarTemp.PRICE: get_price, CarTemp.PHOTO_URLS: get_photos_urls,
                               CarTemp.EXPIRED: get_expiration_status, CarTemp.PUBLISHED_AT: get_publish_date,
                               CarTemp.BRAND: get_brand, CarTemp.MODEL: get_model}.items():
        try:
            ad_info[detail] = get_detail(soup)
        except (AttributeError, TypeError, IndexError):
            continue
    return ad_info


def get_price(soup):
    price = soup.find('span', attrs={'class': 'card-price-main'})
    return price.text.strip()


def get_photos_urls(soup):
    photos_urls = []
    for photo in soup.find_all("img", "catalog-item-cover-img"):
        photos_urls.append(photo['src'])
    return photos_urls


def get_expiration_status(soup):
    expiration = soup.find("div", {'id': 'expired'})
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
