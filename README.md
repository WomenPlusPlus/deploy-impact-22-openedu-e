# deploy-impact-22-openedu-e
# Repository for Team openedu-e for deploy(impact) 2022

## Introduction
In order to enable suggesting new relevant content to OpenEdu.ch the program for scraping of Google Search results has been prepared, as well as scraping information about the Wikimedia Projects with help of an available API. 


## Features: 
-- Google Search Results scraper: 
Scrapy and ScraperAPI for extracting google search results for defined query conditions. 
It allows to perform the scraping without getting banned and taking care of CAPTCHAs and user agents, handles the anti-bots and proxies. 
The program uses Scrapy Framework as well the ScraperAPI which enables a free Google Search Results Pages (SERP) scraper crawling (SERPs) and extracting data from those web pages in structured formats. 


## Dependencies/Limitations
- Scrapy: The official documentation page recommends installing the package using conda or miniconda.
Scrapy settings:
- ScraperAPI: 
The API is available with a Free plan that allows to use 1,000 credits per month.


External Documentation: 
- ScraperAPI: https://www.scraperapi.com/documentation/python/ 
- Refine web search with advanced operators: https://support.google.com/websearch/answer/2466433?visit_id=638043801751520505-2327133070&p=adv_operators&hl=en&rd=1
- Scrapy: 

Input configuration
-query.csv
- api_key.txt

##Usage
After installing packages (scrapy), simply run:
``
scrapy crawl google -o data/path-to-output.json 

``to crawl the web pages.

The extracted data will be stored in the specified file path in a CSV format (json format?).


##Extracted Data
You can see the data scraped in serp.csv(data/X.json). 
This is the result of running with the default setting and the categories specified in src/google_search_quer/query.csv.

For each article, four fields were extracted:
- description: the url which contains the category of the article, e.g. "https://vnexpress.net/y-kien/doi-song-p10". You should ignore the page number (p10) because as explaind below, the URL is not permanent and its content will change as vnexpress add more articles.
url: the url to the full article, you can visit this url to read or crawl the full content
title: the title of the article.
text: a short exceprt of the article.

Here are instructions:

Statistics
20 queries
333? articles
611,733 tokens (single words)
topics?
web sites? 

Customizations


Pages to crawl for each category
You can choose how many pages to crawl for each category by changing the pages parameter in the get_urls() method in the same file. The default is 30 pages. Each page contains 30 articles.
