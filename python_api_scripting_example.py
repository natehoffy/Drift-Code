import json
import pandas as pd
import requests
from pandas.io.json import json_normalize
from requests.exceptions import HTTPError
#from requests.auth import AuthBase

##### Define URLs for requests #####
convo_reports_url = 'https://driftapi.com/reports/conversations'
convo_url = 'https://driftapi.com/conversations/{}'
contacts_url = 'https://driftapi.com/contacts/{}'
messages_url = 'https://driftapi.com/conversations/{}/messages'
##### End defining of request urls #####

##### Defining data, auth, and headers for requests #####
convo_reporting_data = json.dumps({
    "filters": [
        {
            "property": "firstCloseAt",
            "operation": "BETWEEN",
            "values": [
                "2019-07-16",
                "2019-07-22"
            ]
        }
    ],
    "metrics": [
        "botStatus": BOT_ONLY
    ]
})

auth_type = 'Bearer '
auth_token = 'insert_bearer' #input("Please insert your bearer token: ")
auth = auth_type + auth_token

headers = {'Authorization': auth, 'Content-Type': 'application/json'}
##### End definine data, auth, and headers #####

##### First request to conversations reports endpoint to get conversationId(s) #####
try:
    r = requests.post(url = convo_reports_url, data = convo_reporting_data, headers = headers)
    r.raise_for_status()
    json1 = r.json()
    conversationIds = json1['data']
    df = json_normalize(conversationIds)
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as error:
    print(f'Other error occurred: {error}')
else:
    print('Success! Continuing to next request. \n')

convoIdList = df['conversationId'].tolist()
##### End first request to get conversationId(s) #####

##### Second request to loop over conversationId from above and get conversation model #####
df2 = pd.DataFrame()
for i in range(len(convoIdList)):
    r2 = requests.get(url = convo_url.format(convoIdList[i]), headers = headers)
    json2 = r2.json()
    conversations = json2['data']
    df_temp1 = json_normalize(conversations)
    df2 = df2.append(df_temp1, sort = False)

contactList = df2['contactId'].tolist()
print('Success 2! Continuing to next request.')
##### End second request to retrieve list of conversations #####
print(df2)
##### Third request to retrieve contacts from conversations #####
df3 = pd.DataFrame()
for i in range(len(contactList)):
    r3 = requests.get(url = contacts_url.format(contactList[i]), headers = headers)
    json3 = r3.json()
    contacts = json3['data']
    df_temp2 = json_normalize(contacts)
    df3 = df3.append(df_temp2, sort = False)

print('Success 3! Continuing to next request.')
##### End third request to get contacts from conversations #####
print(df3)
##### Get conversation messages from a conversation #####
df4 = pd.DataFrame()
for i in range(len(convoIdList)):
    r4 = requests.get(url = messages_url.format(convoIdList[i]), headers = headers)
    json4 = r4.json()
    messages = json4['data']['messages']
    df_temp3 = json_normalize(messages)
    df4 = df4.append(df_temp3, sort = False)

print(df4)
