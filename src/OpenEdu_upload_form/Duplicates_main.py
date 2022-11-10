# # DUPLICATES SUGGESTION TOOL TO PLUG INTO THE MODERATOR INTERFACE
# The script can be used to extract text from the uploading form submitted to OpenEdu,
# comparing it with the instances stored in the OpenEdu database and suggesting
# to the moderator similar content already existing on the platform to double-check
# (in order to avoid duplicates and/or aggregating the new instance in an existing one).

# Import libraries
import pandas as pd
import re
from sentence_transformers import SentenceTransformer, util


# Define cleaning function for text in description fields
def clean_text(text):
    """Cleans text from brackets/symbols and non-ASCII characters"""

    text = text.encode("ascii", "ignore")  # Remove non-ASCII characters
    text = text.decode()
    text = text.replace('\n', ' ')  # Remove new row escape
    text = re.sub(r'<[^>]+>', '',
                  text)  # Eliminate text within < > characters
    text = re.sub(r'\[[^]]+]', '',
                  text)  # Eliminate text within squared brackets
    text = re.sub(r'\([^)]+\)', '',
                  text)  # Eliminate text within parentheses
    text = text.replace('&nbsp', '')  # Remove HTML non-breaking space
    text = text.replace('&#39;', "'")  # Decode HTML code for apostrophe
    text = text.replace('&quot;', '"')  # Decode HTML code for quotation marks
    text = ' '.join(text.split())  # Reduce all double/triple white spaces to single
    return text


# Load pretrained semantic model (suggested model 'all-MiniLM-L6-v2')
def load_model(model_name):
    """Load pre-trained semantic search model."""
    model = SentenceTransformer(model_name)
    return model


# Define preprocessing function
def preprocess_text(df, model):
    """Puts together text fields for each instance, cleans them, calculates embeddings,
    and makes them ready for the semantic similarity model. Also, it creates labels for each instance."""
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

    # Encode all texts in the database
    embeddings = model.encode(sentence_list_clean)

    return sentence_list_clean, instances_series, instances_links, embeddings


# Define similarity function to propose most similar suggestions by semantic similarity
def similarity_table(new_entry, instances_series, instances_links, model, embeddings):
    """Computes text embeddings for new entry. Calculates the cosine similarity
    vector and shows the 3 most similar database entries to the new entry."""

    # Encode text new entry
    new_embed = model.encode(new_entry)

    # Compute cosine similarity between new text & database
    cos_sim = util.cos_sim(new_embed, embeddings)

    # Put cos_sim in a Dataframe with labels and links
    similarity_vector_values = pd.DataFrame(cos_sim.numpy()).squeeze(axis=0)

    # Create table with cosine similarity, entries titles and links
    similarity_df = pd.concat([similarity_vector_values, instances_series, instances_links], axis=1).rename(
        columns={0: 'similarity_vector_values'})

    # Sort by higher similarity score and show top 3
    result = similarity_df.sort_values('similarity_vector_values', ascending=False).head(3)

    return result

# to get requirements.txt run in Python Terminal pipreqs C:/Users/marco/PycharmProjects/OpenEdu_upload_form
