# UniFire: The OpenEdu.ch AI Engine

![UniFire AI Engine](https://user-images.githubusercontent.com/58151963/202822360-a5fa0bdd-01fe-4d4c-a583-04c9e1565977.PNG)


This section discusses the prepared product listing features and proposition for their implementation and further refinement.  
  <br> 
</p>

## 📝 Table of Contents
- [Overview](#overview)
- [Repo structure](#repostructure)

## 🧐 Overview <a name = "overview"></a>
The AI engine is our solution encompassing  the analytical capabilities based on the newly desiged ontology. 
It is a foundation enabling navigating the ontology, efficient search, browsing of OER, as well as makes smoother user journey through the portal and creates opportunities for employing the AI-based functionalities.

* The knowledge base that is created, codifies information and then an ontology is developed that reflects associations among different data elements. Ontology-based AI allows the system to make inferences based on content and relationships, and therefore emulates human performance. 

### AI Engine Structure:
* AI Engine is comprised of several fundamental modules which include a Machine Learning Module, a Natural Language Processing Module, and a Knowledge Representation(Ontology) Module
* The core of an AI Engine is implemented as an ontology which may be populated by default with a huge amount of general knowledge (e.g. the whole of Wikipedia in the form of DBPedia)

## Repo structure <a name="repostructure"></a>

#### The tree structure of src folder: 

* [Architecture/](.\src\Architecture)
  * [Backend/](.\src\Architecture\Backend)
    * [ontology_mapping_to_RDB_database_schema_UML_diagram.png](.\src\Architecture\Backend\ontology_mapping_to_RDB_database_schema_UML_diagram.png)
    * [README.md](.\src\Architecture\Backend\README.md)
  * [UI Design/]()
    * [images/]()
    * [README.md]()
* [Data/](.\src\Data)
  * [Database/](.\src\Data\Database)
    * [__init__.py](.\src\Data\Database\__init__.py)
  * [Datasets/](.\src\Data\Datasets)
    * [openedu_metadata_schema.xlsx](.\src\Data\Datasets\openedu_metadata_schema.xlsx)
    * [README.md](.\src\Data\Datasets\README.md)
    * [Wikimedia & Education Database - Database.csv](.)
  * [Scraped Data/]()
    * [ResearchGate/]()
    * [Wiki Projects/]()
    * [README.md]()
* [Installation/](.\src\Installation)
  * [README.md](.\src\Installation\README.md)
* [NLP/](.\src\NLP)
  * [Content Analysis/]()
    * [Analysis Apps/]()
    * [Topics Modeling/]()
    * [Language_detection.ipynb]()
  * [Content Moderation/]()
    * [Duplicates Discovery/]()
    * [content_moderator.py]()
    * [README.md]()
  * [Content Recommendation/]()
    * [Existing OpenEdu Contents/]()
  * [Content Search/]()
    * [Demo App/]()
  * [Content Upload/]()
    * [AI-Autofill/]()
  * [README.md](.\src\NLP\README.md)
* [Ontology/](.\src\Ontology)
  * [Access/](.\src\Ontology\Access)
    * [Exploring the ontology using OWLready2.ipynb]()
    * [README.md](.\src\Ontology\Access\README.md)
    * [__init__.py](.\src\Ontology\Access\__init__.py)
  * [Design/](.\src\Ontology\Design)
    * [Patterns/](.\src\Ontology\Design\Patterns)
    * [final ontology design.excalidraw]()
    * [final ontology designX3.png]()
    * [openedu_metadata_schema.xlsx](.\src\Ontology\Design\openedu_metadata_schema.xlsx)
    * [README.md](.\src\Ontology\Design\README.md)
    * [taxonomy.png](.\src\Ontology\Design\taxonomy.png)
    * [test_resource4.png](.\src\Ontology\Design\test_resource4.png)
    * [unifire-openedu.owl](.\src\Ontology\Design\unifire-openedu.owl)
  * [Multilingual Support/]()
    * [files/]()
    * [README.MD]()
  * [README.md](.\src\Ontology\README.md)
* [README.md](.\src\README.md)
