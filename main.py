from uid import *
from friends import *

input_id = input('Введите id: ')
user = GetID(input_id)
user_id = user.execute()

friends_client = GetFriends(user_id)
friends = friends_client.execute()

ages = []
counts = []

for (age, count) in friends:
    print('{} {}'.format(int(age), count * '='))
    ages.append(int(age))
    counts.append(int(count))

