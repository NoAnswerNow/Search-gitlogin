import pytest
from wsgi import *


@pytest.fixture
def client():

    with app.test_client() as client:
        yield client


def test_main_page(client):
    """Open main page and check 'Search' word exists and status code is 200"""

    rv = client.get('/')
    assert b'Search' in rv.data
    assert '200' in rv.status

def test_correct_data_for_existing_user(client):
    """Check that we receive correct data for user that exists"""

    data = {
                "nm": "dhh",
            }
    rv = client.post('/',data=data)
    assert b'Full name: David Heinemeier Hansson' in rv.data
    assert b'asset-hosting-with-minimum-ssl' in rv.data
    assert '200' in rv.status


def test_no_data_not_existing_user(client):
    """Check that we receive correct data for non existing user"""

    data = {
                "nm": "dhh12312312seda12212112121212",
            }

    rv = client.post('/',data=data)
    assert b'Full name: no full name . Repositories: 0'  in rv.data
    assert b'Search' in rv.data
    assert '200' in rv.status

def test_no_data_for_empty_user(client):
    """Check that we receive correct data for empty user"""

    data = {
                "nm": "",
            }

    rv = client.post('/',data=data)
    assert b'Full name: no full name . Repositories: 0'  in rv.data
    assert b'Search' in rv.data
    assert '200' in rv.status

def test_no_data_for_incorrect_symbols_user(client):
    """Check that we receive correct data for incorrect symbols user"""

    data = {
                "nm": "\\\\nt\tnt\as\asda12....!!!%%&$&#&#---s-x--x-q1111",
            }

    rv = client.post('/',data=data)
    assert b'Full name: no full name . Repositories: 0'  in rv.data
    assert b'Search' in rv.data
    assert '200' in rv.status


def test_no_data_for_user_name(client):
    """Check that we receive correct data for no name user"""

    data = {
                "nm": "as",
            }

    rv = client.post('/',data=data)
    assert b'Full name: no full name . Repositories: 0'  in rv.data
    assert b'Search' in rv.data
    assert '200' in rv.status