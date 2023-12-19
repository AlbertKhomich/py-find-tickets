import requests


class DataManager:

    def __init__(self):

        self.endpoint_users = 'https://api.sheety.co/86957ab7d54a0f0044a0d6d7aa507faa/flightDeals/users'
        self.API_ENDPOINT_PERSONAL = "https://api.sheety.co/86957ab7d54a0f0044a0d6d7aa507faa/flightDeals/prices"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer ashdfnkuashf8y3ruihsjkfjsk"
        }

    def read_users(self) -> list:
        res = requests.get(url=self.endpoint_users)
        receivers = [email["email"] for email in res.json()['users']]
        return receivers

    def read_all(self) -> list:

        res = requests.get(url=self.API_ENDPOINT_PERSONAL)
        data = res.json()["prices"]
        data_all = [city for city in data]
        return data_all

    # read cities with no IATA
    # def read_no_iata(self) -> dict:
    #
    #     res = requests.get(url=self.API_ENDPOINT_PERSONAL)
    #     data = res.json()['prices']
    #     data_dict = {city['city']: city["id"] for city in data if len(city["iataCode"]) == 0}
    #     return data_dict

    # put IATA to Google sheet
    # def write(self, word: str, obj: int):
    #
    #     body = {
    #         "price": {
    #             "iataCode": word
    #         }
    #     }
    #
    #     res = requests.put(
    #         url=f"{self.API_ENDPOINT_PERSONAL}/{obj}",
    #         json=body,
    #         headers=self.headers
    #     )
    #
    #     print(res.json())
