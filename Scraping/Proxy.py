import requests,random,os,json
from django.conf import settings
from bs4 import BeautifulSoup as bs
PROXY_LIST=[]
CWD=os.getcwd()

def get_proxy():
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    soup = bs(response.content, features="html.parser")
    hosts=(list(map(lambda x:':'.join(x),
                                list(zip(map(lambda x:x.text,soup.findAll('td')[::8]),
                                         map(lambda x:x.text,soup.findAll('td')[1::8]))))))


    js=list(map(lambda x:{'http':x,'https':x},hosts))
    with open(os.path.join(CWD,'proxies.json'),'w') as f:
        json.dump(js,f,indent=2)



def proxy_request(request_type,url,**kwargs):
    c=r=0
    while True:
        c+=1
        if c>20:break
        try:
            with open(os.path.join(CWD,'proxies.json')) as f:
                proxies=json.load(f)
            proxy=random.choice(proxies)
            print(f'Using proxy:{proxy}')
            r=requests.request(request_type,url,proxies=None,timeout=5,**kwargs)#use 'proxies=proxy' if you wish to use a proxy
            break
        except Exception as e:
            print(e)
            pass
    return r
