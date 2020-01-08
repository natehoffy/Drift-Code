import pandas as pd
import requests
from pandas.io.json import json_normalize


class DriftAccounts(object):
    """Accounts in Drift"""
    # Value of the set is represented by a DataFrame of accounts, self.df

    def __init__(self):
        """Create an empty dataframe"""
        self.df = pd.DataFrame()


    def auth(self, auth_type, auth_token):
        auth = auth_type + auth_token
        headers = {'Authorization': auth, 'Content-Type': 'application/json'}
        return headers


    def get_accounts(self, url, headers):
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        account_json = r.json()
        return account_json


    def process_accounts(self, account_json):
        account_data = account_json['data']['accounts']
        df_temp = json_normalize(account_data)
        return df_temp


    def pagination(self, account_json):
        next = account_json['data']['next']
        return next


    def total(self, account_json):
        total = account_json['data']['total']
        return total


    def constructor(self, index, size):
        base_url = 'https://driftapi.com'
        paginator = '/accounts?index=' + str(index) + '&size=' + str(size)
        submitting_url = base_url + paginator
        return submitting_url


df = DriftAccounts().df
error = False
index = 0
size = 10

while not error:

    a = DriftAccounts()
    url = a.constructor(index, size)
    auth = a.auth('Bearer ', 'y4bXm8rHPgn9Xa7fuE4hDerYhZXg9zXC')
    aJson = a.get_accounts(url, auth)
    aData = a.process_accounts(aJson)
    df = df.append(aData, sort = False)

    try:
        aPage = a.pagination(aJson)
    except KeyError as ke:
        error = True
        aPage = ''

    if len(aPage) > 0 :
        index += 10

desiredId = df.loc[df['domain'] == 'drift.com', 'accountId']

print(desiredId)
