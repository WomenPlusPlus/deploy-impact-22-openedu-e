The Similarity check functionality is part of the quality check steps executed by the moderator as shown in the [Moderator flow chart](). This functionality uses the text description of new content submitted by the contributor, compares it with what currently stored on the OpenEdu, and shows to the moderator a list with the 3 most similar resources already available on the platform to double-check to avoid material duplication.

The `Duplicates_main.py` stores all the functions needed to execute the Similarity check functionality. In short, this script cleans and breaks text in sentences, produces word embeddings (i.e., vectors in a multidimensional space), calculates cosine similarity (scale -1 to 1, with 1 being identical text and -1 being opposite) and shows the top 3 most similar texts. The script foresees the adoption of a pre-trained semantic transformer model (SBERT models) that must be specified at the beginning before executing (we suggest using all-MiniLM-L6-v2).

Ideally, the script should be integrated in a Django upload form interface together with the other functionalities related to the Moderator board template.

The `Duplicates_test.ipynb` shows a practical test of the functionality by using the current OpenEdu content available on the SQL database dump provided.

## Resources
- [SentenceTransformers (SBERT)](https://www.sbert.net/index.html#)
