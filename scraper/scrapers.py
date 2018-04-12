import requests
from bs4 import BeautifulSoup as bs


def rtveuro_scraper(url):


    page = requests.get(url)

    soup = bs(page.text, 'html.parser')

    price = soup.find('div', {'class': "price-normal selenium-price-normal"})
    price = price.get_text().strip()[:-3]

    if ',' in price:
        price = price.replace(',', '.')

    return float(price)


def mediamarkt_scraper(url):


    page = requests.get(url)

    soup = bs(page.text, 'html.parser')

    prod_id = soup.find('div', {'class': 'js-ajaxChain_item js-initForm'})['data-offer-id']

    price = soup.find('a', {'data-offer-id': prod_id})['data-offer-price']

    return float(price)

def mediaexpert_scraper(url):


    page = requests.get(url)

    soup = bs(page.text, 'html.parser')

    price = soup.find('p', {'class': "price"})

    price = price.get_text()

    price = price[:len(price) - 2] + '.' + price[len(price) - 2:]

    return float(price)