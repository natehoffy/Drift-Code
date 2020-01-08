import json
import pandas as pd
import requests
from pandas.io.json import json_normalize
from requests.exceptions import HTTPError
# from requests.auth import AuthBase

auth_type = 'Bearer '
auth_token = 'y4bXm8rHPgn9Xa7fuE4hDerYhZXg9zXC'
auth = auth_type + auth_token
headers = {'Authorization': auth, 'Content-Type': 'application/json'}

base_url = 'https://driftapi.com'
paginator = '/accounts?index=0&size=20'


def set_urls():
    submitting_url = base_url + paginator
    return submitting_url


def get_accounts():
    r = requests.get(url=set_urls(), headers=headers)
    r.raise_for_status()
    account_json = r.json()
    return account_json


def df_accounts():
    account_data = get_accounts()['data']['accounts']
    df_temp = json_normalize(account_data)
    return df_temp

df = df_accounts()

try:
    accounts_next = get_accounts()['data']['next']
except KeyError as ke:
    print('There are no more pages of accounts.')
    accounts_next = ''
    pass

if len(accounts_next) > 0:
    paginator = accounts_next
    df2 = df.append(process_accounts())
else:
    print('This program is finished')

for i, j in df.iterrows():
    print(j)
    print(j.accountId)
