import requests
import json

base_url_test = 'https://dev1-api.rescuegroups.org/v5'
url = f'{base_url_test}/public/animals/search/?sort=-animals.id&limit=5'
# base_url_prod = 'https://api.rescuegroups.org/v5'
api_key = 'VndcBy5f'


def test_get_all_animals(): 
    with open('website/sample-data.json') as f:
        response = json.load(f) 
        animal_data = response["data"]
        my_animals = []
        for animal in animal_data:
            attributes = animal["attributes"]
            ageGroup = attributes["ageGroup"] if "ageGroup" in attributes else "Unknown"
            age = attributes["ageString"] if "ageString" in attributes else ageGroup
            name = attributes["name"] if "name" in attributes else "Unknown"

            my_animals.append({"name": name, "age": age})
        return my_animals
    
    


# def test_get_pets(endpoint, params=None):
#     base_url = "https://dev1-api.rescuegroups.org/v5"
#     url = "https://test-api.rescuegroups.org/v5/public/animals/?include=breeds,colors,fosters,locations,orgs,patterns,pictures,species,videos,videourls"

#     payload={}
#     headers = {
#       'Content-Type': 'application/vnd.api+json',
#       'Authorization': ''
#     }

#     response = requests.request("GET", url, headers=headers, data=payload)

#     print(response)
#     return response

