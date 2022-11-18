# Search engine/Demo app
![Alt Text](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/main/src/NLP/Content%20Search/Demo%20App/search_engine_video.gif)

We built an experimental semantic search engine for the OpenEdu platform by building and deploying a demo app using the Streamlit library on Python. The engine processes the text input provided in the search bar, queries the content currently available on the SQL database dump provided, and provides a list with 10 resources that best match (in semantic similarity terms) the search query. The app is up and running (temporarily) at this [link on the Streamlit cloud](https://slashlan-test-streamlit-openedu-search-engine-app-test-0qqrve.streamlit.app/). 

The search engine is based on passing the text input from the search bar to a pretrained semantic transformer model (SBERT) that vectorizes it and calculates the cosine similarity of the query with respect to the SQL database fields 'short_description_en' and 'more_information_en' of all the resources available on the platform. Notice that these fields contain the resource description in English language.

The `Search_engine_app_test.py` contains the experimental app described. In our test, for computational reasons, we adopted the semantic transformer model ‘paraphrase-albert-small-v2’ model. However, given the multi-language nature of a platform such as OpenEdu, we suggest the use of the multi-language model ‘paraphrase-multilingual-MiniLM-L12-v2’. In this way, the user can search through OpenEdu content by inputting queries in over 50 different languages and get meaningful results without changing anything else in the code we developed.
### Resources
- [Sentence-Transformers (SBERT)](https://www.sbert.net/index.html#)
- [Streamlit](https://streamlit.io/)
