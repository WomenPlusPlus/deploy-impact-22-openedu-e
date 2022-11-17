# deploy-impact-22-openedu-e
Repository for Team openedu-e for deploy(impact) 2022

<p align="center">
  <a href="" rel="noopener">
 <img src="https://user-images.githubusercontent.com/37207832/199510757-5fde0b18-bd73-49bc-8c32-1a8827dcdf81.png" alt="Project logo">
 </a>
</p>
<h3 align="center">OpenEdu.ch</h3>

<div align="center">

  [![OpenEdu.CH](https://img.shields.io/badge/project-name-orange.svg)](http://openedu.ch) 

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
- [Setting up a local environment](#getting_started)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## 🧐 Problem Statement <a name = "problem_statement"></a>

- IDEAL: The creation of an ontological definition that describes the content found at OpenEdu.ch will improve wikidata learning material organization and reachability. The main goal is to collect all the educational material (from wikimedia and from external sources) in one single place and make this material accessible. 

- REALITY: The filters available on the website are unintuitive and the browsing and search for specific resources is tiresome and the resources are described in a very simple way. The content can also be duplicated.   

- CONSEQUENCES: Blocked cooperation between educators. Dispersion of useful resources in various places and huge difficulty with finding a needed content that would enable learning or teaching. Upload of new resources is manual and tiring. Moderation of the proposed content requires human action and fully manual analysis which hinders addition of bigger volume of resources.

## 💡 Idea / Solution <a name = "idea"></a>
The included product is a solution for knowledge management and discovery of OpenEdu.ch which is a platform listing open educational resources from around the world to enable free sharing of relevant content for teaching and learning. 
Our product includes elements and workflows of streamlined uploading process, as well as moderation of the new content uploaded manually or automatically as a result of discovery of new relevant resources.  

Our value proposition:
- Versatile Ontology for Knowledge Management and fostering collaboration between different users 
- Mulitlingual Ontology Support built with Django 
- AI Engine enabling AI features (for Moderation and Upload) 
- Moderation Board Workflow
- Uploading Process 
- Semantic Search
- New Relevant Content sraping
- Figma Prototype with UI/UX Design.


## Repository Structure: 
The generic schema of folder is created as following:
- src: Codes and parametrization of the module.
- doc: Descritpive documentation of the module.
- test: Test experiment.  

/? links to the specific folders to show the structure? 
1.	README.md (Template Anna to fill out)
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

Limitations:
- Enhance current mvp into a finite product
- Data Architecture with dtaabase schema, webservices and scalability solutions
- 


## 🚀 Future Scope <a name = "future_scope"></a>
- Data architecture design: Within the current scope only the general recommendation are included for microservices architecture, as well as defining the new target data schema for education content.
- Ontology extension: Used for describing additional types of resources or users.
- Machine learning? 

## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development 
and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

Final scripts are written in Python. 
Sonia - Django !
!! * For requirements like install packages 


### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

## 🎈 Usage <a name="usage"></a>
Add notes about how to use the system.

## ⛏️ Built With <a name = "tech_stack"></a>
- [Azure](https://https://portal.azure.com/) - Azure Cloud [TO DO: which component? Ibti, cognitive + sth else? ]
- [Figma](https://nodejs.org/en/) - Prototyping tool

## ✍️ Authors <a name = "authors"></a>
- [@slashlan](https://github.com/slashlan)
- [@s-vigolo](https://github.com/s-vigolo)
- [@Ibtihel-ouni](https://github.com/Ibtihel-ouni)
- [@cyyang50](https://github.com/cyyang50)
- [@YasmineM311](https://github.com/YasmineM311)
- [@gildafc](https://github.com/gildafc)
- [@annopol](https://github.com/annopol)

## 🎉 Acknowledgments <a name = "acknowledgments"></a>
- Hat tip to anyone whose code was used
- Inspiration
- References
