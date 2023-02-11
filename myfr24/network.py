import requests
from .exceptions import ResponseFromFlightRadarWasNotSuccessful


def fetch_html_from_fr24(username: str):
    response = requests.get(f"https://my.flightradar24.com/{username}/flights")

    if not response.ok:
        raise ResponseFromFlightRadarWasNotSuccessful()

    return response.content
