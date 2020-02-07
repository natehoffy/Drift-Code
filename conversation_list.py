import pandas as pd
import requests
from pandas.io.json import json_normalize


class Conversation(object):
    """Conversations in Drift"""
    # Value of the set is represented by a DataFrame of conversations, self.df

    def __init__(self):
        """Create an empty dataframe"""
        self.df = pd.DataFrame()


    def auth(self, auth_type, auth_token):
        auth = auth_type + auth_token
        headers = {'Authorization': auth, 'Content-Type': 'application/json'}
        return headers


    def get_conversations(self, url, headers):
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        conversation_json = r.json()
        return conversation_json


    def process_conversations(self, account_json):
        conversation_data = conversation_json['data']['id']
        df_temp = json_normalize(conversation_data)
        return df_temp


    def pagination(self, conversation_json):
        more = conversation_json['pagination']['more']
        return more


    def total(self, conversation_json):
        total = conversation_json['data']['total']
        return total


    def constructor(self, index, size):
        base_url = 'https://driftapi.com'
        paginator = '/conversations/list?next=' + str(index) + '&size=' + str(size)
        submitting_url = base_url + paginator
        return submitting_url


df = Conversation().df
error = False
index = 0
size = 10

while not error:

    a = Conversation()
    url = a.constructor(index, size)
    auth = a.auth('Bearer ', 'insert_bearer_here')
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