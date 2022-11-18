# deploy-impact-22-openedu-e
<p align="center">
  <a href="" rel="noopener">
 <img src="https://user-images.githubusercontent.com/37207832/202691843-84df34e0-180e-40ee-b70d-5a2b37bb5ea2.png" alt="Group logo">
 <img src="https://user-images.githubusercontent.com/37207832/199510757-5fde0b18-bd73-49bc-8c32-1a8827dcdf81.png" alt="Project logo">


</a>
</p>
<h3 align="center">OpenEdu.ch</h3>

<div align="center">

  [![OpenEdu.CH](https://img.shields.io/badge/project-OpenEdu-orange.svg)](http://openedu.ch) 
  [![Unifire](https://img.shields.io/badge/team-Unifire-orange.svg)](http://openedu.ch) 
  [![Developing](https://img.shields.io/badge/status-Dev-orange.svg)](http://openedu.ch) 

</div>

---

<p align="center"> 
This section discusses the prepared product listing features and proposition for their implementation and further refinement.  
  <br> 
</p>

## 📝 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Repo structure](#repostructure)

## 🧐 Overview <a name = "overview"></a>
The above folders documents components of our solution: 
- Data:
- Data Architecture: 
- Ontology: Meant for all documents relating to the creation of the ontology
- NLP: All documents related to AI-based features
- Ontology: 

## 💡 Features <a name = "features"></a>
- Upload
- Make process smoother
- Moderation
- Quality/policy Check
- Content Search:
- Use content - elaborate projects
- Search Engine
- Collaboration of Authors
- Class: collection
- inter-connect
- Multinlingual Support for Ontology with Django plugin: mockup of a website


## Repo structure <a name="repostructure"></a>

#### The tree structure of src folder: 


* [Architecture/](.\src\Architecture)
  * [Backend/](.\src\Architecture\Backend)
    * [datatype _xsd_to_sql_conversion.png](.\src\Architecture\Backend\datatype _xsd_to_sql_conversion.png)
    * [ontology_mapping_to_RDB_database_schema_UML_diagram.png](.\src\Architecture\Backend\ontology_mapping_to_RDB_database_schema_UML_diagram.png)
    * [overview_mapping_rules.png](.\src\Architecture\Backend\overview_mapping_rules.png)
    * [README.md](.\src\Architecture\Backend\README.md)
  * [UI Design/](.\src\Architecture\UI Design)
    * [images/](.\src\Architecture\UI Design\images)
    * [README.md](.\src\Architecture\UI Design\README.md)
* [Data/](.\src\Data)
  * [Database/](.\src\Data\Database)
    * [__init__.py](.\src\Data\Database\__init__.py)
  * [Datasets/](.\src\Data\Datasets)
    * [openedu_metadata_schema.xlsx](.\src\Data\Datasets\openedu_metadata_schema.xlsx)
    * [README.md](.\src\Data\Datasets\README.md)
    * [Wikimedia & Education Database - Database.csv](.\src\Data\Datasets\Wikimedia & Education Database - Database.csv)
  * [Scraped Data/](.\src\Data\Scraped Data)
    * [ResearchGate/](.\src\Data\Scraped Data\ResearchGate)
    * [Wiki Projects/](.\src\Data\Scraped Data\Wiki Projects)
    * [README.md](.\src\Data\Scraped Data\README.md)
* [Installation/](.\src\Installation)
  * [README.md](.\src\Installation\README.md)
* [NLP/](.\src\NLP)
  * [Content Analysis/](.\src\NLP\Content Analysis)
    * [Analysis Apps/](.\src\NLP\Content Analysis\Analysis Apps)
    * [Topics Modeling/](.\src\NLP\Content Analysis\Topics Modeling)
    * [Language_detection.ipynb](.\src\NLP\Content Analysis\Language_detection.ipynb)
  * [Content Moderation/](.\src\NLP\Content Moderation)
    * [Duplicates Discovery/](.\src\NLP\Content Moderation\Duplicates Discovery)
    * [content_moderator.py](.\src\NLP\Content Moderation\content_moderator.py)
    * [README.md](.\src\NLP\Content Moderation\README.md)
  * [Content Recommendation/](.\src\NLP\Content Recommendation)
    * [Existing OpenEdu Contents/](.\src\NLP\Content Recommendation\Existing OpenEdu Contents)
  * [Content Search/](.\src\NLP\Content Search)
    * [Demo App/](.\src\NLP\Content Search\Demo App)
  * [Content Upload/](.\src\NLP\Content Upload)
    * [AI-Autofill/](.\src\NLP\Content Upload\AI-Autofill)
  * [README.md](.\src\NLP\README.md)
* [Ontology/](.\src\Ontology)
  * [Access/](.\src\Ontology\Access)
    * [Exploring the ontology using OWLready2.ipynb](.\src\Ontology\Access\Exploring the ontology using OWLready2.ipynb)
    * [README.md](.\src\Ontology\Access\README.md)
    * [__init__.py](.\src\Ontology\Access\__init__.py)
  * [Design/](.\src\Ontology\Design)
    * [Patterns/](.\src\Ontology\Design\Patterns)
    * [final ontology design.excalidraw](.\src\Ontology\Design\final ontology design.excalidraw)
    * [final ontology designX3.png](.\src\Ontology\Design\final ontology designX3.png)
    * [openedu_metadata_schema.xlsx](.\src\Ontology\Design\openedu_metadata_schema.xlsx)
    * [README.md](.\src\Ontology\Design\README.md)
    * [taxonomy.png](.\src\Ontology\Design\taxonomy.png)
    * [test_resource4.png](.\src\Ontology\Design\test_resource4.png)
    * [unifire-openedu.owl](.\src\Ontology\Design\unifire-openedu.owl)
  * [Multilingual Support/](.\src\Ontology\Multilingual Support)
    * [files/](.\src\Ontology\Multilingual Support\files)
    * [README.MD](.\src\Ontology\Multilingual Support\README.MD)
  * [README.md](.\src\Ontology\README.md)
* [README.md](.\src\README.md)
