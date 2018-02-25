#!/usr/bin/env python3
#Amazon.co.uk Price Checker V3 / geektechstuff
import bs4, requests, json
#Import the Beautiful Soup and Requests modules
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'}
#Needed a headers otherwise Amazon.co.uk fails to give any details

spends=100
spends=float(spends)

filename='amazlist.json'
with open(filename) as f:
    asin_data=json.load(f)
    for asin in asin_data:
        asintxt=str(asin)
        head,sep,tail=asintxt.partition('<')
        asintxt2=tail
        head,sep,tail=asintxt2.partition('>')
        asintxt3=head.strip()
        print(asintxt3)        
        url = 'http://www.amazon.co.uk/dp/'+asintxt3     
        res=requests.get(url,headers=headers)
#Requests the URL and uses the headers to make the script "look" like a web browser
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,"html.parser")
#Needed the html.parser line otherwise Beautiful Soup gives a warning
        asidprice=soup.select('#priceblock_ourprice')
        asidtitle=soup.select('#productTitle')
        if asidprice == []:
            print('Error')
        else:
            ttext=str(asidtitle)
            head,sep,tail=ttext.partition('>')
            ttext2=tail
            head,sep,tail=ttext2.partition('<')
            title=head.strip()
            print(title)
        
            ptext=str(asidprice)
            head,sep,tail=ptext.partition('£')
            ptext2=tail
            head,sep,tail=ptext2.partition('<')
            price=head
            print('£'+price)
            price=float(head)
            if price > spends:
                print("Still too expensive")
            else:
                print("Its cheap enough to purchase")        
#turns the spanIDs into strings and then removes HTML that I don’t need to print  
    
