import requests

JSON_URL = "https://raw.githubusercontent.com/stefangabos/world_countries/master/data/countries/en/world.json"


def fetch_country_codes(url=JSON_URL) -> list[tuple]:
    headers = {"Content-Type": "application/json"}
    request = requests.get(url, headers=headers)

    try:
        request.raise_for_status()
        response = request.json()

    except requests.exceptions.HTTPError() as http_err:
        response = []
        print(http_err)

    except requests.exceptions.JSONDecodeError() as json_err:
        response = []
        print(json_err)

    except Exception as err:
        response = []
        print(err)

    return [(str(c["alpha2"]).upper(), str(c["name"]).title()) for c in response]
