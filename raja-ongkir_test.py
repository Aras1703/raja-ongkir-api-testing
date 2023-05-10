import requests
from pprint import pprint

ENDPOINT = "https://api.rajaongkir.com/starter/"
headers = {"key":"6793dad83f4eb9c8e89ca33a360d163e"}

def test_ListProvince_endpoint():
    # Define parameter (int value or None)
    id = 6

    # Check if status code is OK
    response = requests.get(ENDPOINT + f'province?id={id}', headers=headers)
    assert response.status_code == 200

    data = response.json().get('rajaongkir')
    # Check if parameter id equals to blank character
    if data['query'].get('id') == '':
        assert response.status_code == 200
    # Check if parameter id equals to province_id
    elif data['query'].get('id') == str(id):
        assert data['status'].get('code') == 200
        assert data['query'].get('id') == data['results'].get('province_id')
    else:
        assert response.status_code == 200
    # There's no bad request if we input a wrong parameter
    # Bad request only appear if we not define the API key
    # Clear!!!, do not ever touch this function SMH...

def test_ListCity_endpoint():
    #Define parameter (int value or None)
    id = ''
    province = ''

    #Check if status code is OK
    response = requests.get(ENDPOINT + f'city?id={id}&province={province}', headers=headers)
    assert response.status_code == 200

    data = response.json().get('rajaongkir')
    # Check if parameter equals to blank character
    if data['query'].get('id') == '' and data['query'].get('province') == '':
        #If blank, then assert status code
        assert response.status_code == 200

    # Check if both or id parameter is not a blank character
    elif data['query'].get('id') != '' or (data['query'].get('id') != '' and data['query'].get('province') != ''):
        # If not blank, then assert status code and equals to parameter
        assert data['status'].get('code') == 200
        assert data['query'].get('id') == str(id) or (data['query'].get('id') == str(id) and data['query'].get('province') == str(province))

    # Check if province parameter equals to province_id
    elif data['query'].get('province') == str(province):
        result = [results['province_id'] for results in data['results']]
        for res in result:
            if res == data['query'].get('id'):
                assert data['status'].get('code') == 200
                assert data['query'].get('province') == res
    else:
        assert data['status'].get('code') == 200
    # There's no bad request if we input a wrong parameter
    # Bad request only appear if we not define the API key
    # Clear!!!, do not ever touch this function SMH...

def test_Cost_endpoint():
    #Create data
    payload = {
        "origin":"151",
        "destination":"154",
        "weight":1500,
        "courier":"jne",
    }

    #Check if status code is OK
    response = requests.post(ENDPOINT+'cost', json=payload, headers=headers)
    assert response.status_code == 200

test_ListProvince_endpoint()