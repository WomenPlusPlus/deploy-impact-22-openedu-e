# UniFire: The OpenEdu.ch AI Engine

![UniFire AI Engine](https://user-images.githubusercontent.com/58151963/202822360-a5fa0bdd-01fe-4d4c-a583-04c9e1565977.PNG)


This section discusses the prepared product listing features and proposition for their implementation and further refinement.  
  <br> 
</p>

## 📝 Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Repo structure](#repostructure)

## 🧐 Overview <a name = "overview"></a>
The AI engine is our solution encompassing  the analytical capabilities based on the newly desiged ontology. 
It is a foundation enabling navigating the ontology, efficient search, browsing of OER, as well as makes smoother user journey through the portal and creates opportunities for employing the AI-based functionalities.

* The knowledge base that is created, codifies information and then an ontology is developed that reflects associations among different data elements. Ontology-based AI allows the system to make inferences based on content and relationships, and therefore emulates human performance. 

### AI Engine Structure:
* AI Engine is comprised of several fundamental modules which include 
    * a Machine Learning Module
    * a Natural Language Processing Module
    * a Knowledge Representation(Ontology) Module
    * a UI Interface (OpenEdu.ch Platform)
* The core of an AI Engine is implemented as an ontology which may be populated by default with a huge amount of general knowledge (e.g. the whole of Wikipedia in the form of DBPedia)

# Installation:

The code examples rely on a wide range of Python libraries from the Data Science and NLP domains. To facilitate installation, I use [Docker](https://www.docker.com/get-started) to provide containerized [conda](https://docs.conda.io/en/latest/) environments.


- The [installation](Installation/README.md) directory contains detailed instructions on setting up and using a Docker image to run the notebooks. It also contains configuration files for setting up various `conda` environments and install the packages used in the notebooks directly on your machine.


## Project Development Structure <a name="repostructure"></a>:

#### The tree structure of `src` folder: 

* [Architecture/](Architecture)
  * [Backend/](Architecture/Backend)
    * [ontology_mapping_to_RDB_database_schema_UML_diagram](Architecture/Backend/ontology_mapping_to_RDB_database_schema_UML_diagram.png)
  * [UI Design/]()
    * [images/]()
* [Data/](Data)
  * [Database/](Data/Database)
  * [Datasets/](Data/Datasets)
    * [openedu_metadata_schema.xlsx](Data/Datasets/openedu_metadata_schema.xlsx)
    * [Wikimedia & Education Database - Database.csv](.)
  * [Scraped Data/]()
    * [ResearchGate/]()
    * [Wiki Projects/]()
* [Installation/](Installation)
* [NLP/](NLP)
  * [Content Analysis/]()
    * [Analysis Apps/]()
    * [Topics Modeling/]()
    * [Language_detection.ipynb]()
  * [Content Moderation/]()
    * [Duplicates Discovery/]()
    * [content_moderator.py]()
  * [Content Recommendation/]()
    * [Existing OpenEdu Contents/]()
  * [Content Search/]()
    * [Demo App/]()
  * [Content Upload/]()
    * [AI-Autofill/]()
* [Ontology/](Ontology)
  * [Access/](Ontology/Access)
    * [Exploring the ontology using OWLready2]()
  * [Design/](Ontology/Design)
    * [Patterns/](Ontology/Design/Patterns)
    * [final ontology design.excalidraw]()
    * [final ontology design]()
    * [openedu_metadata_schema.xlsx](Ontology/Design/openedu_metadata_schema.xlsx)
    * [taxonomy](Ontology/Design/taxonomy.png)
    * [test_resource](Ontology/Design/test_resource4.png)
    * [unifire-openedu.owl](Ontology/Design/unifire-openedu.owl)
  * [Multilingual Support/](Ontology/Design/MultilingualSupport)
    * [files/]()
