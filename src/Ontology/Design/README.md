## Contents

* [1. Introduction](#introduction) 
* [2. Overview](#overview) 
* [3. Conceptualization and logic behind the ontology](#conceptualization-and-logic-behind-the-ontology)
* [4. Classes definition](#classes-definition)
* [5. Object properties (aka entity relationships)](#object-properties-(aka-entity-relationships))
* [6. Data properties (aka attributes)](#data-properties-(aka-attributes))
* [7. Constraints](#constraints) 
* [8. Implementation of the Ontology](#implementation-of-the-ontology)
* [9. Testing the ontology](#testing-the-ontology)
* [10. Multilingual Support](#multilingual-support)
* [Development Tools](#tools-used-during-development)
* [Languages](#languages)
* [Ontology files](#Ontology-file)
* [Suggestions for future expansion](#suggestions-for-future-expansion)

## 1. Introduction


## 2. Overview

### 2.1. Ontology mockup
A mockup for the proposed ontology design has been created using excalidraw and can be accessed [here](https://excalidraw.com/#room=ab47f46f93e3c44add0a,JJYUaB1o810ZWsoHbxpeyQ).


### 2.2. Ontology in numbers
The new ontology design consists of **26 classes** (out of which 16 are superclasses), **20 object properties** (aka entity relationships), **28 data properties** (aka attributes). It was implemented using Protégé as discussed later in this [section](#implementation-of-the-ontology) and has **155 instances**, 26 of which are current OpenEdu resources, 10 are test candidate resources that are not on OpenEdu currently, 1 is a collection. The rest are individuals belonging to enumerated classes such as knowledge topic, skills, key competences …. etc.


### 2.3. Taxonomy 

The figure below shows the taxonomy of classes in the new ontology design.

![alt text]( https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/50c9e3546fb738ea1c4dda1fd2612c2a85d3da85/src/Ontology/Design/taxonomy.png)


## 3. Conceptualization and Logic behind the ontology design

### 3.1. Creating a metadata schema

A preliminary step, that paved the path to the ontology design was to extract metadata from the current OpenEdu content and put into a structured schema. This was done by first inspecting OpenEdu`s content one by one, and then digging deeper into the resource by accessing its link and trying to extract relevant information that could be valuable in conceptualizing the ontology. This metadata schema can be accessed [here](https://docs.google.com/spreadsheets/d/1Qb1J6ygn0FOAdwGGGXNcP_pRNIEO41if/edit#gid=323866940), text-rich metadata such as resource description and additional information was put into a separate spreadsheet tab (metadata2), this was used as a dataset for the one of the NLP components of the project. 
Additionally, this schema was helpful when creating instances in Protégé discussed in later [sections](#implementation-of-the-ontology) as it provided a structured and easy access to the information of each resource.


### 3.2. Defining relevant terms 

A crucial step for ontology conceptualization is defining terms and classes relevant for the domain the ontology covers. 


After creating the metadata schema and examining similar platforms, relevant terms for the ontology design became evident to us. We started listing down these terms and tried to envision whether they would be candidates to be classes or attributes in the ontology. Some examples of such terms include [Open access, Open education, Wikimedia sister project, Project type, Project scope, Project target audience, Project location, skills, Project link, Topic, License, Training, Guide, Explanatory video, School project, University project, Professors, Teachers, Students, Online course, Teaching material, Foundation, Events, School, University, Primary school, High school, Free, Beginner, Intermediate, Advanced, Language, Onsite, Online]. 


### 3.3. Questions to be answered by the ontology
It was also important to define the questions that need to be answered by the ontology as they define the perspective and approach by which we should design the ontology.

Below is a sample of these questions: 

1.	I am a student (different levels), what are available open access educational sources available for me?
2.	I am an educator (school teacher/university professor), what are the latest trainings for educators that are also open access?
3.	I am an educator (school teacher/university professor), where can I find open access educational tools?
4.	I work in the xyz domain and want links to free educational content.
5.	Are there trainings on the use of a certain wikimedia project?
6.	What is the location of the course/training? (Online/onsite where specifically)
7.	What are latest (temporal aspect) activities (projects/workshops/events) in a given domain?


### 3.4. Defining classes

#### 3.4.1. The Resource superclass and its subclasses

The term **resource** refers to content uploaded to the platform. One of the things that were immediately clear to us is that the current ontology was limited in terms of categorizing uploaded resources, as they were merely split between projects, trainings and news. The categorization is not well-defined, and the uploaded content doesn’t seem to reflect the definitions that are present. For example “Events and Contests” are supposed to be in News according to the homepage but are actually categorized under Projects. In our opinion, this limited categorization does not reflect the variety of content on the platform. Furthermore, using such generic categorization results in inefficient and incorrect categorization of uploaded content, as is the case currently in OpenEdu.

To tackle this issue, we created additional classes under which uploaded resources can be categorized. We ended up with six subclasses for the Superclass Resource: 

1.	Guides & Tutorials
2.	Tools
3.	Open content online Resources
4.	Events & Contests
5.	Trainings & Workshops
6.	Projects


These categories are based on the content currently on OpenEdu, however, we kept in mind other resources that could be relevant to OpenEdu as described by the Product Owner and also inspired by our own research. Therefore, this new categorization would be flexible and provide a good base for future expansions of the platform.

Once these 6 classes were chosen, we worked on defining them properly and discussed what attributes were necessary for each one and which were optional, still trying to keep in mind that flexibility to describe content and use cases we hadn’t yet considered. Once we defined the attributes for each subclass, we could more clearly see which ones were common to all and could go be assigned directly to the Superclass level. 

Afterwards, we inspected the remaining attributes that are specific to one or a subset of the subclasses. A natural separation between the 6 Classes appeared. Projects, Trainings & Workshops and Events & Contests, had common attributes that reflect their dynamic nature; namely location attributes like country, city, canton, and nature of attendance (online/onsite/hybrid), in addition to temporal attributes, such as start date, end date, duration and recurrence. 

On the other hand, Guides & Tutorials, Tools and Open content online Resources did not have these dynamic attributes. Subsequently, it was reasonable to group the 6 subclasses into 2 intermediate classes:

1.	Dynamic content
2.	Aiding tools and reference material 

The intermediate subclass **Dynamic Content** has for subclasses Projects, Trainings & Workshops and Events & Contests. They are grouped together by being resources that have a dynamic nature, i.e., are activities that can have a time and a place. For example, a professor running a Project with their students is a resource that is happening in a university (a place) and for a specific semester (a time). Likewise, Events & Contests implicitly have a date connected to them (the date of the event and the deadline for the submission of the contest) and can have a place if they’re not happening online. 
The intermediate subclass **Aiding Tools and Reference Materials** has for subclasses Guides & Tutorials, Tools, Open content online resources. These are all resources that can be accessed completely online at any time.

#### 3.4.2. The Collections superclass

The aim of the superclass is to provide a way for OpenEdu moderators to group and highlight a group of resources that share a common theme. For example, a collection “Wikimedia sister projects” groups all Wikimedia sister projects regardless of their categorization, similarly a collection “Wikipedia-related content” groups resources such as tools, tutorials, trainings and projects that are focused on Wikipedia. These collections could be highlighted in the main page as one of several methods to filter the content on OpenEdu.

#### 3.4.3. Enumerated superclasses

These are classes that represent important concepts in the ontology. They are characterized by having a defined set of individuals (aka instances). For example, the class **Attendance form** is defined by three and only three individuals: online, onsite and hybrid, hence the name “enumerated”.
The majority of these classes can be used as filters for the content on OpenEdu. Our recommendation is to use **Knowledge topic**, **Educational level** and **Language** as the main filters in the homepage, and to reserve other classes, namely **Key competences**, **Skills**, **Target audience**, **Attendance form** and **Difficulty level** as advanced filters, that appear when the user moves forward with their search. Such an approach minimizes the possibility of overwhelming the user at an early point in their journey of exploring the resources on OpenEdu.

Another class in this category is the **license** class which represents the license of the resource, this could potentially be a filter in the future, for now that is not feasible as all content has the license CCbySA. 

#### 3.4.4. Uploader classes

These are classes that represent the body of content uploaders on the platform. We make a distinction between two different uploaders, the **User** superclass represents an uploader who is an individual and the **institution** superclass which represents an uploader which is either an educational institution such as schools and universities, or a foundation such as WikimediaCH.
Another two related superclasses are the **User profile** and the **Institution profile** which are detailed profile that are linked to the corresponding User or Institution.


While defining these classes, their attributes and the relationships between them, we made the following assumptions:
1.	In order to upload a resource on OpenEdu, one must register or log in to the platform
2.	Creating a profile is not mandatory to upload a resource
3.	A user profile can be affiliated with an institution profile


An additional class belonging to this section is the **User role** which is at the moment limited to either “learner” or “educator”. 
This class has been added to account for a possible extension of the platform (and the ontology) to include learning paths to users that identify as learners. 


## 4. Classes definition

| Class| Description| 
| ------------- | ------------------------------------------- |
| Resource | Any content that is uploaded to the platform|                             
| Dynamic content | content that is more dynamic in nature and mostly has a temporal aspect | 
| Aiding tools and reference material | facilitator content such as tools, guiding material and open-content resources |
| Projects | ongoing or legacy projects and collaborations |
| Events & Contests | past, present and future events and contests |
| Trainings & Workshops | past, present and future trainings and workshops |
| Guides & Tutorials | explanatory guides and tutorials|
| Open content online resources | an online resource offering content that is open to public use |
| Tools | open access aiding tools |
| Institution | An educational institution or foundation that could offer content to the openedu platform |
| Educational institution | Institutions such as and not limited to schools and universities |
| Foundation | nonprofit corporation or a charitable trust that makes grants to organizations, institutions, or individuals for charitable purposes |
| Institution profile | The detailed profile of an institution |
| User | An individual using the openedu platform either to upload content or for learning purposes |
| User profile | The detailed profile of a user |
| Collections | A collection of resources that share a topic or theme |
| Attendance form | The attendance form of an activity, whether online or onsite |
| Difficulty level | The level of difficulty of a given resource on the platform |
| Educational level | The educational level to which a resource is directed |
| Key competencies | The European key competences that are trained by a given resource|  
| Knowledge topic | The knowledge topic spanned by the resource |
| Language | A list of languages |   
| License | The license of a given resource |
| Skills | Skillset that is trained by a given resource |
| Target audience | The audience to which the resource content is directed |
| User role | The role played by the user on the platform, could be learner or educator | 


## 5. Object properties (aka entity relationships)


| Object Property | Domain (subject) Class | Range (object) Class | Description | 
| ------------- | ------------------------ | -------------------- | ----------- |
| hasAffiliatedUsers | Institution profile | User profile | Institution profile has affiliated user profiles |
| isAffiliatedTo | User profile | Institution profile | A user profile is affiliated to an institution`s profile |
| hasAttendanceForm | Dynamic content | Attendance form | Dynamic content has attendance form |
| hasDifficultyLevel | Guides & Tutorials/Trainings & Workshops | Difficulty level | Guides & Tutorials/Trainings & Workshops have a difficulty level |
| hasLanguageOfContent | Resource | Language | A resource has language of content |
| hasLicense | Resoucrce | License | A resource has a license |
| hasPartner | Resource | Institution | A resource could have partner institutions/organizations other than the uploader who are part of the openedu platform and are collaborators or partners to its content |
| hasProfile | User/Institution | User profile/Institution profile| A user or an institution have a detailed profile |
| hasRole | User | User role | A user has one or more role(s) | 
| hasTarget | Resource | Target audience | a resource has a target audience |
| hasTopic | Resource | Knowledge topic | A resource has a knowledge topic |
| hasUploader | Resource | User/Institution | A resource has an uploader |
| isUploaderOf | User/Institution | Resource | A user/institution is the uploader of a resource |
| isForEducationalLevel | Resource | Educational level | A resource is for one or more educational levels |
| isGroupOf | Collections | Resource | A collection is a group of resources sharing a theme |
| isPartOf | Resource | Collections | A resource can be part of a collection |	
| isLinkedTo | User Profile/Institution profile | User/Institution | A user profile is linked to a specific user/ an institution profile is linked to a specific institution |
| trainsKeyCompetency | Resource | Key competences | A resource trains one or more key competences |
| trainsSkill | Resource | Skills | A resource trains one or more skills |
| utilizes | Aiding tools & Reference material/Dynamic content | Aiding tools & Reference material | A resource from the subclass Aiding tools & Reference material can utilize another resource from the same class/ A resource form dynamic content can utilize a resource from Aiding tools & Reference material |  


## 6. Data properties (aka attributes)

| Data Property | Domain (subject) Class | Range (object) Datatype | Description | 
| ------------- | ---------------------- | ----------------------- | ----------- |
| hasAccessibilityFeatures | Resource | boolean | A resource has or does not have accessibility features |
| hasAdditionalInfo | Resource | string | A resource has additional more detailed information |
| has Address | Institution profile | string | An institutions profile has its physical address |
| hasBio | User profile | string | A user profile has their bio |
| hasDescription | Resource/Collections/Institution profile | string | An instance of domain classes has a description |
| hasDuration | Dynamic content | integer | An instance of the class has a duration in days |
| hasEmailAddress | User/Institution | string | A user/institution has an email address |
| hasStartDate | Dynamic content | datetime | An instance of the class has a start date |
| hasEndDate | Dynamic content | datetime | An instance of the class has an end date |
| hasExternalPartner | Resource | string | A resource can have a text listing institutions/organizations that are collaborators or partners to creating its content but are not on openedu platform |
| hasFunding | Projects | string | A project has a text describing the type of funding and funding body |
| hasId | Resource/Collections/User/Institution | string | An instance of these classes has a unique identifier |
| hasLink | Resource/Institution profile/License | URI | link leading to more information on the instance |
| hasLocationCanton | Dynamic content/Institution profile | string | Geographical location: canton (Relevant if the country is CH only) |
| hasLocationCity | Dynamic content/Institution profile | string | Geographical location: city |
| hasLocationCountry | Dynamic content/Institution profile/User profile | string | Geographical location: country |
| hasMedia | Resource | URI | Resource can have links to relevant media files |
| hasName | User/Institution/Collections/License | string | instance has a name |
| hasNumberOfContributions | User profile/Institution profile | integer | User profile or institution profile has number of contributions to the platform |
| hasPersonalTitle | User profile | string | User profile has their preferred personal title | 
| hasRecurrence | Dynamic content | boolean | An instance of the class is either recurrent or not |
| hasRecurrenceDescription | Dynamic content | string | An instance of the class has description of the nature of its recurrence rate |
| hasSocialNetworkProfile | User profile/Institution profile | URI | A user profile or institution profile has links to their social network profile(s) |
| hasSponsor | Events & Contests | string | An instance of the class has a sponsor | 
| hasTitle | Resource | string | A resource has a title | 
| hasSubtitle | Resource | string | A resource has a subtitle (i.e. tagline) |
| hasTag | Resource | string | A resource has tag(s) which are short text (one or two words) that describe the content of a resource |
| hasTelephoneNumber | Institution profile | string | An institution profile has its telephone number |


## 7. Constraints

## 8. Implementation of the ontology 

After the initial step of conceptualizing and creating a mockup for the ontology, we looked into tools to implement it. We decided to use Protégé, an ontology development tool developed by Stanford university. Protégé is a well-developed and supported user-friendly interface for creating and editing ontologies with full support for the OWL 2 Web Ontology Language. A good starting point for us was reading the Ontology development 101 [guide by Stanford university](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf). Another important guide was reading and referring to [this practical guide](https://drive.google.com/file/d/1A3Y8T6nIfXQ_UQOpCAr_HFSCwpTqELeP/view) to building ontologies in Protégé, which details building the famous Pizza ontology in Protégé.
We used Protégé version 5.5 which the latest version to date. 
An important feature of Protégé is the Reasoner. The Reasoner is a tool that when activated, checks the ontology for inconsistencies and makes inferences based on the current state of the ontology. 
After creating the necessary elements of the ontology; namely classes and subclasses, object properties (aka relationships), and data properties (aka attributes), defining constraints and specifying data types, we created instances for 26 of the current content uploaded on opened.ch. In addition to mapping what is already present on openedu to the current ontology, we also added additional metadata for uploaded resources that are now enabled by the new ontology design. We also created instances for institutions and their associated profiles and linked them to instances of resources through the hasUploader and isUploadedBy object properties. 

**Enumerated Classes**
Protégé offers the concept of enumerated classes, which are classes that are limited to and only to a set of individuals, please refer to the relevant content in the abovementioned links. We used these classes for concepts like key competencies, skills, languages, knowledge topics… etc



## 9. Testing the ontology


In order to test our ontology and it`s capability to describe other candidate resources, we developed and used a crawler to suggest open education resources that could be relevant to the scope of OpenEdu. 
The crawler suggested several resources some of which were already part of OpenEdu. After exclusion of irrelevant ad redundant content, 10 resources were considered suitable for incorporation into the platform, all of which were successfully classified by the new ontology and implemented into Protégé.
For ease of identification of these resources, the corresponding instances created in Protégé start with the prefix **Test**. 

![alt text](Ontology/Design/test_resource4.png)



This was also an opportunity to showcase a scenario where the uploader is an individual and not an institution. For the current OpenEdu content, we affiliated each resource to the institution that created it, e.g., Wikimedia foundation, University of Zurich, Wikimedia Germany etc., however, when implementing the 10 test resources into Protégé, we created a user (a member of our team), created metadata for their hypothetical user profile details, and affiliated the test instances to them. 


![alt text]( https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/50c9e3546fb738ea1c4dda1fd2612c2a85d3da85/src/Ontology/Design/user.png)





## 10. Multilingual Support



## Tools 

* Ontology Editor: [Protégé 5.5.0](https://protege.stanford.edu/products.php#desktop-protege)

## Languages

* [OWL 2 Web Ontology Language](https://www.w3.org/TR/owl2-overview/)
* [RDF (Resource Description Framework)](https://en.wikipedia.org/wiki/Resource_Description_Framework) 


## Ontology files


