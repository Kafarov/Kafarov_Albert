import json
import csv
from itertools import zip_longest
import sys


with open('Kafarov_Albert_dz_6/users.csv', 'r', encoding='utf-8') as users:
    with open('Kafarov_Albert_dz_6/hobby.csv', 'r', encoding='utf-8') as hobby:
        with open('Kafarov_Albert_dz_6/users_hobby.json', 'w+', encoding='utf-8') as users_hobby:
            if sum(1 for line in csv.reader(users)) < sum(1 for line in csv.reader(hobby)):
                sys.exit(1)
            users.seek(0)
            hobby.seek(0)
            u_h = {' '.join(i): j for i, j in zip_longest(
                csv.reader(users), csv.reader(hobby), fillvalue=None)}
            json.dump(u_h, users_hobby, ensure_ascii=False)


with open('Kafarov_Albert_dz_6/users_hobby.json', 'r', encoding='utf-8') as users_hobby:
    print(json.load(users_hobby))
