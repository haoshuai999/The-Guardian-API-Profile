#The Guardian API Profile

**Author: Shuai Hao<br>
Date: Feb. 2, 2019**

All the following write up are summarized from https://open-platform.theguardian.com/documentation/

The Guardian is a world-famous British daily newspaper with a history of 198 years. The newspaper's API contains over 2 million pieces of content, which is a valuable source for scholars, experts and journalists to study the history and recent news. The Guardian has built a [platform](https://open-platform.theguardian.com/explore/) for visitors to explore their API. 

Five endpoints are available for visitors to begin their search.

* Content
* Tags
* Sections
* Editions
* Single item

**Content** (endpoint: /search) can be used to retrieve all the content in the API, and more parameters can be set to return more specific content.

**Tags** (endpoint: /tags) can be used to retrieve all the tags at the end of every news articles.

**Sections** (endpoint: /sections) can be used to retrieve all the sections like Environment, Technology, Food and Fashion.

**Edition** (endpoint: /editions) can be used to retrieve three different editions for the United Kingdom, the United States and Australia.

**Single item** is more special because the endpoint follows the same format as the domain "theguardian.com."  

This article will focus on exploring the first three endpoints, because for **Edition** endpoint, visitors can only retrieve three URLs for The Guardian's UK/US/Australia homepage. As for the **Single item** endpoint, visitors need to get the article id (a specific path of the article), which can only be found through **Content** endpoint search. 

##1) Authorization
 
