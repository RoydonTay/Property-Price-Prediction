# URA Token Retrieval API Call 
# Key valid for a year, Token generated lasts for 24 hours each time.
import requests
import json

# Connect to API
user_agent = 'PostmanRuntime/7.28.4'
access_key = '<input key>'
headers = {'AccessKey': access_key,'User-Agent': user_agent}
response = requests.get('https://www.ura.gov.sg/uraDataService/insertNewToken.action', headers=headers)
token_dict = response.json()
print(token_dict)

# Fetching data
headers = {'AccessKey':access_key,'Token': token_dict['Result'],'User-Agent': user_agent}
response_batch1 = requests.get('https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Transaction&batch=1', headers=headers)
response_batch2 = requests.get('https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Transaction&batch=2', headers=headers)
response_batch3 = requests.get('https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Transaction&batch=3', headers=headers)
response_batch4 = requests.get('https://www.ura.gov.sg/uraDataService/invokeUraDS?service=PMI_Resi_Transaction&batch=4', headers=headers)

data_dict_1 = response_batch1.json()
data_dict_2 = response_batch2.json()
data_dict_3 = response_batch3.json()
data_dict_4 = response_batch4.json()

# Changing the name of the dictionary keys to join without overlap
data_dict_1['result1'] = data_dict_1.pop('Result')
data_dict_2['result2'] = data_dict_2.pop('Result')
data_dict_3['result3'] = data_dict_3.pop('Result')
data_dict_4['result4'] = data_dict_4.pop('Result')

# Consolidating all 4 batches into a single dataset
data_collated = {**data_dict_1, **data_dict_2, **data_dict_3, **data_dict_4}

# Creating json with indents
json_data = json.dumps(data_collated, indent = 4) 

# Write json into a file
json_file = open("Collated_Data_170622", "w")
json_file.write(json_data)
json_file.close()
print("File Created")

