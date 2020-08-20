
def tripadvisor(page_soup):
    c=0
    info=[]
    page_soup=page_soup.find('div',class_='bodycon_main')
    try:
        for tile in page_soup.find_all('div',class_='ui_column is-8 main_col allowEllipsis'):
            dic={}
            if c==30:break
            hotel_name=tile.find('div',class_='listing_title')
            hotel_link=str(hotel_name)
            hotel_link=hotel_link.split('href')[1].split('"')[1]
            hotel_name=hotel_name.a.text
            hotel_price=tile.find('div',class_='price autoResize').text
            if hotel_price=='':
                hotel_price='UNAVAILABLE'
            dic['name']=hotel_name.strip().split(' \n ')[0]
            dic['price']=hotel_price
            dic['link']=str('https://www.tripadvisor.in/' + hotel_link)
            info.append(dic)
            c+=1
    except Exception as e:
        #print(e)
        return []
    return info
