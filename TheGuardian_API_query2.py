from TheGuardian_credentials import api_key
import requests
import json

# set up base url
base_url = "https://content.guardianapis.com/"

# set up parameters
search_keyword = 'liverpool'
data_format = 'json'
section = 'football'
page = 1
page_size = 10

# combine url
finalized_url = "{}tags?q={}&format={}&section={}&page={}&page-size={}&api-key={}".format(base_url, search_keyword, data_format, section, page, page_size, api_key)

# perform the request and print the query
r = requests.get(url = finalized_url, params={})

print(finalized_url, '\t')

# output the responses to a file
Guardian = json.loads(r.text)
with open('Guardian_data_query2.json', 'w') as outfile:  
    json.dump(Guardian, outfile, indent=4)
