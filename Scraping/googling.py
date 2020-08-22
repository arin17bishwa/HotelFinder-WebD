from googleapiclient.discovery import build
import os
from googleapiclient.errors import HttpError
API_KEY = os.environ.get('GOOGLE_API_KEY')
CSE_ID=os.environ.get('GOOGLE_CSE_ID')


SUPPORTED_DOMAINS=(
    'tripadvisor',

)

def f(items):
    d=[(get_domain(item),item) for item in items]
    return d

def google_query(query, api_key, cse_id, **kwargs):
    query_service = build("customsearch",
                          "v1",
                          developerKey=api_key
                          )
    query_results={}
    try:
        query_results = query_service.cse().list(q=query,    # Query
                                             cx=cse_id,  # CSE ID
                                             **kwargs
                                             ).execute()
    except HttpError:
        print('ERROES',HttpError)

    return query_results.get('items')

def get_domain(url):
    return url.split('.')[1]

def get_results(placename='kolkata'):
    query=f'hotels in {placename}'
    url_list=[]
    start=1
    num=10
    while len(url_list)<2 and start<20:
        my_results = google_query(query,
                                  API_KEY,
                                  CSE_ID,
                                  num=10,
                                  start=start
                                  )
        start+=num
        if my_results is None:raise Exception('CSE API ERROR')

        for result in my_results:
            if get_domain(result['link']) in SUPPORTED_DOMAINS:
                url_list.append(result['link'])

    url_list=f(url_list)
    return url_list
