import requests
from bs4 import BeautifulSoup
import ssl 
from urllib import  error



iphonesImg = ['https://softech.kg/image/cache/8fccd9ea3afd1ccd771305f2116dde6d.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/9707e4dbf6aa0b53aa973946d3155060.jpg',
              'https://softech.kg/image/cache/73c9cecf5d8d4ebfd0dc1dd5681ceefc.png',
              'https://softech.kg/image/cache/73c9cecf5d8d4ebfd0dc1dd5681ceefc.png',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/8f58f236f6378b60d1a9fed79c6a6a88.png',
              'https://softech.kg/image/cache/8f58f236f6378b60d1a9fed79c6a6a88.png',
              'https://softech.kg/image/cache/8f58f236f6378b60d1a9fed79c6a6a88.png',
              'https://softech.kg/image/cache/8071d88579066b7e6ec5bae6d8efe80a.png',
              'https://softech.kg/image/cache/8071d88579066b7e6ec5bae6d8efe80a.png',
              'https://softech.kg/image/cache/8071d88579066b7e6ec5bae6d8efe80a.png',
              'https://softech.kg/image/cache/8071d88579066b7e6ec5bae6d8efe80a.png',
              'https://softech.kg/image/cache/8071d88579066b7e6ec5bae6d8efe80a.png',
              'https://softech.kg/image/cache/f17b5efb549b0e94dc7e3d60c02c16e6.png',
              'https://softech.kg/image/cache/f17b5efb549b0e94dc7e3d60c02c16e6.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/5ac46e26ad0432c1d09305885e82623a.png',
              'https://softech.kg/image/cache/8fccd9ea3afd1ccd771305f2116dde6d.jpg',
              'https://softech.kg/image/cache/8fccd9ea3afd1ccd771305f2116dde6d.jpg',
              'https://softech.kg/image/cache/8fccd9ea3afd1ccd771305f2116dde6d.jpg',
              'https://softech.kg/image/cache/8fccd9ea3afd1ccd771305f2116dde6d.jpg',
              'https://softech.kg/image/cache/8fccd9ea3afd1ccd771305f2116dde6d.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/1674d51ad4c75a185348103253b1b41b.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/f98d016e62af61ed8ff31937e0c89ea7.jpg',
              'https://softech.kg/image/cache/baf6db10b252981422662610baf54b15.png'
              ]
nothing_phone = ['https://softech.kg/image/cache/3fc8617feeab35a7aa71f34b34dbe392.jpg']



def getPhone(take_url):
    phones = []
    ssl._create_default_https_context = ssl._create_unverified_context
    url = take_url 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('div.caption')
    counter = 0
    for item in items:
        phone_data = []
        name = item.select_one('div.name')
        price = item.select_one('div.price')
        description = item.select_one('div.description-small')
        img = iphonesImg[counter]
        counter+=1
        link = item.select_one('a').get('href')
        phone_data.append(name.get_text())
        phone_data.append(price.get_text().strip())
        phone_data.append(description.get_text())
        phone_data.append(link)
        phone_data.append(img)
        phones.append(phone_data)
    return phones



def getDiscountItem():
    all_items = []
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://softech.kg/rasprodazha-belaja-pjatnitsa-skidki-do-40/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('div.caption')
    
    for item in items:
        item_data = []
        name = item.select_one('div.name')
        new_price = item.select_one('span.price-new')
        old_price = item.select_one('span.price-old')
        price_sale = item.select_one('span.price-sale')
        description = item.select_one('div.description-small')
        link = item.select_one('a').get('href')
        
        item_data.append(name.get_text())
        item_data.append(new_price.get_text().strip())
        item_data.append(old_price.get_text())
        item_data.append(price_sale.get_text())
        item_data.append(description.get_text())
        item_data.append(link)
        all_items.append(item_data)
    return all_items


# s = getDiscountItem()

# for i in s:
#     print (i)
   
   
   
    
    





