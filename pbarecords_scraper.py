from interface.scraper import Scraper

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
import csv
import json

class PBARecordsScraper(Scraper):
    _display = Display(visible=0, size=(800, 600))
    _browser = None

    def init_driver(self):
        self._display.start()
        self._browser = webdriver.Firefox()

    def close_driver(self):
        self._browser.quit()
        self._display.stop()

    def parse(self, URL=''):
        self._browser.get(URL)

        ret_dict = dict()
        ret_dict[self.parse_name(URL)] = self.parse_content(URL)

        return ret_dict

    def parse_name(self, URL):
        return self._browser.find_element(By.CSS_SELECTOR, 'h3.post-title').text

    def parse_content(self, URL):
        return self._browser.find_element(By.CSS_SELECTOR, 'div.post-body').text

def message(text):
    print "MESSAGE: " + text

def write_file(data):
    with open('output/raw_text/'+data.keys()[0] + '.txt', 'w') as f:
        f.write(data[data.keys()[0]])

    return data.keys()[0]

def retrieve_links(path = ''):
    ls = list()

    with open(path, 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        for row in reader:
            ls.append(row['link'])

    return ls

def main():
    c = PBARecordsScraper()
    c.init_driver()

    for link in retrieve_links(path = "./output/links_boxscore.csv"):
        f = write_file(c.parse(URL = link))
        message(f + " Done")

    c.close_driver()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--debug":
            debug()

    else:
        main()
