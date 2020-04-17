import requests, json

auth_type = 'Bearer '
auth_token = '95IDI0ARzuA9TdXJT4JilU3n0WPKC73g' #input("Please insert your bearer token: ")
auth = auth_type + auth_token
header = {'Authorization': auth, 'Content-Type': 'application/json'}

r = requests.get(url = 'https://driftapi.com/conversations/1893345327', headers = header)
convo_json = r.json()

contactId = convo_json['data']['contactId']

r2 = requests.get(url = 'https://driftapi.com/contacts/'+str(contactId), headers = header)

contact_json = r2.json()

print(contact_json)

if contact_json['data']['country']:
    print('success')
else:
    print('failure')

