import requests
from bs4 import BeautifulSoup
import csv


def getHtml():
    url = 'https://bj.58.com/wangjing/pinpaigongyu/pn/{page}/?minprice=2000-3000'
    page = 0
    CSV_FILE = open('collection.csv', 'w', newline='')
    writer = csv.writer(CSV_FILE, dialect='excel')
    while True:
        page += 1
        response = requests.get(url.format(page=page))
        response.encoding = 'utf-8'
        html = BeautifulSoup(response.text, 'html.parser')
        house_list = html.select('.list > li')
        print('downloading page' + url.format(page=page))
        page_a_list = html.find('div', class_='page')
        if page_a_list is not None:
            page_a_list = page_a_list.select('span')
            str_page = str(page_a_list)
            if '<span>下一页</span>' in str_page:
                writeFile(house_list, writer)
            else:
                writeFile(house_list, writer)
                CSV_FILE.close()
                break
        else:
            writeFile(house_list, writer)
            CSV_FILE.close()
            break


def writeFile(house_list, writer):
    for house in house_list:
        if house is not None:
            house_title = house.find('div', class_='img').img.get('alt')
            house_info_list = house_title.split()
            house_location = house_info_list[1]
            house_url = house.select('a')[0]['href']
            writer.writerow([house_title, house_location, house_url])


if __name__ == '__main__':
    getHtml()
