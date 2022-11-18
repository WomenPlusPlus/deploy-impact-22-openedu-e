# deploy-impact-22-openedu-e
Repository for Team OpenEdu-E for deploy(impact) 2022

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
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)

## 🧐 Problem Statement <a name = "problem_statement"></a>
In the center of attention there is OpenEdu.ch which is the open education resources (OER) platform. Its mission is enabling sharing OER for teaching and learning, collaboration between educators in creating and reusing materials.

- IDEAL: 
The content of the website is easy to navigate and the search functionality is intuitive and provides sufficient and organized information to the users of the portal with suggestions of other related entries. 
Wikimedia Community and Educators can easily upload new content, the uploading process is faciliated with automatic tools and the uploading forms are comfortable to understand and navigate.
The Scientific Board can approve or modify the newly uploaded content quicker based on the automatic testing functions.The new relevant content is also proposed automatically based on the parametrization given by the Moderators.
Users can contact the other users for open collaboration. 

- REALITY: 
The filters available on the website are unintuitive and the browsing and search for specific resources is tiresome and the resources are described in a very simple way. The content can also be duplicated.   

- CONSEQUENCES: 
Blocked cooperation between educators due to lack of contact info. 
Dispersion of useful resources in various places and huge difficulty with finding a needed content that would enable learning or teaching. 
Upload of new resources is manual and complicated. 
Moderation of the proposed content requires human action and fully manual analysis which hinders addition of bigger volume of resources.

## 💡 Idea / Solution <a name = "idea"></a>
The prepared solution is a knowledge management and discovery tool for OpenEdu.ch.
Our product includes elements and workflows of streamlined uploading process, as well as moderation of the new content uploaded manually or automatically as a result of discovery of new relevant resources.  
<p align="center">
<a href="" rel="noopener">
  <img src="https://user-images.githubusercontent.com/37207832/202766910-7e2b231b-e6d3-4119-9bda-7e80d299e51f.png" alt="Overview" width="630" height="380">
</a>
</p>
                   
Our value proposition:
- Versatile Ontology for Knowledge Management and fostering collaboration between different users 
- Mulitlingual Ontology Support built with Django 
- AI Engine enabling AI features (for Moderation and Upload) 
- Moderation Board Workflow
- Uploading Process 
- Semantic Search
- New Relevant Content sraping
- Figma Prototype with UI/UX Design.

<p align="center">
<a href="" rel="noopener">
<img src="https://user-images.githubusercontent.com/37207832/202767064-dd8d1011-79fb-45ee-8a0c-ae22fde70e1c.png" alt="Overview" width="520" height="340">
</a>
</p>


## Repository Structure: 
The generic schema of folder is created as following:
- src: Codes and parametrization of the module.
- doc: Descritpive documentation of the module.
- test: Test experiment.  

Tree:
1.	README.md: Overall Project Statement 
2.	src → Core modules
    ○	Format: Folders + README.md
    ○	Content:
    ■	Folders → Scripts
    ■	Data
      ■	Datasets
      ■	Database schema
      ■	Data Scraping
      ■	README.md
    ■	README.md 
    ■	Architecture
      ■	Overall Architecture
      ■	UI - Backend/Frontend
      ■	Flowcharts/Diagrams
      ■	SQL/NoSQL
      ■	Ontology mapping
    ■	Ontology
      ■	README.md
      ■	Contents
      ■	Intro
        ■	Abstract
      ■	Use Case
      ■	Explain Folders contents
      ■	Design
      ■	README.md
      ■	Overview of the classes → nice image of the design conceptual map
      ■	Tools
      ■	OWL/RDF/JSON files
      ■	metadata.txt
      ■	Patterns
      ■	Navigation
      ■	Access/Read and Edit
      ■	Visualization
      ■	Documentation
      ■	Querying
    ■	Testing and Evaluation
      ■	Ontology Competency Questions 
    ■	NLP Pipeline, # Topics Elaborated
    ■	Topics prediction and Similarity Search → serve for the recommendation later and deduplication
      ■	README.md
      ■	Scripts/Experiments
      ■	Recommendation
      ■	README.md
    ■	Upload
      ■	README.md: Make it smoother, how?
      ■	Filters Suggestions!
      ■	Description → Summarization
      ■	Language detection
    ■	Moderation
      ■	README.md
      ■	License Checker
      ■	Link Checker
      ■	Content moderation
      ■	Text
      ■	Image
      ■	Duplicates Discovery
      ■	Ontology Learning Experiments
      ■	README.md
    ■	Topics clustering (before)
      ■	Multi-class multi-label classification (once classes are defined)
      ■	README.md
    ■	ML (Optional)
      ■	README.md 
    ■	Additional AI Features (Within each folder or separately, we’ll decide!)
      ■	Important Note: Show how modules/folders:
      ■	connect with the project → user-based → map user journey
      ■	We’re telling a story! key points + our answers below!
    ■	Upload
      ■	Make process smoother
    ■	Moderation
    ■	  Quality/policy Check
    ■	content Search:
    ■	use content - elaborate projects
    ■	Search Engine
    ■	Collaboration of Authors
    ■	Class: collection
    ■	inter-connect
    3.	test
    4.	docs
    5.	LICENSE file



## ⛓️ Dependencies / Limitations <a name = "limitations"></a>
- What are the dependencies of your project?
- Describe each limitation in detailed but concise terms
- Explain why each limitation exists
- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.
- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if 
appropriate, describe how these limitations could point to the need for further research.

Limitation of the created product:
- Enhance current MVP into a finite product
- Data Architecture solution: The solution does not cover database schema, webservices setup and scalability solutions. This part has been moved out of the scope of the project due to the time constraint within the 6 week program. 
- 


## 🚀 Future Scope <a name = "future_scope"></a>
- Data Architecture and Backend Development: the current solution includes the general recommendations and UML diagram of a relational DB mapped to the newly proposed ontology. 
- Ontology extensions:  For adopting additional content to OpenEdu.ch we created concepts of new classes and relationships which can be included to the ontology.
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
- Django plugin Django-parler.

## Languages
- Python 3.8
- OWL 2 Web Ontology Language
- RDF (Resource Description Framework)

## ✍️ Authors <a name = "authors"></a>
- [@slashlan](https://github.com/slashlan)
- [@s-vigolo](https://github.com/s-vigolo)
- [@Ibtihel-ouni](https://github.com/Ibtihel-ouni)
- [@cyyang50](https://github.com/cyyang50)
- [@YasmineM311](https://github.com/YasmineM311)
- [@gildafc](https://github.com/gildafc)
- [@annopol](https://github.com/annopol)
