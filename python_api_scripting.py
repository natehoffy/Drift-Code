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
                "2010-01-01",
                "2021-01-01"
            ]
        }
    ],
    "metrics": [
        "meaningfulConversation"
    ]
})

auth_type = 'Bearer '
auth_token = 'ButjokbrDzrnxUse1rGDOPc6zHX30vFu' #input("Please insert your bearer token: ")
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

