# UniFire Ontology Extension Patterns

## Introduction

* Our Ontology consists of independent modules that can be combined to create the complete schema of the ontology. We also refer to the modules as patterns.
* Each pattern of the ontology is highlighted individually!

![Conceptual Map of Ontology Patterns](https://user-images.githubusercontent.com/58151963/202840481-928e0f49-3c2c-4a81-b76e-560fddd4bf3f.jpg)
## Patterns

 * [A: Educational Resource](#Educational-Resource)
 * [B: Skill](#Skill) 
 * [C: Test](#Test)
 * [D: Knowledge Topic](#Knowledge-Topic)
 * [E: Learning Path](#Learning-Path)
 * [F: Recommendation](#Recommendation)
 * [G: User Profile](#User-Profile)
 
## Educational Resource


This pattern represents the actual educational materials used to learn a specific Knowledge Topic (pattern D). Educational resources in UnFire are described with three main classes and several data-type properties. 
* An educational resource has one or more Quality Indicators. Each indicator can measure the quality of a specific feature of the educational resource. For example, a video educational resource can have a quality value of its content and another quality value for its resolution. Educational resources also have different Multimedia Types, including the most common four classes (Video, Audio, Image, Text). The educational resource can be accessed in different methods by different users. Therefore, the Accessibility class in this pattern is used to represent: 
    - 1) the accessibility needs of a certain user. For example, the font size requirements of a user with visual impairment. 
    - 2) the access rights of different users. This can be the case of an OER repository that allows accessing advanced materials for users who finished the basic ones, for instance. The Accessibility class is directly related to the User Profile (pattern G) for personalizing the user's access to educational resources.


## Skill

* It represents  skills that the user gains from learning the Knowledge Topics (pattern D). 
## Test



* Test class  is provided to cover the assessment tasks of Knowledge Topics (pattern D). A test is offered to the user (pattern G) in the form of one or more Questions. The user solves the Test by providing Answers to its Questions. Moreover, Questions and Answers can be framed in an Exercise class (pattern C) to group or categorise the tasks in one Test.

## Knowledge Topic



* The Knowledge Topic class lies at the centre of ontology. It represents the topics that users require to learn to gain a particular skill. 

## Learning Path


We introduce the Learning Path pattern in UniFire to address two issues: 
1.  the complexity of some Skills, which require multiple Knowledge Topics to cover it, and 
2.  the learning history of a particular user, which may have implications on the recommended Knowledge Topics in the future. This is why the Learning Path and Recommendation patterns (patterns E and F, respectively) intersect in UniFire. 
Each Learning Path has a final Learning Goal, which is usually the last step of the path. A Learning Path also has one or more Learning Outcomes, which are achieved through all the Knowledge Topics that compose the Learning Path. 

## Recommendation

* The recommendation class  is designed to provide OER hosting repositories and educational platforms to generate learning recommendations for their users. The Recommendation is personalized to the user’s needs based on their User Profile (pattern G). It defines an element in the Learning Path (pattern E). Therefore, by generating a sequence of Knowledge Topic recommendations, a full Learning Path is defined and personalized for each user. 



* We developed as a user-centric ontology that gives personalization great importance. The User Profile pattern is designed to reflect this focus by introducing a variety of classes to cover the user information that influences the learning. Those classes include the user’s Learning Goals, Learning Preferences, Accessibility requirements, Academic Parameters, and Psychological Parameters.
We takes into consideration the effect of the psychological factors on the learning process. Therefore, the Psychological Parameter class is introduced to account for the user’s state of mind and reflect it on the learning recommendations. Academic Parameters class plays the same role for the academic performance information that the user achieved during their learning. Accessibility Class (pattern A) is meant to reflect the user access requirements as well as access rights of the Educational Resources. To support those classes, a history of the user’s learning actions is stored in the User Logs class. This way, the recommendation is generated based on three levels of information: the user Learning Goals, Learning requirements and preferences, and the past learning history. 
