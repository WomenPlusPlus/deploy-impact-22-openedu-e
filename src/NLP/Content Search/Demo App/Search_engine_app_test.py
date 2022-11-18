### STREAMLIT APP FOR OPENEDU ###
# to launch the app on ANACONDA console, activate virtual env and run: streamlit run [PATH]\Search_engine_app_test.py

## IMPORT LIBRARIES

import pandas as pd
import re
import streamlit as st
import sqlalchemy as sa
from sentence_transformers import SentenceTransformer, util
from PIL import Image

# Define semantic model to use
# model = SentenceTransformer('all-MiniLM-L6-v2')
model = SentenceTransformer('paraphrase-albert-small-v2')
# model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')


## DEFINE FUNCTIONS

# Define cleaning function for description field
@st.cache
def clean_text(text):
    """Cleans text from brackets/symbols and non-ASCII characters"""

    text = text.encode("ascii", "ignore")  # Remove non-ASCII characters
    text = text.decode()
    text = text.replace('\n', ' ')  # Remove new row escape
    text = re.sub(r'<[^>]+>', '',
                  text)  # Eliminate text within < > characters (often contaning info on subs font/color)
    text = re.sub(r'\[[^]]+\]', '',
                  text)  # Eliminate text within squared brackets (often contaning audio description for hearing-impaired individuals)
    text = re.sub(r'\([^)]+\)', '',
                  text)  # Eliminate text within parentheses (often contaning audio description for hearing-impaired individuals)
    text = text.replace('&nbsp', '')  # Remove HTML non-breaking space
    text = text.replace('&#39;', "'")  # Decode HTML code for apostrophe
    text = text.replace('&quot;', '"')  # Decode HTML code for quotation marks
    text = ' '.join(text.split())  # Reduce all double/triple whitespacing to single
    return text


# Define preprocessing function

def preprocess_text(df):
    """Puts together text fields for each instance, cleans them
    and makes them ready for semantic similarity model. Also, it creates labels for each instance."""
    # Define full body of text to analyse
    df['full_text'] = df['short_description_en'].astype(str) + df['more_information_en'].astype(str)

    # Create list of texts to feed SBERT model
    sentence_list = df['full_text'].tolist()

    # Clean text
    sentence_list_clean = [clean_text(element) for element in sentence_list]

    # Build label for each instance with title + author
    df['instance'] = df['title_en'].astype(str) + str(' by ') + df['by'].astype(str)

    # Export entries titles and links as series
    instances_series = pd.Series(df['instance'])
    instances_links = pd.Series(df['link'])

    # Calculate text embeddings for entries in the database
    embeddings = model.encode(sentence_list_clean)

    return sentence_list_clean, instances_series, instances_links, embeddings


# Define similarity function to propose most similar suggestions by semantic similarity

def similarity_table(new_entry, instances_series, instances_links, embeddings):
    """Computes text embeddings for new entry and all entries already in the database.
    Calculates the cosine similarity vector and shows the 3 most similar database entries to the new entry."""

    # Encode text new entry
    new_embed = model.encode(new_entry)

    # Compute cosine similarity between new text & database
    cos_sim = util.cos_sim(new_embed, embeddings)

    # Put cos_sim in a Dataframe with labels and links
    similarity_vector_values = pd.DataFrame(cos_sim.numpy()).squeeze(axis=0)

    # Create table with cosine similarity, entries titles and links
    similarity_df = pd.concat([similarity_vector_values, instances_series, instances_links], axis=1).rename(
        columns={0: 'similarity_vector_values'})

    # Sort by higher similarity score and show top 10
    result = similarity_df.sort_values('similarity_vector_values', ascending=False).head(10)

    return result


## DEMO APP START

image_title = Image.open('/app/test_streamlit_openedu/Wikimedia-logo.png')
st.image(image_title, width=100)
st.title('Wikimedia - OpenEdu')

# Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')

# Load OpenEdu data from SQL server (only columns that are needed)
database_link = sa.create_engine(
    'postgresql://deploy_impact:AVNS_tEdPMnvmmI0knrjJe-R@deploy-impact-cg-chrisg-demo.aivencloud.com:24947/openedu')
df = pd.read_sql_query('SELECT title_en, by, link, short_description_en, more_information_en FROM sito_project',
                       database_link)

# Preprocess data for app
sentence_list, title_list, link_list, embeddings = preprocess_text(df)

# Create ontology navigation and search bar
onto_nav, search_bar = st.tabs(["Explore", "Search"])

# ONTOLOGY NAVIGATION TAB
# Keep empty for the moment

# SEARCH TAB
# Build search bar & find button action

with search_bar:
    col4, col5 = st.columns(2)
    with col4:
        value = st.text_input('', max_chars=128, placeholder='Type..')
    with col5:
        st.write('')
        st.write('')
        search_button = st.button('Find')
    if not value and not search_button:
        print('')
    else:
        # Create similarity vector and top 3 most similar scores
        results_search = similarity_table(value, title_list, link_list, embeddings)

        # Print results
        for i in range(0, len(results_search)):
            result_box = st.container()
            result_box.image(image_asset, width=150)
            result_box.write(results_search['instance'].iloc[i])
            result_box.write(results_search['link'].iloc[i])

# Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')
