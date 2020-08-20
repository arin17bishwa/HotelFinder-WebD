from googleapiclient.discovery import build
import os
API_KEY ='YOUR API KEY'
CSE_ID='YOUR CSE ID'




SUPPORTED_DOMAINS=(
    'goibibo',
    'tripadvisor',
    'trivago',
    'booking',
    'agoda',
    'cleartrip',
    'treebo',
)

def f(items):
    d=[(get_domain(item),item) for item in items]
    return d

def google_query(query, api_key, cse_id, **kwargs):
    query_service = build("customsearch",
                          "v1",
                          developerKey=api_key
                          )
    query_results = query_service.cse().list(q=query,    # Query
                                             cx=cse_id,  # CSE ID
                                             **kwargs
                                             ).execute()
    return query_results['items']

def get_domain(url):
    return url.split('.')[1]

def get_results(placename='kolkata'):
    query=f'hotels in {placename}'
    #print(query)
    url_list=[]
    start=1
    num=10
    while len(url_list)<10 and start<50:
        my_results = google_query(query,
                                  API_KEY,
                                  CSE_ID,
                                  num=10,
                                  start=start
                                  )
        start+=num
        for result in my_results:
            if get_domain(result['link']) in SUPPORTED_DOMAINS:
                url_list.append(result['link'])
    url_list=f(url_list)
    return url_list
