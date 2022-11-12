
# Implementation in Protégé 
After the initial step of conceptualizing and creating a mockup for the ontology, we looked into tools to implement it. We decided to use Protégé, an ontology development tool developed by Stanford university. Protégé is a well-developed and supported user-friendly interface for creating and editing ontologies with full support for the OWL 2 Web Ontology Language. A good starting point for us was reading the Ontology development 101 guide by Stanford university (https://protege.stanford.edu/publications/ontology_development/ontology101.pdf). Another important guide was reading and referring to this practical guide (https://drive.google.com/file/d/1A3Y8T6nIfXQ_UQOpCAr_HFSCwpTqELeP/view)  to building ontologies in Protégé, which details building the famous Pizza ontology in Protégé.
We used Protégé version 5.5 which the latest version to date. 
An important feature of Protégé is the Reasoner. The Reasoner is a tool that when activated, checks the ontology for inconsistencies and makes inferences based on the current state of the ontology. 
After creating the necessary elements of the ontology; namely classes and subclasses, object properties (aka relationships), and data properties (aka attributes), defining constraints and specifying data types, we created instances for 26 of the current content uploaded on opened.ch. In addition to mapping what is already present on openedu to the current ontology, we also added additional metadata for uploaded resources that are now enabled by the new ontology design. We also created instances for institutions and their associated profiles and linked them to instances of resources through the hasUploader and isUploadedBy object properties. 
**Enumerated Classes**
Protégé offers the concept of enumerated classes, which are classes that are limited to and only to a set of individuals, please refer to the relevant content in the abovementioned links. We used these classes for concepts like key competencies, skills, languages, knowledge topics… etc




# Classes

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


