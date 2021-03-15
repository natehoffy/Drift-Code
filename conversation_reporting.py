import json
import pandas as pd
import requests
from pandas.io.json import json_normalize
from requests.exceptions import HTTPError

conversationReportsUrl = 'https://driftapi.com/reports/conversations'

requestBody = json.dumps({
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
        "meaningfulConversation",
        "id",
        "firstCloseAt"
    ]
})

authType = 'Bearer '
authToken = 'ButjokbrDzrnxUse1rGDOPc6zHX30vFu' #input("Please insert your bearer token: ")
auth = authType + authToken

requestHeaders = {'Authorization': auth, 'Content-Type': 'application/json'}

try:
    r = requests.post(url = conversationReportsUrl, data = requestBody, headers = requestHeaders)
    r.raise_for_status()
    rJson = r.json()
    #conversationIds = rJson['data']
    metrics = rJson['data'][]
    df = json_normalize(metrics)
except HTTPError as http_error:
    print(f'HTTP error occurred: {http_error}')
except Exception as error:
    print(f'Other error occurred: {error}')
else:
    print('Success!\n')

#print(conversationIds)
print(metrics)
convoIdList = df['conversationId'].tolist()
counter = 0

for id in convoIdList:
    counter += 1

print(counter)
