import pytest

@pytest.fixture
def api_headers(request):
    header_type = request.param
    if header_type == "default":
        return {
            "X-RapidAPI-Key": "9de39692afmsha02c5f42918bef2p16c60ajsn975baebbf045",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }
    elif header_type == "custom":
        return {
            "X-Custom-Header": "custom-value"
        }

