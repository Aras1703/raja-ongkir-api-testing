import requests

ENDPOINT = "https://api.rajaongkir.com/starter/"
headers = {"key":"6793dad83f4eb9c8e89ca33a360d163e"}

def test_ListProvince_endpoint():
    #Define province id
    id = 6

    #Check if status code is OK
    response = requests.get(ENDPOINT + f'province?id={id}', headers=headers)
    assert response.status_code == 200

def test_ListCity_endpoint():
    #Define city id and province id
    id = 151
    province = 6

    #Check if status code is OK
    response = requests.get(ENDPOINT + f'city?id={id}&province={province}', headers=headers)
    assert response.status_code == 200

def test_Cost_endpoint():
    #Create data
    payload = {
        "origin":"151",
        "destination":"154",
        "weight":1500,
        "courier":"jne"
    }

    #Check if status code is OK
    response = requests.post(ENDPOINT+'cost', json=payload, headers=headers)
    assert response.status_code == 200