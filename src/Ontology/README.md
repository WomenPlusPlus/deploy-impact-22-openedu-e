#  Ontology_Name

## Contents
* [Introduction](#Introduction)
* [Abstract](#Abstract)

* Implementation in Protégé 


After the initial step of conceptualizing and creating a mockup for the ontology, we looked into tools to implement it. We decided to use Protégé, an ontology development tool developed by Stanford university. Protégé is a well-developed and supported user-friendly interface for creating and editing ontologies with full support for the OWL 2 Web Ontology Language. A good starting point for us was reading the Ontology development 101 [guide by Stanford university](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf). Another important guide was reading and referring to this [practical guide](https://drive.google.com/file/d/1A3Y8T6nIfXQ_UQOpCAr_HFSCwpTqELeP/view) to building ontologies in Protégé, which details building the famous Pizza ontology in Protégé.
We used Protégé version 5.5 which the latest version to date. 
An important feature of Protégé is the Reasoner. The Reasoner is a tool that when activated, checks the ontology for inconsistencies and makes inferences based on the current state of the ontology. 
After creating the necessary elements of the ontology; namely classes and subclasses, object properties (aka relationships), and data properties (aka attributes), defining constraints and specifying data types, we created instances for 26 of the current content uploaded on opened.ch. In addition to mapping what is already present on openedu to the current ontology, we also added additional metadata for uploaded resources that are now enabled by the new ontology design. We also created instances for institutions and their associated profiles and linked them to instances of resources through the hasUploader and isUploadedBy object properties. 


**Enumerated Classes**
Protégé offers the concept of enumerated classes, which are classes that are limited to and only to a set of individuals, please refer to the relevant content in the abovementioned links. We used these classes for concepts like key competencies, skills, languages, knowledge topics… etc




* Classes

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


* Object properties (aka entity relationships)


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
| hasResource | Knowledge topic | Resource | A knowledge topic has resource(s) |
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


* Data properties (aka attributes)

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
