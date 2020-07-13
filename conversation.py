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
