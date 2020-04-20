from typing import List, Dict

import validators

from parser import Parser
from utils.request import request
from utils.url_creator import AmazonURLCreator as URLCreator

class Amazon:
    def __init__(self):
        self.parser = Parser()

    def get_product_ids(self, url: str) -> List[str]:
        if validators.url(url):
            response = request(url)

            return self.parser.parse_products_page(response)

        return None

    def get_product(self, product_id: str) -> (Dict, List):        
        response_details = request(URLCreator.create_product_url(product_id))
        product_details = self.parser.parse_product(response_details)

        response_reviews = request(URLCreator.create_product_reviews_url(product_id))
        product_reviews = self.parser.parse_reviews(response_reviews)

        return product_details, product_reviews