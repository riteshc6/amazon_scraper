import os
from bs4 import BeautifulSoup
import requests, webbrowser
import csv

amazon = requests.get("https://www.amazon.in/gp/bestsellers/").text

amazon_bs = BeautifulSoup(amazon, 'lxml')
departments = amazon_bs.find(id='zg_browseRoot')

for val in departments.find_all('a'):
    cat_link = val['href']
    print(val.text)
    print(cat_link)
    print()

    file = open(os.path.join('downloads',(val.text + ".csv")),"w")
    writer = csv.writer(file)
    writer.writerow(["Product","Price", "Rating","No. of reviews", "Link"])
    amazon = requests.get(cat_link).text

    best = BeautifulSoup(amazon,'lxml')

    k = best.find_all(class_='zg-item-immersion')


    for val in k:
        #print(val)
        try:
            name = val.find( class_="p13n-sc-truncate p13n-sc-line-clamp-2").text.strip()
            print(name.strip())

            link = "https://www.amazon.in/" + val.a['href']

            print(link)

            price = val.find(class_="p13n-sc-price").text.strip()
            print(price)
            rating = val.find(class_="a-icon-alt").text
            print(rating)
            reviews = val.find(class_="a-size-small a-link-normal").text
            print(reviews)
            print()
            writer.writerow([name, price, rating, reviews, link])

        except:
            print("Error")
            print()
