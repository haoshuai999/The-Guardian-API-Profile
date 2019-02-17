from TheGuardian_credentials import api_key
import requests
import json

# set up base url
base_url = "https://content.guardianapis.com/"

# set up parameters
search_keyword = 'Brexit OR (Theresa AND May)'
data_format = 'json'
section = 'politics'
from_date = '2018-01-01'
to_date = '2018-12-31'
page = 1
page_size = 10
order_by = 'newest'
production_office = 'uk'
lang = 'en'

# combine url
finalized_url = "{}search?/q={}&format={}&section={}&from-date={}&to-date={}&page={}&page-size={}&order-by={}&production-office={}&lang={}&api-key={}".format(base_url, search_keyword, data_format, section, from_date, to_date, page, page_size, order_by, production_office, lang, api_key)

# perform the request and print the query
r = requests.get(url = finalized_url, params={})

print(finalized_url, '\t')

# output the responses to a file
Guardian = json.loads(r.text)
with open('Guardian_data_query1.json', 'w') as outfile:  
    json.dump(Guardian, outfile, indent=4)
