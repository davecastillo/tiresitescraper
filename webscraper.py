from collections import OrderedDict
import requests
import lxml
from lxml import html
from proxy_servers import proxy


class WebScraper():
    """This tire site scraper is used to inherit basic scaping abilities
    for children tire site scrapers.
    """

    def __init__(self, main_url, url, size_element,
                 price_element, brand, model):
        self.main_url = main_url
        self.url = url
        self.size_element = size_element
        self.price_element = price_element
        self.brand = brand
        self.model = model
        self.size_list = list()
        self.price_list = list()
        self.tire_url_list = list()
        self.price_size_dict = dict()
        self.url_size_dict = dict()

    def make_request(self, url):
        try:
            r = requests.get(url, proxies=proxy)
        except requests.ConnectionError:
            print "\nError Connecting to the server"
        except requests.HTTPError:
            print "\nAn HTTP error occured"
        except requests.TooManyRedirects:
            print "\nToo many redirects"
        except requests.RequestException:
            print "\nThere was an ambiguous exception that"\
                   " occured while handling the request."
        else:
            return r

    def parse_size(s):
        """Helper funciton. Only called in parse_and_save_sizes.
        Tire size 's' can be no longer or shorther than 19 and
        6 characters respectively.
        """
        if len(s) > 19 or len(s) < 6:
            pass
        else:
            if s[0].isalpha():
                char = s[0]
                s = s.replace(char, ' ')
                s = s.strip()
            s = s[:10]
            s = s.strip()
            if 'ZR' in s:
                s = s.replace('ZR', '/')
            elif 'R' in s:
                s = s.replace('R', '/')
            return s

    def parse_and_save_sizes(sizes):
        """tmp_sie_list is a list of raw sizes.
        Raw sizes are needed to be checked against urls
        in order to grab individual price/size urls for each
        tire.
        """
        tmp_size_list = list()
        for size in sizes:
            s = size.text_content()
            tmp_size_list.append(s.strip())
            self.size_list.append(parse_size(s))
        return tmp_size_list

    def get_url_list(tree):
        for a in tree.cssselect('tr a'):
            if a.text in tmp_size_list:
                self.tire_url_list.append(a.get('href'))

    def parse_price(self, price):
        """This function will be overriden for every
        tire site.
        """
        return price

    def get_prices(self):
        for url in self.tire_url_list:
            r = self.make_request(url)
            tree = lxml.html.fromstring(rqst.content)
            price = tree.find_class(self.price_element)
            self.price_list.append(self.parse_price(price))

    def zip_key_values(self):
        self.price_dict = OrderedDict(zip(self.size_list, self.price_list))
        self.url_size_dict = OrderedDict(
                                zip(self.size_list, self.tire_url_list))

    def main(self):
        site_request = self.make_request(self.main_url + self.url)
        tree = lxml.html.fromstring(site_request.content)
        sizes = tree.find_class(self.size_element)
        tmp_size_list = self.parse_and_save_sizes(sizes)
        self.get_url_list(tree, tmp_size_list)
        self.get_prices()
        self.zip_key_values()

    def print_size_list(self):
        for size in self.size_list:
            print size

    def print_price_size(self):
        for s, p in self.price_size_dict.items():
            print s, p
