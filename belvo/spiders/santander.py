import re
import scrapy
import datetime
from belvo.items import Card
from urllib.parse import urljoin

class SantanderSpider(scrapy.Spider):
    name = "santander"

    def start_requests(self):
        # Retrieve card information
        url = "https://www.santander.com.ar/banco/online/personas/tarjetas#todas"
        yield scrapy.Request(url=url, callback=self.parse_cards)

    def parse_cards(self, response):
        # Find all cards
        for c in set(response.css(".tarjeta-box")):
            name = c.css("h3").extract_first()
            if name:
                # Remove H3 tags and unnecessary spaces
                name = " ".join(name.split("<br>"))[4:-5]
            chars = c.css("ul li::text").extract()
            if chars:
                # Create a nice paragraph
                chars = ". ".join(chars)
            url = c.css("span.ver-detalle a::attr(href)").extract_first()
            if url:
                url = urljoin("https://www.santander.com.ar/", url)
            card = Card(name=name, characteristics=chars, more_info_url=url)
            yield card