Visitors need to [apply for a key](https://open-platform.theguardian.com/access/) to access the API. Free developer key allows 12 calls per second and 5,000 keys per day. After typing in the name and email address, reasons for getting a key and click "register" button, The Guardian will send API key via email.

Developer usually create a Python file named TheGuardian_credentials.py to store the API key, because sometimes keys need to be encoded or appended. For The Guardian's API, what visitors need to do is typing their API key in the credentials file.

The Python file contains the following code:

```python
    # type in API key in the quotation marks
    api_key = "API key goes here"
```

##2) Parameter Explanation

The Guardian's API provides a large number of query parameters for visitors to perform advanced search. All the parameters used in queries are listed here:

| Parameter | Description | Accept Values | AND/OR/NOT
| --- | --- | --- | ---
| api-key | API key visitors get from email | valid key | Not allowed
| q | search terms | key word | Allowed
| format | format of the result | json/xml | Not allowed 
| section | search by section | valid sections (e.g., politics) | Allowed
| tag | search by tag | valid tags (e.g., football/liverpool) | Allowed
| ids | search by single items | valid ids (e.g., culture/2019/feb/07/samantha-bee-trump-stephen-colbert-late-night-hosts-tv) | Not allowed
| from-date | search from certain date | YYYY-MM-DD | Not allowed
| to-date | search until certain date | YYYY-MM-DD | Not allowed
| page | show the result from a particular page | integers (e.g., 13) | Not allowed
| page-size | the number of items shown on one page | integers from 1 to 50 | Not allowed
| order-by | the order of result | newest/oldest/relevance | Not allowed
| production-office | content from certain office | aus/us/uk | Not allowed
| lang | language of the article | 	ISO language codes (e.g., en) | Allowed

* If we want to search for articles with both two keywords, we can use "AND" or "&" to connect them;
* If we want to search for articles with either two keywords, we can use "OR" or "|" to connect them;
* If we want to search for articles with no certain keywords , we can use "NOT" or "-" to exclude them.

For **Content** and **Single item** endpoints, all parameters are available. For **Tags** endpoint, parameters such as *api-key, format, q, section page and page size* are valid. For **sections** and **editions** endpoints, only *api-key, format and q* parameter are valid. 

If the API returns no results, it means the website doesn't have tags or sections with that name, a too specific path is provided, or too many search conditions are applied.

More available parameters can be found on https://open-platform.theguardian.com/documentation/. 

##3) JSON File Field Explanation

JSON is a file format that are commonly used for data storage and can be viewed through web browser or notepad. [JSON viewer](https://github.com/tulios/json-viewer) is an useful extension for Chrome users to read the JSON file efficiently.

The information are stored in different field of JSON file. The explanation of some fields in JSON file are listed here:

| Field | Description 
| --- | --- 
| total | total number of articles match the search requirements
| pageSize | number of items shown on one page
| currentPage | page number
| pages | total number of pages
| id | unique article id for searching
| sectionId | unique section id for searching
| sectionName | name of the section
| webPublicationDate | article publication date
| webTitle | article title
| webUrl | url of the article

More explanations about the keys can also be found on https://open-platform.theguardian.com/documentation/.
<br>

##4) Query 1: Search for articles about Brexit or Theresa May

The Guardian's API is an efficient tool to search articles by conditions. For example, the following query retrieves all articles under the "politics" section with the keyword "Brexit" or "Theresa May" produced in The Guardian's UK office in 2018. The format of output is json, and language of it is English. Every page shows 10 articles and the first page is printed in the file.

Query: `https://content.guardianapis.com/search?/q=Brexit OR (Theresa AND May)&format=json&section=politics&from-date=2018-01-01&to-date=2018-12-31&page=1&page-size=10&order-by=newest&production-office=uk&lang=en&api-key=[fill in api key here]`

All the parameters in the query are set with the following code:

```python
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
```

Then they are combined with the base URL:

```python
	# combine url

	finalized_url = "{}search?/q={}&format={}&section={}&from-date={}&to-date={}&page={}&page-size={}&order-by={}&production-office={}&lang={}&api-key={}".format(base_url, search_keyword, data_format, section, from_date, to_date, page, page_size, order_by, production_office, lang, api_key)
```

At last, the information about articles are output to a JSON file called Guardian_data_query1.json.

```python
	# perform the request and print the query
	r = requests.get(url = finalized_url, params={})

	print(finalized_url, '\t')

	# output the responses to a file
	Guardian = json.loads(r.text)
	with open('Guardian_data_query1.json', 'w') as outfile:  
	    json.dump(Guardian, outfile, indent=4)
```

Part of the output JSON file looks like this:

```json
{
    "response": {
        "status": "ok",
        "userTier": "developer",
        "total": 3693,
        "startIndex": 1,
        "pageSize": 10,
        "currentPage": 1,
        "pages": 370,
        "orderBy": "newest",
        "results": [
            {
                "id": "politics/2018/dec/31/in-2019-the-uk-will-start-a-new-chapter-says-theresa-may",
                "type": "article",
                "sectionId": "politics",
                "sectionName": "Politics",
                "webPublicationDate": "2018-12-31T22:30:02Z",
                "webTitle": "Theresa May urges MPs to back Brexit deal in new year message",
                "webUrl": "https://www.theguardian.com/politics/2018/dec/31/in-2019-the-uk-will-start-a-new-chapter-says-theresa-may",
                "apiUrl": "https://content.guardianapis.com/politics/2018/dec/31/in-2019-the-uk-will-start-a-new-chapter-says-theresa-may",
                "isHosted": false,
                "pillarId": "pillar/news",
                "pillarName": "News"
            }
        ]
    }
}
```
<br>

##5) Query 2: Get a list of tags related to football club Liverpool

The Guardian's website has a strict data structure, and all articles are under certain section with more than 1,000 tags for visitors to search. With the following query, users can access tags containing keyword "liverpool" under the "football" section. Every page shows 10 articles and the first page is printed in the file.

Query: `https://content.guardianapis.com/tags?q=liverpool&format=json&section=football&page=1&page-size=10&api-key=[fill in api key here]`

The following code has similar structure to query 1 with fewer parameters and **Tags** endpoints are applied:

```python
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
```

The responses are printed to a JSON file called Guardian_data_query2.json. The output looks like this:

```json
{
    "response": {
        "status": "ok",
        "userTier": "developer",
        "total": 2,
        "startIndex": 1,
        "pageSize": 10,
        "currentPage": 1,
        "pages": 1,
        "results": [
            {
                "id": "football/liverpool",
                "type": "keyword",
                "sectionId": "football",
                "sectionName": "Football",
                "webTitle": "Liverpool",
                "webUrl": "https://www.theguardian.com/football/liverpool",
                "apiUrl": "https://content.guardianapis.com/football/liverpool",
                "description": "Read the latest Liverpool news, transfer rumours, match reports, fixtures and live scores from the Guardian"
            },
            {
                "id": "football/liverpool-women",
                "type": "keyword",
                "sectionId": "football",
                "sectionName": "Football",
                "webTitle": "Liverpool Women",
                "webUrl": "https://www.theguardian.com/football/liverpool-women",
                "apiUrl": "https://content.guardianapis.com/football/liverpool-women"
            }
        ]
    }
}
```
<br>

##6) Query 3: Get a list of all sections in The Guardian

Articles are divided into 75 sections in The Guardian's website, but it is difficult for visitors to remember section names. The following query generates a list of all sections.

Query: `https://content.guardianapis.com/sections?&format=json&api-key=[fill in api key here]`

The following code uses **Sections** endpoints to output the list:

```python
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
```

The responses are printed to a JSON file called Guardian_data_query3.json. Part of the output looks like this:

```json
{
    "response": {
        "status": "ok",
        "userTier": "developer",
        "total": 75,
        "results": [
            {
                "id": "about",
                "webTitle": "About",
                "webUrl": "https://www.theguardian.com/about",
                "apiUrl": "https://content.guardianapis.com/about",
                "editions": [
                    {
                        "id": "about",
                        "webTitle": "About",
                        "webUrl": "https://www.theguardian.com/about",
                        "apiUrl": "https://content.guardianapis.com/about",
                        "code": "default"
                    }
                ]
            }
        ]
    }
}
```
