import requests
import datetime


class FlightSearch:

    def __init__(self):
        self.ENDPOINT = "https://api.tequila.kiwi.com/"
        self.SEARCH = "v2/search"
        self.LOCATIONS = "locations/query"
        self.API_KEY = "Yrq0buXigFQ5_pK-ev4p232zOFe0eTm7"
        self.FROM = "DUS"

        self.header = {
            "Content-Encoding": "gzip",
            "Content-Type": "application/json",
            "apikey": self.API_KEY,
        }

    # find IATA
    def iata(self, city: str) -> str:

        params_loc = {
            "term": city
        }

        res = requests.get(
            url=f"{self.ENDPOINT}{self.LOCATIONS}",
            params=params_loc,
            headers=self.header
        )
        data = res.json()

        return data['locations'][0]['code']

    def find_plane(self, destination: str, max_stopovers=0) -> list:

        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=1)
        half_m_later = now + datetime.timedelta(weeks=24)

        params = {
            "fly_from": self.FROM,
            "fly_to": destination,
            "date_from": tomorrow.strftime('%d/%m/%Y'),
            "date_to": half_m_later.strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": max_stopovers,
            "one_for_city": 1
        }

        res = requests.get(
            url=f"{self.ENDPOINT}{self.SEARCH}",
            params=params,
            headers=self.header
        )
        if len(res.json()['data']) != 0:
            price = res.json()['data'][0]['price']
            airport_from = f"{res.json()['data'][0]['cityFrom']}-{res.json()['data'][0]['flyFrom']}"
            airport_to = f"{res.json()['data'][0]['cityTo']}-{res.json()['data'][0]['flyTo']}"
            departure = f"{res.json()['data'][0]['local_departure']}"[0:10]
            return_departure = f"{res.json()['data'][0]['route'][-1]['local_departure']}"[0:10]
            via_city = f"{res.json()['data'][0]['route'][0]['cityTo']}"
            info = [price, airport_from, airport_to, departure, return_departure]
            if max_stopovers == 2:
                info.append(via_city)
            return info
        else:
            pass
