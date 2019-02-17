from TheGuardian_credentials import api_key
import requests
import json

# set up base url
base_url = "https://content.guardianapis.com/"

# set up parameters
data_format = 'json'

# combine url
finalized_url = "{}sections?&format={}&api-key={}".format(base_url, data_format, api_key)

# perform the request and print the query
r = requests.get(url = finalized_url, params={})

print(finalized_url, '\t')

# output the responses to a file
Guardian = json.loads(r.text)
with open('Guardian_data_query3.json', 'w') as outfile:  
    json.dump(Guardian, outfile, indent=4)
