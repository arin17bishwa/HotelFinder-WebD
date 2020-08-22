from bs4 import BeautifulSoup as bs
from Scraping.Proxy import proxy_request
from Scraping.googling import get_results
import Scraping.HotelScrapers as hs
PROXY_LIST=[]

SCRAPERS={
    'tripadvisor':hs.tripadvisor,
}

def get_domain(url):
    return url.split('.')[1]

def main(query='kolkata'):
    items=get_results(query)
    if items is None:return None
    info=[]
    for item in items:
        if item[0] in SCRAPERS:
            try:
                print(item)
                response=proxy_request(request_type='get',
                                       url=item[1],
                                       )
            except Exception as e:
                print(e)
                continue

            if response==0 or not response.ok:continue

            soup=bs(response.text,features="html.parser")
            answer=SCRAPERS[item[0]](soup)
            if answer==0:continue
            info.extend(answer)

    return info