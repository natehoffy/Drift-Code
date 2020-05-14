import pandas as pd
import requests
from pandas.io.json import json_normalize
import time

start_time = time.time()

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


    def process_conversations(self, conversation_json):
        conversation_data = conversation_json['data']
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

a = Conversation()
df = a.df
error = False
index = 0
size = 25
counter = 0

while not error:

    url = a.constructor(index, size)
    auth = a.auth('Bearer ', 'ButjokbrDzrnxUse1rGDOPc6zHX30vFu')
    aJson = a.get_conversations(url, auth)
    aData = a.process_conversations(aJson)
    df = df.append(aData, sort = False)

    try:
        aPage = a.pagination(aJson)
        counter += 1
        print(counter)
    except KeyError:
        error = True
        aPage = False
        print(aPage)

    if aPage == True:
        index += 25

convoIdList = df['id'].to_list()
countIds = 0
for item in convoIdList:
    countIds += 1

print(countIds)
run_time = time.time() - start_time
print("--- %s minutes ---" % (run_time/60))
