import json
import logging

import requests

from api.errors import handle_error, APIError
from logging_config import logger


def request(method, url, headers=None, **kwargs):
    if headers is None:
        headers = {
            "X-RapidAPI-Key": "9de39692afmsha02c5f42918bef2p16c60ajsn975baebbf045",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }
    logger.debug(f"Sending {method} request to {url}")
    response = requests.request(method, url, headers=headers, **kwargs)
    logger.debug(f"Received {response.status_code} response from {url}\nWith body: {json.dumps(response.json(), sort_keys=True, indent=4)}")
    try:
        handle_error(response)
        return response
    except APIError as e:
        print(f"An API error occurred: {e}")
