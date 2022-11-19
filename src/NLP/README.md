# NLP Pipeline

## Table of Contents
- [Introduction](#Introduction)
- [Special Features](#special-features)
- [Content Analysis](#content-analysis)
- [Content Search](#search-engine)
- [Search Engine](#search-engine)
- [Content Upload](#content-upload)
- [Content Recommendation](#content-recommendation)
- [Content Moderation](#content-moderation)




# Introduction

### **NLP = NLU + NLG**
![NLP](https://user-images.githubusercontent.com/58151963/202849987-c44c44ef-9ce4-4087-9151-8709dfa603a2.PNG)

### Special Features
- ![Features](https://user-images.githubusercontent.com/58151963/202850212-e1660097-b47f-4100-9676-244c4d0d85ce.PNG)
- ![Special Features](https://user-images.githubusercontent.com/58151963/202850046-90cb46b1-c3ed-449f-bde8-c2c3d75e6223.PNG)
## Content Analysis
* Topics Prediction and Similarity Search
* Analysis Apps Demo

### **NLPiffy with UniFire**

* ![NLPiffy](https://user-images.githubusercontent.com/58151963/202764791-c38be4f0-6aa9-4fde-a480-d9a79b90c5d3.gif)

### Sentiment Analysis Emoji
* ![Sentiment_Analysis_Emoji](https://user-images.githubusercontent.com/58151963/202770421-504a3a05-b04b-471a-89c9-22be81703c79.gif)


## Content Upload
* Forms Automation and Filters Discovery
    * AI assistant that automates form filling and discovers deep filters based on Named Entity Recognition.
## Content Search 

### Search Engine

* Demo app

    ![Alt Text](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/main/src/NLP/Content%20Search/Demo%20App/search_engine_video.gif)

    [This folder](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/tree/main/src/NLP/Content%20Search/Demo%20App) stores all the files related to the search engine. We built an experimental semantic search engine for the OpenEdu platform by building and deploying a demo app on Python using the Streamlit library. The engine processes the text input provided in the search bar, queries the content currently available on the SQL database dump provided, and provides a list with 10 resources that best match (in semantic similarity terms) the search query. The app is up and running (temporarily) at this [link on the Streamlit cloud](https://slashlan-test-streamlit-openedu-search-engine-app-test-0qqrve.streamlit.app/). 

## Topics prediction and Similarity Search
*  We runned Experiments fot topics detection, and modelling with Pycaret dor OpenEdu Content, Wikimedia, and Wiki-projects.
* **AutoML:**
    * We managed to automate the hyperparameters Tuning and model selection thanks to [Pycaret]() 
* **ML Interpretability:**
    * We used [Shapash]() and [Shap]()
* We Tracked the experiments with [MLFlow]()

## Recommendation
* Related Existing and External Content Suggestions based on Similarity Search.

## Upload
### Forms Automation and Filters Discovery
* AI assistant that automates form filling and discovers deep filters based on Named Entity Recognition.
* To create positive user experience, We used AI to detect custom named entities and classify according to our needs.


## Content Moderation
[This folder](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/tree/main/src/NLP/Content%20Moderation) groups all the NLP functionalities we developed for the moderation system of the OpenEdu platform such as License Checker, Link Checker, Content moderation and Similarity check.


## Ontology Learning Experiments
[This folder](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/tree/main/src/NLP/Content%20Analysis) uses topics discovery and analysis apps.
It groups all the NLP Experiments we did within the ontology Learning, Evaluation, and Extension Suggestions based on Multi-topics (labels) Text clustering (classification).