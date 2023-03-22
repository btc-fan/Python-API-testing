from assertpy import assert_that
from pytest_testrail.plugin import pytestrail

from api.client import request
from api.paths import CITIES_PATH

@pytestrail.case('C2')
def test_get_cities():
    response = request("GET", CITIES_PATH)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.headers["Content-Type"]).contains("application/json")
    assert_that(response.json()['data'][3]['population']).is_greater_than(0)

