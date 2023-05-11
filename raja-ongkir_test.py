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
        assert response.status_code == data['status'].get('code')
    # Check if parameter id equals to province_id
    elif data['query'].get('id') == str(id):
        assert data['status'].get('code') == data['status'].get('code')
        assert data['query'].get('id') == data['results'].get('province_id')
    else:
        assert response.status_code == data['status'].get('code')
    # There's no bad request if we input a wrong parameter
    # Bad request only appear if we not define the API key
    # Clear!!!, do not ever touch this function SMH...

def test_ListCity_endpoint():
    #Define parameter (int value or None)
    id = 151
    province = 6

    #Check if status code is OK
    response = requests.get(ENDPOINT + f'city?id={id}&province={province}', headers=headers)
    assert response.status_code == 200

    data = response.json().get('rajaongkir')
    # Check if parameter equals to blank character
    if data['query'].get('id') == '' and data['query'].get('province') == '':
        assert response.status_code == data['status'].get('code')

    # Check if both or id parameter is not a blank character
    elif data['query'].get('id') != '' or (data['query'].get('id') != '' and data['query'].get('province') != ''):
        assert data['status'].get('code') == data['status'].get('code')
        assert data['query'].get('id') == str(id) or (data['query'].get('id') == str(id) and data['query'].get('province') == str(province))

    # Check if province parameter equals to province_id
    elif data['query'].get('province') == str(province):
        result = [results['province_id'] for results in data['results']]
        for res in result:
            if res == data['query'].get('id'):
                assert data['status'].get('code') == data['status'].get('code')
                assert data['query'].get('province') == res
    else:
        assert data['status'].get('code') == data['status'].get('code')
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
    response = requests.post(ENDPOINT+'cost', json=payload, headers=headers)

    data = response.json().get('rajaongkir')
    # Check if payload equals to blank character
    if payload['origin'] == '' or payload['destination'] == '' or payload['weight'] == 0 or payload['weight'] == '' or payload['courier'] == '':
        # If blank, then status code is bad request
        assert response.status_code == data['status'].get('code')
    # Check if payload equals to data query response
    else:
        payloads = [body for body in payload.values()]
        queries = [query for query in data['query'].values()]
        if payloads == queries:
            assert response.status_code == data['status'].get('code')
            assert str(data['query'].get('origin')) == data['origin_details'].get('city_id')
            assert str(data['query'].get('destination')) == data['destination_details'].get('city_id')
    # Bad request will appear if api key and payload not inputted
    # Clear!!!, do not ever touch this function SMH...