from interface.scraper import Scraper

from bs4 import BeautifulSoup
import json
import csv

class PbaScraper(Scraper):


    def init_driver(self, URL=''):
        global soup

        with open(URL) as markup:
            soup = BeautifulSoup(markup.read(), 'lxml')

    def close_driver(self):
        pass

    def parse(self):
        ret_data = dict()
        name_ls = list()
        link_ls = list()

        for ul in soup.select('#BlogArchive1_ArchiveList > ul.hierarchy > li > ul > li > ul'):
            for li in ul.find_all('li'):
                name_ls.append(parse_name(li))
                link_ls.append(parse_link(li))
        ret_data['name'] = name_ls
        ret_data['link'] = link_ls
        return ret_data

def parse_name(element):
    return element.text

def parse_link(element):
    return element.find('a',href=True)['href']

def write_to_csv(data):


    with open('output/links.csv', 'w') as csvfile:
        fieldnames = ['name', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for n,l in zip(data['name'],data['link']):
            writer.writerow({'name': n, 'link': l})



if __name__ == "__main__":
    c = PbaScraper()
    c.init_driver(URL = "http://pbarecordsoddities.blogspot.com/")
    data = c.parse()
    write_to_csv(data)
