from myfr24.scraper import parse_flights
from myfr24.network import fetch_html_from_fr24


class MyFR24(object):
    def __init__(self, username: str, skip_fetch_at_start=False) -> None:
        self.username = username
        self.html = None

        if not skip_fetch_at_start:
            self.fetch_flights()
            self.parse_flights()

    def fetch_flights(self):
        self.html = fetch_html_from_fr24(self.username)

    def parse_flights(self):
        self.flights = parse_flights(self.html)
