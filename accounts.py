import json
import pandas as pd
import requests
from pandas.io.json import json_normalize
from requests.exceptions import HTTPError
# from requests.auth import AuthBase


def authorization(auth_type, auth_token):
    auth = auth_type + auth_token
    headers = {'Authorization': auth, 'Content-Type': 'application/json'}
    return headers


def get_accounts(url, authenticator):
    r = requests.get(url=url, headers=authenticator)
    r.raise_for_status()
    account_json = r.json()
    return account_json


def process_accounts(account_json):
    account_data = account_json['data']['accounts']
    df_temp = json_normalize(account_data)
    return df_temp


def pagination(account_json):
    account_next = account_json['data']['next']
    return account_next


authenticator = authorization('Bearer ', 'y4bXm8rHPgn9Xa7fuE4hDerYhZXg9zXC')
base_url = 'https://driftapi.com'
paginator = '/accounts?index=0&size=10'
submitting_url = base_url + paginator
account_table = pd.DataFrame()

while len(paginator) > 0:
    account_json = get_accounts(submitting_url, authenticator)
    account_table = account_table.append(process_accounts(account_json), sort=False)
    try:
        paginator = pagination(account_json)
    except KeyError as ke:
        print('There are no more pages of accounts.')
        paginator = ''

print(account_table)