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
  [![Status](https://img.shields.io/badge/Status-Developing-blueviolet.svg)](https://github.com/WomenPlusPlus/deploy-impact-21-kona-b/projects/5) 



</div>

---

<p align="center"> 
Different schools and universities would love to benefit from the advantages to have collaborative, shared educational material and prevent duplication of content. When planning an educational activity, the entities involved wish to use existing online material in order to ease the teachers life and to avoid duplication of materials. The existing material on the Internet is complex to find and very confusing. One thing that can save a lot of time is to be able to search a database with this amount of structured data (and directly contact the authors of the research/material).
<br> 
</p>

## 📝 Table of Contents
- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Dependencies / Limitations](#limitations)
- [Future Scope](#future_scope)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Authors](#authors)

## 🧐 Problem Statement <a name = "problem_statement"></a>
In the center of attention there is OpenEdu.ch which is the open education resources (OER) platform. Its mission is enabling sharing OER for teaching and learning, collaboration between educators in creating and reusing materials.

#### IDEAL: <br> 
-The content of the website is easy to navigate and the search functionality is intuitive and provides sufficient and organized information to the users of the portal with suggestions of other related entries. <br> 
-Wikimedia Community and Educators can easily upload new content, the uploading process is faciliated with automatic tools and the uploading forms are comfortable to understand and navigate.<br> 
-The Scientific Board can approve or modify the newly uploaded content quicker based on the automatic testing functions.The new relevant content is also proposed automatically based on the parametrization given by the Moderators.<br> 
-Users can contact the other users for open collaboration. <br> 

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
-locked cooperation between educators due to lack of available contact information. <br> 


## 💡 Idea / Solution <a name = "idea"></a>
The prepared solution is a knowledge management and discovery tool for OpenEdu.ch.
Our product includes elements and workflows of streamlined uploading process, as well as moderation of the new content uploaded manually or automatically as a result of discovery of new relevant resources.  
<p align="center">
<a href="" rel="noopener">
  <img src="https://user-images.githubusercontent.com/37207832/202766910-7e2b231b-e6d3-4119-9bda-7e80d299e51f.png" alt="Overview" width="660" height="380">
</a>
</p>
                   
Our value proposition - **AI Engine** - :

- Versatile Ontology for Knowledge Management allowing easier browsing, searching and fostering collaboration between educators
- Mulitlingual Ontology Support for enabling navigating materials created and described in foreign languages 

- Moderation Board Workflow designed for more efficient approval process of the new content 
- Uploading Process simplified and facilitated by organized forms and automatic functionalities
- AI-based features facilitating the analysis of the new content and its moderation, as well as linking related materials 
    - Moderation, Upload, Search, Recommendation,..
- Semantic Search and Suggesting new Relevant Content for addition to the OpenEdu 
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
- [src:]()  Implementation and parametrization of the module.
- [docs:]() Descritpive documentation of the solution and presentation [to add].
- [test:]() Code and Experiments Testing.  

These three folders are then sub-divided into different AI Engine modules, which include (depending on the presence of the relevant files):
- [Data Architecture:]() it includes backend and frontend deliverables
- [Data:]() it includes current database content, used datasets and data scraping  
- [Ontology:]() includes new ontology design implemented in Protégé, patterns for future expansion of the ontology and multilingual support
- [NLP:]() AI-based features for semantic search, recommendations. 

Moreover, please note: 
- [README.md]()
- [licence:]() GPL license.
The detailed tree, can be found [here](#repository-tree)

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>
- What are the dependencies of your project?
- Describe each limitation in detailed but concise terms
- Explain why each limitation exists
- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.
- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if 
appropriate, describe how these limitations could point to the need for further research.

Limitation of the created product:
- Enhance current MVP into a finite product
- Data Architecture solution: The solution does not cover a database schema, webservices setup and scalability solutions. This part has been moved out of the scope of the project due to the time constraint within the 6 week program. 


## 🚀 Future Scope <a name = "future_scope"></a>
- Data Architecture and Backend Development: 
Due to internal project scoping and main requirements of the stakeholders, the current architectural proposition consists of the UML diagram of a relation DB mapped to the newly proposed ontology and the result of the comparative research. 
The further development suggested by us, considers shifting the infrastructure to the cloud environment including a composition of microservices containing postgreSQL database and elasticsearch (a distributed search and analytics engine). 

- Ontology extensions:  For a recommender-based ontology design, we propose future possibilities for expanding the ontology by implementing learning paths and user-reviewing functionalities to the platform.
- A/B Testing: 
- NLP: For refinement of the user browsing for the resources, the algorithmic recommendation tuned to a specific user can be built.   

### Prerequisites
Requirements of the installed packages and versions are described in the domain-specific folders. 

## 🎈 Usage <a name="usage"></a>
Add notes about how to use the system.

## ⛏️ Built With <a name = "tech_stack"></a>
- [Azure](https://https://portal.azure.com/) | [Azure Content Moderator Cognitive Services]()
- [SparkNLP]() | [spaCy]()
- [Figma](https://nodejs.org/en/) - Prototyping tool
- [Ontology Editor:]() Protégé 5.5.0
- [Django plugin Django-parler]()

## Languages
- Python 3.8
- OWL 2 Web Ontology Language
- RDF (Resource Description Framework)

## ✍️ Authors <a name = "authors"></a>

- Yasmine Mohamed, [@YasmineM311](https://github.com/YasmineM311)
- Ibtihel Ouni, [@Ibtihel-ouni](https://github.com/Ibtihel-ouni)
- Chueh Yang, [@cyyang50](https://github.com/cyyang50)
- Anna Wojcieszek [@annopol](https://github.com/annopol)
- Marco Pistis [@slashlan](https://github.com/slashlan)
- Sonia Vigolo, [@s-vigolo](https://github.com/s-vigolo)
- Gilda Fernandez-Concha, [@gildafc](https://github.com/gildafc)

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
    |   |-- Future Outlooks
    |   |   `-- README.md
    |   |-- README.md
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
    |       |-- Ontology
    |       |   |-- OER_suggestions - Arkusz1.pdf
    |       |   `-- Ontology articles and references.pdf
    |       `-- README.md
    |-- src
    |   |-- Architecture
    |   |   |-- Backend
    |   |   |   |-- README.md
    |   |   |   |-- datatype _xsd_to_sql_conversion.png
    |   |   |   |-- ontology_mapping_to_RDB_database_schema_UML_diagram.png
    |   |   |   `-- overview_mapping_rules.png
    |   |   `-- UI Design
    |   |       |-- README.md
    |   |       `-- images
    |   |           |-- 10_Login Page.png
    |   |           |-- 11_Full search and results.png
    |   |           |-- 120_Upload Form - Content Type.png
    |   |           |-- 120_Upload Form - Policy.png
    |   |           |-- 121_Successful upload.png
    |   |           |-- 121_Uplod Form - Projects 1.png
    |   |           |-- 121_Uplod Form - Projects.png
    |   |           |-- 122_Upload Form - Events & Contests.png
    |   |           |-- 130_Moderation System - main.png
    |   |           |-- 131_Moderation System - New  Suggested Content.png
    |   |           |-- 132_Moderation System - Upload Resource Moderation.png
    |   |           |-- 1_Main Page.png
    |   |           `-- test.MD
    |   |-- Data
    |   |   |-- Database
    |   |   |   `-- __init__.py
    |   |   |-- Datasets
    |   |   |   |-- README.md
    |   |   |   |-- Wikimedia & Education Database - Database.csv
    |   |   |   `-- openedu_metadata_schema.xlsx
    |   |   |-- Scraped Data
    |   |   |   |-- README.md
    |   |   |   |-- ResearchGate
    |   |   |   |   |-- README.md
    |   |   |   |   |-- path.py
    |   |   |   |   |-- spider.py
    |   |   |   |   `-- util
    |   |   |   |       `-- helper.py
    |   |   |   `-- Wiki Projects
    |   |   |       |-- README.md
    |   |   |       `-- serps.csv
    |   |   `-- Scraped Metadata
    |   |-- Installation
    |   |   |-- README.md
    |   |   |-- linux
    |   |   `-- windows
    |   |-- NLP
    |   |   |-- Content Analysis
    |   |   |   |-- Analysis Apps
    |   |   |   |   |-- GIFs
    |   |   |   |   |   |-- NLPiffy.gif
    |   |   |   |   |   `-- Sentiment_Analysis_Emoji.gif
    |   |   |   |   |-- NLPiffy.py
    |   |   |   |   |-- README.md
    |   |   |   |   `-- Sentiment Analysis Emoji App.py
    |   |   |   |-- Language_detection.ipynb
    |   |   |   `-- Topics Modeling
    |   |   |       |-- OpenEdu
    |   |   |       |   |-- Experiments Tracking
    |   |   |       |   |   |-- logs.log
    |   |   |       |   |   `-- mlruns
    |   |   |       |   |       |-- 0
    |   |   |       |   |       |   `-- meta.yaml
    |   |   |       |   |       `-- 1
    |   |   |       |   |           |-- 0ba9cc4fccdd4ecebca7d8055be4803a
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   |-- Bigram.html
    |   |   |       |   |           |   |   |-- POS.html
    |   |   |       |   |           |   |   |-- Trigram.html
    |   |   |       |   |           |   |   |-- Word Frequency.html
    |   |   |       |   |           |   |   `-- id2word
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- Custom Stopwords
    |   |   |       |   |           |   |   |-- Documents
    |   |   |       |   |           |   |   |-- Vocab Size
    |   |   |       |   |           |   |   `-- session_id
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           |-- 3c062aa3da4b468982c24188d0e12db5
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   |-- model
    |   |   |       |   |           |   |   |-- model.expElogbeta.npy
    |   |   |       |   |           |   |   |-- model.id2word
    |   |   |       |   |           |   |   `-- model.state
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- alpha
    |   |   |       |   |           |   |   |-- callbacks
    |   |   |       |   |           |   |   |-- chunksize
    |   |   |       |   |           |   |   |-- decay
    |   |   |       |   |           |   |   |-- dispatcher
    |   |   |       |   |           |   |   |-- distributed
    |   |   |       |   |           |   |   |-- dtype
    |   |   |       |   |           |   |   |-- eval_every
    |   |   |       |   |           |   |   |-- gamma_threshold
    |   |   |       |   |           |   |   |-- idword
    |   |   |       |   |           |   |   |-- iterations
    |   |   |       |   |           |   |   |-- minimum_phi_value
    |   |   |       |   |           |   |   |-- minimum_probability
    |   |   |       |   |           |   |   |-- num_terms
    |   |   |       |   |           |   |   |-- num_topics
    |   |   |       |   |           |   |   |-- num_updates
    |   |   |       |   |           |   |   |-- numworkers
    |   |   |       |   |           |   |   |-- offset
    |   |   |       |   |           |   |   |-- optimize_alpha
    |   |   |       |   |           |   |   |-- optimize_eta
    |   |   |       |   |           |   |   |-- passes
    |   |   |       |   |           |   |   |-- per_word_topics
    |   |   |       |   |           |   |   |-- random_state
    |   |   |       |   |           |   |   |-- state
    |   |   |       |   |           |   |   `-- update_every
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.parentRunId
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           |-- 555b9a7c1da947b5bf514a5a89fac297
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   |-- Bigram.html
    |   |   |       |   |           |   |   |-- POS.html
    |   |   |       |   |           |   |   |-- Trigram.html
    |   |   |       |   |           |   |   |-- Word Frequency.html
    |   |   |       |   |           |   |   `-- id2word
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- Custom Stopwords
    |   |   |       |   |           |   |   |-- Documents
    |   |   |       |   |           |   |   |-- Vocab Size
    |   |   |       |   |           |   |   `-- session_id
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           |-- 63eeffcbbd574c4c9318d958106f9c8f
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   |-- model
    |   |   |       |   |           |   |   |-- model.expElogbeta.npy
    |   |   |       |   |           |   |   |-- model.id2word
    |   |   |       |   |           |   |   `-- model.state
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- alpha
    |   |   |       |   |           |   |   |-- callbacks
    |   |   |       |   |           |   |   |-- chunksize
    |   |   |       |   |           |   |   |-- decay
    |   |   |       |   |           |   |   |-- dispatcher
    |   |   |       |   |           |   |   |-- distributed
    |   |   |       |   |           |   |   |-- dtype
    |   |   |       |   |           |   |   |-- eval_every
    |   |   |       |   |           |   |   |-- gamma_threshold
    |   |   |       |   |           |   |   |-- idword
    |   |   |       |   |           |   |   |-- iterations
    |   |   |       |   |           |   |   |-- minimum_phi_value
    |   |   |       |   |           |   |   |-- minimum_probability
    |   |   |       |   |           |   |   |-- num_terms
    |   |   |       |   |           |   |   |-- num_topics
    |   |   |       |   |           |   |   |-- num_updates
    |   |   |       |   |           |   |   |-- numworkers
    |   |   |       |   |           |   |   |-- offset
    |   |   |       |   |           |   |   |-- optimize_alpha
    |   |   |       |   |           |   |   |-- optimize_eta
    |   |   |       |   |           |   |   |-- passes
    |   |   |       |   |           |   |   |-- per_word_topics
    |   |   |       |   |           |   |   |-- random_state
    |   |   |       |   |           |   |   |-- state
    |   |   |       |   |           |   |   `-- update_every
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.parentRunId
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           |-- 73ddd7992e6c46c2b11cccd6312ab294
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   |-- Bigram.html
    |   |   |       |   |           |   |   |-- POS.html
    |   |   |       |   |           |   |   |-- Trigram.html
    |   |   |       |   |           |   |   |-- Word Frequency.html
    |   |   |       |   |           |   |   `-- id2word
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- Custom Stopwords
    |   |   |       |   |           |   |   |-- Documents
    |   |   |       |   |           |   |   |-- Vocab Size
    |   |   |       |   |           |   |   `-- session_id
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           |-- a93f452a896641439b49ac346d33b404
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   |-- model
    |   |   |       |   |           |   |   |-- model.expElogbeta.npy
    |   |   |       |   |           |   |   |-- model.id2word
    |   |   |       |   |           |   |   `-- model.state
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- alpha
    |   |   |       |   |           |   |   |-- callbacks
    |   |   |       |   |           |   |   |-- chunksize
    |   |   |       |   |           |   |   |-- decay
    |   |   |       |   |           |   |   |-- dispatcher
    |   |   |       |   |           |   |   |-- distributed
    |   |   |       |   |           |   |   |-- dtype
    |   |   |       |   |           |   |   |-- eval_every
    |   |   |       |   |           |   |   |-- gamma_threshold
    |   |   |       |   |           |   |   |-- idword
    |   |   |       |   |           |   |   |-- iterations
    |   |   |       |   |           |   |   |-- minimum_phi_value
    |   |   |       |   |           |   |   |-- minimum_probability
    |   |   |       |   |           |   |   |-- num_terms
    |   |   |       |   |           |   |   |-- num_topics
    |   |   |       |   |           |   |   |-- num_updates
    |   |   |       |   |           |   |   |-- numworkers
    |   |   |       |   |           |   |   |-- offset
    |   |   |       |   |           |   |   |-- optimize_alpha
    |   |   |       |   |           |   |   |-- optimize_eta
    |   |   |       |   |           |   |   |-- passes
    |   |   |       |   |           |   |   |-- per_word_topics
    |   |   |       |   |           |   |   |-- random_state
    |   |   |       |   |           |   |   |-- state
    |   |   |       |   |           |   |   `-- update_every
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.parentRunId
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           |-- b18160b6082f4812bc805079621f0bdd
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   `-- model.pkl
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- alpha
    |   |   |       |   |           |   |   |-- alpha_H
    |   |   |       |   |           |   |   |-- alpha_W
    |   |   |       |   |           |   |   |-- beta_loss
    |   |   |       |   |           |   |   |-- init
    |   |   |       |   |           |   |   |-- l_ratio
    |   |   |       |   |           |   |   |-- max_iter
    |   |   |       |   |           |   |   |-- n_components
    |   |   |       |   |           |   |   |-- random_state
    |   |   |       |   |           |   |   |-- regularization
    |   |   |       |   |           |   |   |-- shuffle
    |   |   |       |   |           |   |   |-- solver
    |   |   |       |   |           |   |   |-- tol
    |   |   |       |   |           |   |   `-- verbose
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.parentRunId
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           |-- e1a71b2ec5bb4d0695eed0c9cbba1795
    |   |   |       |   |           |   |-- artifacts
    |   |   |       |   |           |   |   |-- Bigram.html
    |   |   |       |   |           |   |   |-- POS.html
    |   |   |       |   |           |   |   |-- Trigram.html
    |   |   |       |   |           |   |   |-- Word Frequency.html
    |   |   |       |   |           |   |   `-- id2word
    |   |   |       |   |           |   |-- meta.yaml
    |   |   |       |   |           |   |-- metrics
    |   |   |       |   |           |   |-- params
    |   |   |       |   |           |   |   |-- Custom Stopwords
    |   |   |       |   |           |   |   |-- Documents
    |   |   |       |   |           |   |   |-- Vocab Size
    |   |   |       |   |           |   |   `-- session_id
    |   |   |       |   |           |   `-- tags
    |   |   |       |   |           |       |-- Run ID
    |   |   |       |   |           |       |-- Run Time
    |   |   |       |   |           |       |-- Source
    |   |   |       |   |           |       |-- URI
    |   |   |       |   |           |       |-- USI
    |   |   |       |   |           |       |-- mlflow.parentRunId
    |   |   |       |   |           |       |-- mlflow.runName
    |   |   |       |   |           |       |-- mlflow.source.name
    |   |   |       |   |           |       |-- mlflow.source.type
    |   |   |       |   |           |       `-- mlflow.user
    |   |   |       |   |           `-- meta.yaml
    |   |   |       |   `-- OpenEdu_pycaret.ipynb
    |   |   |       |-- Wikimedia
    |   |   |       |   `-- Wikimedia_pycaret.ipynb
    |   |   |       `-- Wikipedia
    |   |   |           `-- Wikipedia_pycaret.ipynb
    |   |   |-- Content Moderation
    |   |   |   |-- Duplicates Discovery
    |   |   |   |   |-- Duplicates_main.py
    |   |   |   |   |-- Duplicates_test.ipynb
    |   |   |   |   `-- README.md
    |   |   |   |-- README.md
    |   |   |   `-- content_moderator.py
    |   |   |-- Content Recommendation
    |   |   |   |-- Existing OpenEdu Contents
    |   |   |   |   `-- Similarity Search
    |   |   |   |       `-- openedu_recommender_by_similarity.ipynb
    |   |   |   `-- External Contents
    |   |   |-- Content Search
    |   |   |   `-- Demo App
    |   |   |       |-- OpenEdu_main.py
    |   |   |       |-- README.md
    |   |   |       |-- Wikimedia-logo.png
    |   |   |       |-- Wikimedia_asset_pic.png
    |   |   |       `-- search_engine_video.gif
    |   |   |-- Content Translation
    |   |   |-- Content Upload
    |   |   |   `-- AI-Autofill
    |   |   |       |-- AI assistant.ipynb
    |   |   |       `-- README.md
    |   |   `-- README.md
    |   |-- Ontology
    |   |   |-- Access
    |   |   |   |-- Exploring the ontology using OWLready2.ipynb
    |   |   |   |-- README.md
    |   |   |   `-- __init__.py
    |   |   |-- Design
    |   |   |   |-- Multilingual Support
    |   |   |   |-- Patterns
    |   |   |   |   `-- README.md
    |   |   |   |-- README.md
    |   |   |   |-- final ontology design.excalidraw
    |   |   |   |-- final ontology designX3.png
    |   |   |   |-- openedu_metadata_schema.xlsx
    |   |   |   |-- taxonomy.png
    |   |   |   |-- test_resource4.png
    |   |   |   `-- unifire-openedu.owl
    |   |   |-- Multilingual Support
    |   |   |   |-- README.MD
    |   |   |   `-- files
    |   |   |       |-- forms
    |   |   |       |   |-- __init__.py
    |   |   |       |   |-- __pycache__
    |   |   |       |   |   |-- __init__.cpython-39.pyc
    |   |   |       |   |   |-- admin.cpython-39.pyc
    |   |   |       |   |   |-- apps.cpython-39.pyc
    |   |   |       |   |   |-- forms.cpython-39.pyc
    |   |   |       |   |   |-- models.cpython-39.pyc
    |   |   |       |   |   |-- urls.cpython-39.pyc
    |   |   |       |   |   `-- views.cpython-39.pyc
    |   |   |       |   |-- admin.py
    |   |   |       |   |-- apps.py
    |   |   |       |   |-- forms.py
    |   |   |       |   |-- migrations
    |   |   |       |   |   |-- 0001_initial.py
    |   |   |       |   |   |-- 0002_rename_your_name_personname_name.py
    |   |   |       |   |   |-- 0003_resource.py
    |   |   |       |   |   |-- 0004_remove_personname_name_remove_resource_description_and_more.py
    |   |   |       |   |   |-- 0005_remove_resourcetranslation_pub_date.py
    |   |   |       |   |   |-- 0006_resourcetranslation_pub_date.py
    |   |   |       |   |   |-- 0007_personname_name_alter_resourcetranslation_pub_date_and_more.py
    |   |   |       |   |   |-- 0008_alter_resourcetranslation_description_and_more.py
    |   |   |       |   |   |-- 0009_remove_resourcetranslation_pub_date_and_more.py
    |   |   |       |   |   |-- 0010_resource_key_competence_resource_level_and_more.py
    |   |   |       |   |   |-- 0011_alter_resource_pub_date_and_more.py
    |   |   |       |   |   |-- 0012_alter_resource_key_competence_and_more.py
    |   |   |       |   |   |-- 0013_alter_resource_key_competence_and_more.py
    |   |   |       |   |   |-- 0014_delete_personname_alter_resource_pub_date.py
    |   |   |       |   |   |-- __init__.py
    |   |   |       |   |   `-- __pycache__
    |   |   |       |   |       |-- 0001_initial.cpython-39.pyc
    |   |   |       |   |       |-- 0002_rename_your_name_personname_name.cpython-39.pyc
    |   |   |       |   |       |-- 0003_resource.cpython-39.pyc
    |   |   |       |   |       |-- 0004_remove_personname_name_remove_resource_description_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0005_remove_resourcetranslation_pub_date.cpython-39.pyc
    |   |   |       |   |       |-- 0006_resourcetranslation_pub_date.cpython-39.pyc
    |   |   |       |   |       |-- 0007_personname_name_alter_resourcetranslation_pub_date_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0008_alter_resourcetranslation_description_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0009_remove_resourcetranslation_pub_date_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0010_resource_key_competence_resource_level_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0011_alter_resource_pub_date_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0012_alter_resource_key_competence_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0013_alter_resource_key_competence_and_more.cpython-39.pyc
    |   |   |       |   |       |-- 0014_delete_personname_alter_resource_pub_date.cpython-39.pyc
    |   |   |       |   |       `-- __init__.cpython-39.pyc
    |   |   |       |   |-- models.py
    |   |   |       |   |-- static
    |   |   |       |   |   `-- style.css
    |   |   |       |   |-- templates
    |   |   |       |   |   |-- index.html
    |   |   |       |   |   |-- name.html
    |   |   |       |   |   |-- newlang.html
    |   |   |       |   |   |-- newresource.html
    |   |   |       |   |   |-- resourceview.html
    |   |   |       |   |   `-- thanks.html
    |   |   |       |   |-- tests.py
    |   |   |       |   |-- urls.py
    |   |   |       |   `-- views.py
    |   |   |       |-- locale
    |   |   |       |   |-- de
    |   |   |       |   |   `-- LC_MESSAGES
    |   |   |       |   |       |-- django.mo
    |   |   |       |   |       `-- django.po
    |   |   |       |   |-- en
    |   |   |       |   |   `-- LC_MESSAGES
    |   |   |       |   |       |-- django.mo
    |   |   |       |   |       `-- django.po
    |   |   |       |   |-- fr
    |   |   |       |   |   `-- LC_MESSAGES
    |   |   |       |   |       |-- django.mo
    |   |   |       |   |       `-- django.po
    |   |   |       |   `-- it
    |   |   |       |       `-- LC_MESSAGES
    |   |   |       |           |-- django.mo
    |   |   |       |           `-- django.po
    |   |   |       `-- settings.py
    |   |   `-- README.md
    |   `-- README.md
    `-- test
        |-- Ontology
        |   |-- Access
        |   |   `-- __init__.py
        |   `-- Evaluation
        |       `-- __init__.py
        `-- README.md

    114 directories, 369 files

    ```
