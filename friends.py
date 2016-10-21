from base import *
import requests
import json
from datetime import datetime


class GetFriends(BaseClient):
    BASE_URL = 'https://api.vk.com/method/friends.get'
    http_method = 'GET'

    def __init__(self, uid):
        self.uid = uid

    def get_params(self):
        return 'user_id=' + str(self.uid) + '&fields=bdate'

    def response_handler(self, response):
        try:
            obje = json.loads(response.text)
            friends = obje.get('response')

            ages = []

            for friend in friends:
                b_date = friend.get('bdate')

                if b_date is None or b_date.count('.') < 2:
                    continue

                b_date = datetime.strptime(b_date, "%d.%m.%Y")
                n_date = datetime.now()

                ages.append(int((n_date - b_date).days) // 365.2425)

            uniqages = list(set(ages))
            return sorted([(x, ages.count(x)) for x in uniqages], key=lambda x: x[0])
        except:
            raise Exception("У пользователя нет друзей, либо они недоступны {}".format(self.uid))

    def _get_data(self, method, http_method):
        response = requests.get(self.BASE_URL + '?' + self.get_params())
        return self.response_handler(response)