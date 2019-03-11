import requests,pprint
from bs4 import BeautifulSoup
url='https://www.findyogi.com/laptops/hp'
dow=requests.get(url)

soup=BeautifulSoup(dow.text,'html.parser')
# print(soup)
dict_list=[]
def All_laptops():
	l_div=soup.find('div',class_='card-body')
	l_ul=l_div.find('ul',class_='product-grid')
	l_li=l_ul.find_all('li',class_='product card')
	for ditals in l_li:
		artical=ditals.find('article')
		boking_link=artical.find('a').get('href')   #1@

		tital=artical.find('a').get('title')   #2@

		All_ditals=artical.find('a',class_='block-a')
		lapi_image=All_ditals.find('div',class_='image-wrapper')
		img = lapi_image.find('img').get('src')    #3@

		Rs=All_ditals.find('div',class_='info-wrapper')
		price=Rs.find('p',class_='price')
		laptop_price=price.find('meta',itemprop="price").get('content')  #4@

		lipi_ditals=All_ditals.find('div',class_='key-features-wrapper')
		laptops_informeton=lipi_ditals.find('ul',class_='key-features')
		if laptops_informeton == None:
			continue
		else:
			laptops_ditals=laptops_informeton.text      #5

			laptops_dict={"IMAGE":'','Boking-link':'','Title':'','Rs':'','Laptop-ditals':''}
			laptops_dict['IMAGE']=img
			laptops_dict['Boking-link']=boking_link
			laptops_dict['Title']=tital
			laptops_dict['Rs']=laptop_price
			laptops_dict['Laptop-ditals']=laptops_ditals
			dict_list.append(laptops_dict)
	pprint.pprint(dict_list)
		



print (All_laptops())