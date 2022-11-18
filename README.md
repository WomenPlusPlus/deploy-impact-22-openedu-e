# deploy-impact-22-openedu-e

<p align="center">
  <a href="" rel="noopener">
 <img src="https://user-images.githubusercontent.com/37207832/202691843-84df34e0-180e-40ee-b70d-5a2b37bb5ea2.png" alt="Group logo" width="800" height="200">
    <br></br>
 <img src="https://user-images.githubusercontent.com/37207832/199510757-5fde0b18-bd73-49bc-8c32-1a8827dcdf81.png" alt="Project logo" width="200" height="70">


</a>
</p>
<div align="center">

  [![OpenEdu.CH](https://img.shields.io/badge/project-OpenEdu-orange.svg)](http://openedu.ch) 
  [![Unifire](https://img.shields.io/badge/team-Unifire-orange.svg)](http://openedu.ch) 
  [![Developing](https://img.shields.io/badge/status-Dev-orange.svg)](http://openedu.ch) 

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
OpenEdu.ch is an open education resources (OER) platform. Its mission is enabling sharing OER for teaching and learning, collaboration between educators in creating and reusing materials.

- IDEAL: <br> 
--The content of the website is easy to navigate and the search functionality is intuitive and provides sufficient and organized information to the users of the portal with suggestions of other related entries. <br> 
--Wikimedia Community and Educators can easily upload new content, the uploading process is faciliated with automatic tools and the uploading forms are comfortable to understand and navigate.<br> 
--The Scientific Board can approve or modify the newly uploaded content quicker based on the automatic testing functions.The new relevant content is also proposed automatically based on the parametrization given by the Moderators.<br> 
--Users can contact the other users for open collaboration. <br> 

- REALITY: <br> 
--Unrefined filters for content navigation. <br> 
--Lack of ontology structuring the resources.<br> 
--Only manual actions are needed for content upload and moderation.<br>
--Very long and complicated upload fom<br>
--No multilingual support and the resources are described and created in multiple languages. <br> 

- CONSEQUENCES: <br> 
--Difficulty finding relevant resources on the website and in the web. Unintuitive navigation on the website.<br> 
--Upload of new resources is manual and complicated. <br> 
--Fully manual moderation of the newly proposed content which hinders addition of bigger number of resources.<br> 
--Blocked cooperation between educators due to lack of available contact information. <br> 


## 💡 Idea / Solution <a name = "idea"></a>
The prepared solution is a knowledge management and discovery tool for OpenEdu.ch.
Our product includes elements and workflows of streamlined uploading process, as well as moderation of the new content uploaded manually or automatically as a result of discovery of new relevant resources.  
<p align="center">
<a href="" rel="noopener">
  <img src="https://user-images.githubusercontent.com/37207832/202766910-7e2b231b-e6d3-4119-9bda-7e80d299e51f.png" alt="Overview" width="660" height="380">
</a>
</p>
                   
Our value proposition:
- Versatile Ontology for Knowledge Management allowing easier browsing, searching and fostering collaboration between educators
- Mulitlingual Ontology Support for enabling navigating materials created and described in foreign languages 
- AI Engine enabling AI features (for Moderation and Upload) 
- Moderation Board Workflow designed for more efficient approval process of the new content 
- Uploading Process simplified and facilitated by organized forms and automatic functionalities
- AI-based features facilitating the analysis of the new content and its moderation, as well as linking related materials 
- Semantic Search for more relevant
- Suggesting new Relevant Content for addition to the OpenEdu 
- Figma Prototype with UI/UX Design.

<p align="center">
<a href="" rel="noopener">
<img src="https://user-images.githubusercontent.com/37207832/202767064-dd8d1011-79fb-45ee-8a0c-ae22fde70e1c.png" alt="Overview" width="650" height="380">
</a>
</p>


## Repository Structure: 
The generic schema of folders created for documentation is as following:
- src: Codes and parametrization of the module.
- docs: Descritpive documentation of the solution and presentation [to add].
- test: Test experiment.  

#### Repo tree:
* [docs/](.\deploy-impact-22-openedu-e\docs)
  * [Future Outlooks/](.\deploy-impact-22-openedu-e\docs\Future Outlooks)
    * [README.md](.\deploy-impact-22-openedu-e\docs\Future Outlooks\README.md)
  * [Work Documentation/](.\deploy-impact-22-openedu-e\docs\Work Documentation)
    * [Architecture/](.\deploy-impact-22-openedu-e\docs\Work Documentation\Architecture)
    * [Data/](.\deploy-impact-22-openedu-e\docs\Work Documentation\Data)
    * [NLP Pipeline/](.\deploy-impact-22-openedu-e\docs\Work Documentation\NLP Pipeline)
    * [Ontology/](.\deploy-impact-22-openedu-e\docs\Work Documentation\Ontology)
    * [README.md](.\deploy-impact-22-openedu-e\docs\Work Documentation\README.md)
  * [README.md](.\deploy-impact-22-openedu-e\docs\README.md)
* [src/](.\deploy-impact-22-openedu-e\src)
  * [Architecture/](.\deploy-impact-22-openedu-e\src\Architecture)
    * [Backend/](.\deploy-impact-22-openedu-e\src\Architecture\Backend)
    * [UI Design/](.\deploy-impact-22-openedu-e\src\Architecture\UI Design)
  * [Data/](.\deploy-impact-22-openedu-e\src\Data)
    * [Database/](.\deploy-impact-22-openedu-e\src\Data\Database)
    * [Datasets/](.\deploy-impact-22-openedu-e\src\Data\Datasets)
    * [Scraped Data/](.\deploy-impact-22-openedu-e\src\Data\Scraped Data)
  * [NLP/](.\deploy-impact-22-openedu-e\src\NLP)
    * [Content Analysis/](.\deploy-impact-22-openedu-e\src\NLP\Content Analysis)
    * [Content Moderation/](.\deploy-impact-22-openedu-e\src\NLP\Content Moderation)
    * [Content Recommendation/](.\deploy-impact-22-openedu-e\src\NLP\Content Recommendation)
    * [Content Search/](.\deploy-impact-22-openedu-e\src\NLP\Content Search)
    * [Content Upload/](.\deploy-impact-22-openedu-e\src\NLP\Content Upload)
    * [README.md](.\deploy-impact-22-openedu-e\src\NLP\README.md)
  * [Ontology/](.\deploy-impact-22-openedu-e\src\Ontology)
    * [Access/](.\deploy-impact-22-openedu-e\src\Ontology\Access)
    * [Design/](.\deploy-impact-22-openedu-e\src\Ontology\Design)
    * [Multilingual Support/](.\deploy-impact-22-openedu-e\src\Ontology\Multilingual Support)
    * [README.md](.\deploy-impact-22-openedu-e\src\Ontology\README.md)
  * [README.md](.\deploy-impact-22-openedu-e\src\README.md)
* [test/](.\deploy-impact-22-openedu-e\test)
  * [Ontology/](.\deploy-impact-22-openedu-e\test\Ontology)
    * [Access/](.\deploy-impact-22-openedu-e\test\Ontology\Access)
    * [Evaluation/](.\deploy-impact-22-openedu-e\test\Ontology\Evaluation)
  * [README.md](.\deploy-impact-22-openedu-e\test\README.md)
* [LICENSE](.\deploy-impact-22-openedu-e\LICENSE)

Moreover, please note: 
- README.md
- licence: GPL license.

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
- [Azure](https://https://portal.azure.com/) - Azure Cloud [TO DO: which component? Ibti, cognitive + sth else? ]
- [Figma](https://nodejs.org/en/) - Prototyping tool
- Ontology Editor: Protégé 5.5.0
- Django plugin Django-parler

## Languages
- Python 3.8
- OWL 2 Web Ontology Language
- RDF (Resource Description Framework)

## ✍️ Authors <a name = "authors"></a>
- [@slashlan](https://github.com/slashlan), Data Scientist, Deputy PM 
- [@s-vigolo](https://github.com/s-vigolo), Backend Developer
- [@Ibtihel-ouni](https://github.com/Ibtihel-ouni), Data Scientist
- [@cyyang50](https://github.com/cyyang50), Data Scientist 
- [@YasmineM311](https://github.com/YasmineM311), Data Scientist
- [@gildafc](https://github.com/gildafc), Data Scientist, Team Satellite
- [@annopol](https://github.com/annopol), Data Scientist, PM
