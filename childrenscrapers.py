from webscraper import WebScraper


class TirerackScraper(WebScraper):
    def parse_price(self, price):
        price = price[0].text_content()
        return price


class OnlinetiresScraper(WebScraper):
    def parse_price(self, price):
        price = price[1].text_content()
        # Only interested in the price per tire
        if price.endswith('/each'):
            price = price[:-5]
        return price


class TiresdirectScraper(WebScraper):
    def parse_price(self, price):
        price = price[0].text_content()
        price = price.strip()
        return price


if __name__ == '__main__':
    from tirerackurls import re_11 as tire
    PRICE_ELEMENT = 'itemprice'
    SIZE_ELEMENT = 'sizetabSize'
    MAIN_URL = 'http://www.tirerack.com/tires/tires.jsp?tireMake='

    ws = TirerackScraper(MAIN_URL, tire_url, SIZE_ELEMENT,
                         PRICE_ELEMENT, tire.brand, tire.model)
    ws.main()
    ws.print_price_size()

    from onlinetiresurls import re_11 as tire
    SIZE_ELEMENT = 'red_arrow_blackback'
    PRICE_ELEMENT = 'price'
    MAIN_URL = 'http://www.onlinetires.com/search/vehicle/tires/'

    ws = TirerackScraper(MAIN_URL, tire_url, SIZE_ELEMENT,
                         PRICE_ELEMENT, tire.brand, tire.model)
    ws.main()
    ws.print_price_size()

    from tiresdirecturls import re_11 as tire
    SIZE_ELEMENT = 'sytle7'
    PRICE_ELEMENT = 'w2OurPrice'
    MAIN_URL = 'http://www.tiresdirect.net'

    ws = TirerackScraper(MAIN_URL, tire_url, SIZE_ELEMENT,
                         PRICE_ELEMENT, tire.brand, tire.model)
    ws.main()
    ws.print_price_size()
