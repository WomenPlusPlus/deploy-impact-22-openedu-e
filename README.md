# deploy-impact-22-openedu-e

## Introduction
This directory stores all the files related to the discovery of the new relevant content. </br>
The proposition includes a program for scraping Google Search results, as well as scraping information from ResearchGate.

## Folders: 
### Google Search Results scraper for Wiki Projects: 
Defined query conditions based on advance Google Search operatos were defined to capture search of entries related to Wiki entries - may it be news, articles, various platforms and single resources which refer to using Wiki in teaching and education.  
The program uses Scrapy Framework as well the ScraperAPI which enables a free Google Search Results Pages (SERP) scraper crawling (SERPs) and extracting data from those web pages in structured formats. 
The API used allows for the scraping without getting banned and is taking care of CAPTCHAs and user agents, as well as handles the anti-bots and proxies. 

##### Parametrization
Input configuration
-query.csv: the file contains a list of google search queries using advanced operators and topics aiming to capture Wiki-related pages, as well the information about the language of the words used in the query. It can be further enriched based on the article provided in ./doc
![image](https://user-images.githubusercontent.com/37207832/202822524-07879f14-164e-4d64-b638-be8bc5b39308.png)

-api_key.txt

##### Usage
After installing packages (scrapy), simply run:
```
scrapy crawl google -o serps.csv 
```
to crawl the web pages.

##### Extracted Data
The extracted data is stored in the specified file path in a CSV format (other formats available): 
![image](https://user-images.githubusercontent.com/37207832/202822730-d170435a-6d0b-436b-a6aa-a67021937971.png)

You can see the data scraped in serp.csv. This is the result of running with the default setting and the categories specified in src/google_scraper/query.csv.

For each SERP, four fields were extracted:
- snippet: description of each search results briefly showing the content relevant to the input query
- link: the url to the full article, you can visit this url to read or crawl the full content
- title: the title of the article.
- position: number of entry scraped
- date: date of scraper's run
![Uploading image.png…]()

##### Dependencies/Limitations
- Scrapy: The official documentation page recommends installing the package using conda or miniconda.
- ScraperAPI: The API is available with a Free plan that allows to use 1,000 credits per month.


#### Research Gate scraper: 
The program uses Scrapy Framework to extract information from researchgate.net.


## External Documentation: 
- ScraperAPI: https://www.scraperapi.com/documentation/python/ 
- Refine web search with advanced operators: https://support.google.com/websearch/answer/2466433?visit_id=638043801751520505-2327133070&p=adv_operators&hl=en&rd=1
- Scrapy: https://scrapy.org/

## Recognition: 
https://www.scraperapi.com/blog/scrape-data-google-search-results/
