import json
import pandas as pd

f = "/Users/nhoffelmeyer/Desktop/Drift-Code/gong_data.json"
# url = "https://app.gong.io/calls/ajax/calls?company-id=3568831574419877865&pageSize=1000&offset=30&callSearch=%7B%22search%22%3A%7B%22type%22%3A%22And%22%2C%22filters%22%3A%5B%7B%22type%22%3A%22Participant%22%2C%22userIds%22%3A%5B%228948771410146644384%22%5D%7D%5D%7D%7D"

with open(f, 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)

call_titles = []
call_start_time = []
call_owner = []
call_owner_name = []
account_name = []
oppty_name = []
stage_at_call = []
stage_now = []
mrr_at_call = []
mrr_now = []
account_type = []
opportunity_type = []
participant_names = []
topics = []
main_topic = []

def gong_responses(num_calls):
    for i in range(num_calls):
        call_titles.append(obj['allCallsResponse'][i]["title"])
        call_start_time.append(obj['allCallsResponse'][i]["effectiveStartDateTime"])
        call_owner.append(obj['allCallsResponse'][i]["owner"])
        call_owner_name.append(obj['allCallsResponse'][i]["ownerName"])
        if 'customerAccounts' in obj['allCallsResponse'][i]:
            account_name.append(obj['allCallsResponse'][i]['customerAccounts'][0]["name"])
        else:
            account_name.append("N/A")
        oppty_name.append(obj['allCallsResponse'][i]["opportunityName"])
        stage_at_call.append(obj['allCallsResponse'][i]["stageAtCall"])
        stage_now.append(obj['allCallsResponse'][i]["stageNow"])
        mrr_at_call.append(obj['allCallsResponse'][i]["amountAtCall"])
        mrr_now.append(obj['allCallsResponse'][i]["amountNow"])
        account_type.append(obj['allCallsResponse'][i]["accountType"])
        opportunity_type.append(obj['allCallsResponse'][i]["opportunityType"])
        participant_names.append(obj['allCallsResponse'][i]["participantNames"])
        topics.append(obj['allCallsResponse'][i]["topics"])
        main_topic.append(obj['allCallsResponse'][i]["mainTopic"])

num_calls = int(input("Enter number of gong calls: "))

gong_responses(num_calls)

dict = {'Account_Name': account_name,
        'Account_Type': account_type,
        'Call_Owner': call_owner,
        'Call_Owner_Chk': call_owner_name,
        'Call_Title': call_titles,
        'Call_Date': call_start_time,
        'Opportunity_Name': oppty_name,
        'Opportunity_Type': opportunity_type,
        'Stage_At_Call': stage_at_call,
        'Stage_Now': stage_now,
        'MRR_At_Call': mrr_at_call,
        'MRR_Now': mrr_now,
        'Participants': participant_names,
        'Main_Topic': main_topic,
        'All_Topics_Discussed': topics}

df = pd.DataFrame(dict)

df.to_csv(r'~/Desktop/Drift-Code/gong_responses.csv', index=False)

print("Done!")
