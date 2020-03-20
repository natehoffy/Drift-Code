import json
import pandas as pd
from pandas.io.json import json_normalize
import requests


##### Define URLs for requests #####
convo_reports_url = 'https://driftapi.com/reports/conversations'
convo_url = 'https://driftapi.com/conversations/{}'
contacts_url = 'https://driftapi.com/contacts/{}'
##### End defining of request urls #####

##### Defining data, auth, and headers for requests #####
convo_reporting_data = json.dumps({
    "filters": [
        {
            "property": "firstCloseAt",
            "operation": "BETWEEN",
            "values": [
                "2019-12-01",
                "2020-02-29"
            ]
        }
    ],
    "metrics": [
        "meaningfulConversation"
    ]
})
auth_type = 'Bearer '
auth_token = 'DcTZCxdr2aJK6ztVmwNwIbzu2rJOhodu' #input("Please insert your bearer token: ")
auth = auth_type + auth_token
headers = {'Authorization': auth, 'Content-Type': 'application/json'}
##### End definine data, auth, and headers #####

##### First request to conversations reports endpoint to get conversationId(s) #####
r = requests.post(url = convo_reports_url, data = convo_reporting_data, headers = headers)
r.raise_for_status()
json1 = r.json()
conversationIds = json1['data']
df = json_normalize(conversationIds)
convoIdList = df['conversationId'].tolist()
##### End first request to get conversationId(s) #####
print(len(convoIdList))

##### Second request to loop over conversationId from above and get conversation model #####
df2 = pd.DataFrame()
for i in range(len(convoIdList)):
    r2 = requests.get(url = convo_url.format(convoIdList[i]), headers = headers)
    json2 = r2.json()
    try:
        conversations = json2['data']
    except KeyError:
        continue
    df_temp1 = json_normalize(conversations)
    df2 = df2.append(df_temp1, sort = False)

##### End second request to retrieve list of conversations #####

df2.to_csv(r'Josh_File.csv')

df.participants.value_counts().reset_index(name='id')