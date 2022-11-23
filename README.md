# Deploy-impact-22-openedu-e

<p align="center">
  <a href="" rel="noopener">
 <img src="https://user-images.githubusercontent.com/37207832/202691843-84df34e0-180e-40ee-b70d-5a2b37bb5ea2.png" alt="Group logo" width="800" height="200">
    <br></br>
 <img src="https://user-images.githubusercontent.com/37207832/199510757-5fde0b18-bd73-49bc-8c32-1a8827dcdf81.png" alt="Project logo" width="200" height="70">


</a>
</p>
<div align="center">

  [![OpenEdu.CH](https://img.shields.io/badge/OpenEdu-UniFire-blueviolet.svg)](http://openedu.ch) 
 [![Program](https://img.shields.io/badge/Program-Deploy(impact)-blueviolet.svg)](https://www.womenplusplus.ch/deploy-impact) 
  ![Status](https://img.shields.io/badge/Status-Developing-blueviolet.svg) 



</div>

---

<p align="center"> 
Different schools and universities would love to benefit from the advantages to have collaborative, shared educational material and prevent duplication of content. When planning an educational activity, the entities involved wish to use existing online material in order to ease the teachers life and to avoid duplication of materials. The existing material on the Internet is complex to find and very confusing. One thing that can save a lot of time is to be able to search a database with this amount of structured data (and directly contact the authors of the research/material).
<br> 
</p>

## 📝 Table of Contents
- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Limitations](#limitations)
- [Future Scope](#future_scope)
- [Prerequisites](#prerequisites)
- [Technology Stack](#tech_stack)
- [Authors](#authors)
- [Resources](#resources)

## 🧐 Problem Statement <a name = "problem_statement"></a>
In the center of attention there is OpenEdu.ch which is the open education resources (OER) platform. Its mission is enabling sharing OER for teaching and learning, collaboration between educators in creating and reusing materials.

#### IDEAL: <br> 
- The content of the website is easy to navigate and the search functionality is intuitive and provides sufficient and organized information to the users of the portal with suggestions of other related entries. <br> 
- Wikimedia Community and Educators can easily upload new content, the uploading process is faciliated with automatic tools and the uploading forms are comfortable to understand and navigate.<br> 
- The Scientific Board can approve or modify the newly uploaded content quicker based on the automatic testing functions.The new relevant content is also proposed automatically based on the parametrization given by the Moderators.<br> 
- Users can contact the other users for open collaboration. <br> 

#### REALITY: <br> 
- Unrefined filters for content navigation. <br> 
- Lack of ontology structuring the resources.<br> 
- Only manual actions are needed for content upload and moderation.<br>
- Very long and complicated upload fom<br>
- No multilingual support and the resources are described and created in multiple languages. <br> 

#### CONSEQUENCES: <br> 
- Difficulty finding relevant resources on the website and in the web. Unintuitive navigation on the website.<br> 
- Upload of new resources is manual and complicated. <br> 
- Fully manual moderation of the newly proposed content which hinders addition of bigger number of resources.<br> 
- Impeded cooperation between educators due to lack of available contact information. <br> 


## 💡 Idea / Solution <a name = "idea"></a>
The prepared solution is a knowledge management and discovery tool for OpenEdu.ch.
Our product includes elements and workflows of streamlined uploading process, as well as moderation of the new content uploaded manually or automatically as a result of discovery of new relevant resources.  
<p align="center">
<a href="" rel="noopener">
  <img src="https://user-images.githubusercontent.com/37207832/202766910-7e2b231b-e6d3-4119-9bda-7e80d299e51f.png" alt="Overview" width="660" height="380">
</a>
</p>
                   
Our value proposition is **AI Engine** encompassing the following:

- Versatile Ontology for Knowledge Management allowing easier browsing, searching and fostering collaboration between educators
- Mulitlingual Ontology Support for enabling navigating materials created and described in foreign languages 

- Moderation Board Workflow designed for more efficient approval process of the new content 
- Uploading Process simplified and facilitated by organized forms and automatic functionalities
- AI-based features facilitating the analysis of the new content and its moderation, as well as linking related materials 
    - Moderation, Upload, Search, Recommendation,..
- Semantic Search for enriched results of the content querying
- Figma Prototype with UI/UX Design
- Extending the available content by suggesting new relevant content with web scrapers.

To Enable a **structured, user-friendly, Informative, moderated, collaborative, and inclusive** Platform!

<p align="center">
<a href="" rel="noopener">
<img src="https://user-images.githubusercontent.com/37207832/202767064-dd8d1011-79fb-45ee-8a0c-ae22fde70e1c.png" alt="Overview" width="650" height="380">
</a>
</p>


## Repository Structure: 
The generic schema of folders created for documentation is as following:
- [src:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/tree/main/src)  Implementation and parametrization of the module.
- [docs:](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/tree/main/docs) Descritpive documentation of the solution and presentation [to add].

These folders are then sub-divided into different AI Engine modules, which include (depending on the presence of the relevant files):
- Data Architecture: it includes backend and frontend deliverables
- Data: it includes current database content, used datasets and data scraping  
- Ontology: includes new ontology design implemented in Protégé, patterns for future expansion of the ontology and multilingual support
- NLP: AI-based features for semantic search, recommendations. 

Moreover, please note: 
- [README.md](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/main/README.md)
- [GPL license](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/main/LICENSE).

The detailed tree for the repo, can be found [here](#repository-tree)

## ⛓️ Limitations <a name = "limitations"></a>

- Data Architecture solution: The solution does not cover a database schema, webservices setup and scalability solutions. This part has been moved out of the scope of the project due to the time constraint within the 6 week program. 


## 🚀 Future Scope <a name = "future_scope"></a>
- Data Architecture and Backend Development: 
Due to internal project scoping and main requirements of the stakeholders, the current architectural proposition consists of the UML diagram of a relation DB mapped to the newly proposed ontology and the result of the comparative research. 
The further development suggested by us, considers shifting the infrastructure to the cloud environment including a composition of microservices containing postgreSQL database and elasticsearch (a distributed search and analytics engine). 

- Ontology extensions:  Recommender-based ontology design for discovery of new topics, implementing conceptualization of how to expand the ontology by including learning paths, ratings etc, and adding user-reviewing functionalities to the platform.

- A/B Testing: Experiments for assessing multiple website alternatives by users for statistical analysis to further refine the user journey.

- NLP: Introducing the algorithmic user-based recommendation for more targeted suggestions.   

## Prerequisites
Requirements of the installed packages and versions are described in the domain-specific folders. 

## ⛏️ Built With <a name = "tech_stack"></a>
- [Azure](https://https://portal.azure.com/) | [Azure Content Moderator Cognitive Services]()
- [SparkNLP]() | [spaCy]()
- [Figma](https://nodejs.org/en/) - Prototyping tool
- [Ontology Editor:]() Protégé 5.5.0
- [Django plugin Django-parler]()
- **Note:** This repo uses Python 3.8 and various NLP-related libraries that can be installed [here](src/Installation/README.md)

## Languages
- Python 3.8
- OWL 2 Web Ontology Language
- RDF (Resource Description Framework)

## ✍️ Authors <a name = "authors"></a>

- Yasmine Mohamed, [@YasmineM311](https://github.com/YasmineM311) 
- Ibtihel Ouni, [@Ibtihel-ouni](https://github.com/Ibtihel-ouni)
- Chueh Yang, [@cyyang50](https://github.com/cyyang50)
- Anna Wojcieszek [@annopol](https://github.com/annopol) - Contact person
- Marco Pistis [@slashlan](https://github.com/slashlan)
- Sonia Vigolo, [@s-vigolo](https://github.com/s-vigolo)
- Gilda Fernandez-Concha, [@gildafc](https://github.com/gildafc)

## Resources

[Link to our presentation](https://www.canva.com/design/DAFRlSCbu-g/FiH1rJ5rDJcAVnHhRLiAuQ/view?utm_content=DAFRlSCbu-g&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

[Link to our Miro board](https://miro.com/app/board/uXjVPRFpfAs=/)

[Link to our google drive](https://drive.google.com/drive/folders/1V0O3WWoJWENF3NF9_IwsNIZRNpTPT_zl)

[Link to our Figma prototype](https://www.figma.com/file/FWPyKwfz51AA2quxe2O4Y6/OpenEdu_web?t=46qmdxeySpzwzder-0)


## Recognition 
<img src="https://user-images.githubusercontent.com/37207832/202848121-0f318918-75c2-4c62-adf3-77779f19d25b.png" width="200"  alt="deploy" ></br>
<img src="https://user-images.githubusercontent.com/37207832/202848148-1926fb0b-e859-4472-adbf-fe3e6aa094f7.png" width="600"  alt="womenplusplus">      


### Repository tree 

    ```bash

    $ tree
    .
    |-- LICENSE
    |-- README.md
    |-- docs
    |   |-- Further Technologies
    |   |-- UniFire on Fire OpenEduE.pdf
    |   |-- Visual_OpenEdu_E.png
    |   `-- Work Documentation
    |       |-- Architecture
    |       |   |-- Discover Django!.pdf
    |       |   |-- Figma.pdf
    |       |   `-- UI_UX Plan.pdf
    |       |-- Data
    |       |   `-- Databases_-_SQL_or_NoSQL.pdf
    |       |-- NLP Pipeline
    |       |   `-- Moderation
    |       |       `-- Wiki Duplicates info.pdf
    |       `-- Ontology
    |           |-- OER_suggestions - Arkusz1.pdf
    |           `-- Ontology articles and references.pdf
    |-- src
    |   |-- Architecture
    |   |   |-- Backend
    |   |   |   `-- ontology_mapping_to_RDB_database_schema_UML_diagram.png
    |   |   `-- UI Design
    |   |       |-- README.md
    |   |       `-- images
    |   |           |-- ...
    |   |           |-- 1_Main Page.png
    |   |           `-- test.MD
    |   |-- Data
    |   |   |-- Database
    |   |   |   `-- openedu_db_dump.txt
    |   |   |-- Datasets
    |   |   |   |-- Wikimedia & Education Database - Database.csv
    |   |   |   `-- openedu_metadata_schema.xlsx
    |   |   |-- Scraped Data
    |   |   |   |-- ResearchGate
    |   |   |   `-- Wiki Projects
    |   |   `-- Scraped Metadata
    |   |-- Installation
    |   |   |-- linux
    |   |   `-- windows
    |   |-- NLP
    |   |   |-- Content Analysis
    |   |   |   |-- Analysis Apps
    |   |   |   |-- Language_detection.ipynb
    |   |   |   `-- Topics Modeling
    |   |   |       |-- OpenEdu
    |   |   |       |   |-- Experiments Tracking
    |   |   |       |   `-- OpenEdu_pycaret.ipynb
    |   |   |       |-- Wikimedia
    |   |   |       |   `-- Wikimedia_pycaret.ipynb
    |   |   |       `-- Wikipedia
    |   |   |           `-- Wikipedia_pycaret.ipynb
    |   |   |-- Content Moderation
    |   |   |   |-- Duplicates Discovery
    |   |   |   |-- Euphemism Detection and Identification
    |   |   |   `-- content_moderator.py
    |   |   |-- Content Recommendation
    |   |   |   |-- Existing OpenEdu Contents
    |   |   |   |   `-- Similarity Search
    |   |   |   |       `-- openedu_recommender_by_similarity.ipynb
    |   |   |   `-- External Contents
    |   |   |-- Content Search
    |   |   |   `-- Demo App
    |   |   |-- Content Translation
    |   |   |-- Content Upload
    |   |   |   |-- AI-Autofill
    |   |   |   |   |-- AI assistant.ipynb
    |   |   |   |   |-- Data
    |   |-- Ontology
    |   |   |-- Access
    |   |   |   |-- Exploring the ontology using OWLready2.ipynb
    |   |   |-- Design
    |   |   |   |-- Multilingual Support
    |   |   |   |-- Patterns
    |   |   |   |   |-- Conceptual Map of Ontology Patterns.jpg
    |   |   |   |-- VOWL viuslization.png
    |   |   |   |-- final ontology design.excalidraw
    |   |   |   |-- final ontology designX3.png
    |   |   |   |-- openedu_metadata_schema.xlsx
    |   |   |   |-- taxonomy.png
    |   |   |   |-- test_resource4.png
    |   |   |   `-- unifire-openedu.owl
    |   |   |-- Multilingual Support
    |   |   |   `-- files
    |   |   |       |-- forms
    |   |   |       `-- settings.py
    |   `-- UniFire AI Engine.PNG
    `-- test
        |-- Ontology
        |   |-- Access
        |   `-- Evaluation

    120 directories, 396 files

    ```
