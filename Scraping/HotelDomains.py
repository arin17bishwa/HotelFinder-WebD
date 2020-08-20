from bs4 import BeautifulSoup as bs
import requests,os,sys
from django.conf import settings
ROOT_PATH=str(os.path.sep).join(str(settings.BASE_DIR).split(os.path.sep)[:-2])
if ROOT_PATH not in sys.path:sys.path.append(ROOT_PATH)
from Scraping.googling import get_results
import Scraping.HotelScrapers as hs

def oyo(soup):
    with open('oyo.txt','w') as f:
        f.write(soup.prettify())
    return

def tripadvisor(soup):
    with open('tripadvisor.txt', 'w') as f:
        f.write(soup.prettify())
    return

def makemytrip(soup):
    with open('makemytrip.txt','w') as f:
        f.write(soup.prettify())
    return

def booking(soup):
    with open('booking.txt','w') as f:
        f.write(soup.prettify())
    return

def trivago(soup):
    with open('trivago.txt','w') as f:
        f.write(soup.prettify())
    return

def yatra(soup):
    with open('yatra.txt','w') as f:
        f.write(soup.prettify())
    return

def agoda(soup):
    with open('agoda.txt','w') as f:
        f.write(soup.prettify())
    return

def cleartrip(soup):
    with open('cleartrip.txt','w') as f:
        f.write(soup.prettify())
    return

def treebo(soup):
    with open('treebo.txt', 'w') as f:
        f.write(soup.prettify())
    return

def hotels(soup):
    with open('hotels.txt', 'w') as f:
        f.write(soup.prettify())
    return

SCRAPERS={
    'tripadvisor':hs.tripadvisor,
}



FUNCTIONS={
    'oyorooms':oyo,#503
    'makemytrip':makemytrip,
    'tripadvisor':tripadvisor,
    #'trivago':trivago,#403
    'yatra':yatra,#443
    'booking':booking,
    'agoda':agoda,
    'cleartrip':cleartrip,
    'treebo':treebo,
    'hotels':hotels,
}


def get_domain(url):
    return url.split('.')[1]

def main(query='kolkata'):
    items=get_results(query)
    info=[]
    for item in items:
        if item[0] in SCRAPERS:
            try:
                response=requests.get(item[1],timeout=5)
            except Exception as e:
                continue
            if not response.ok:continue
            soup=bs(response.text,features="html.parser")
            answer=SCRAPERS[item[0]](soup)
            if answer==0:continue
            info.extend(answer)
    return info
