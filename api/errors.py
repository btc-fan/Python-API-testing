import requests

class APIError(Exception):
    """Base class for API errors."""

class InvalidAPIKeyError(APIError):
    """Error for when an invalid API key is provided."""

class RateLimitExceededError(APIError):
    """Error for when the rate limit for the API is exceeded."""

class EndpointNotFoundError(APIError):
    """Error for when an API endpoint is not found."""

def handle_error(response):
    """Handle an API error based on the HTTP status code of the response.

    Args:
        response: The HTTP response from the API.

    Raises:
        APIError: An error corresponding to the HTTP status code of the response.
    """
    if response.status_code == 401:
        raise InvalidAPIKeyError
    elif response.status_code == 429:
        raise RateLimitExceededError
    elif response.status_code == 404:
        raise EndpointNotFoundError
    elif response.status_code >= 500:
        raise APIError
