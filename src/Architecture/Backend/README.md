## Introduction
In order to map the ontology to a backend database, we conducted a thorough research of approaches by which this can be achieved. Many database types are used for this purpose such as relational databases, non-relational databases and graph databases.

We opted to mapping our ontology to a relational database due to the following reasons:
-	time constraints
-	high familiarity of our team with RDB
-	OpenEdu is currently using a RDB backend

Researchers have proposed several approaches to store and manage ontological data in relational databases. Relational ontology storage approaches could be either: schema oblivious, schema aware, or mixed schema. Schema oblivious uses fixed relational structure for all ontological content. Schema aware adopts a variable number of relational tables to closely represent ontological data. Mixed schema adopts both schema oblivious and schema aware approaches.

Our chosen approach is a **Schema Oblivious** one. The advantage with this approach is that the schema is ontology independent and therefore more suitable for dynamic ontologies which would be the case with OpenEdu as an iteratively evolving platform. The limitations of this approach are data redundancy and difficult to store more expressive ontologies. 

A relational database mapping an ontology consists of two main components:
-	**The A Box**: Factual ontology components, i.e., instances and their associated relationships and attributes.
-	**The T Box**: Conceptual ontology components, such as class hierarchies, object properties domains and subjects, data properties and constraints.

## Mapping approach 

The process of mapping the ontology to a RDBMS entails the following steps:

A box tables:

-	Classes and subclasses are transformed into separate tables and one-to-one relationships are created among them. 
-	Object properties (aka entity relationships) transformed into table relationships. Additional tables might be needed in some cases to map object properties.
-	Data properties (aka attributes) are transformed into columns or tables according to their values (single value or multi value).

T box tables:
- Creating a table for lass hierarchy
- Creating a table for object properties with their domain and range classes
- Creating a table for data properties with their domain classes and range datatypes
- Creating a table for restrictions with their types, restricted class, property and domain 

To do so we adapted the mapping rules from [this publication](https://pdfs.semanticscholar.org/939d/9c03cdd45016a7e242c54302ce5c73c55bb7.pdf) and other sources as follows:


1.**OWL Classes**

Each OWL Class (Super or subclasses) is transformed into a table in our database. Class name will become Table name. Each table is allocated a primary key. A table that relates to subclass is
assigned a primary key and a foreign key that reference to its “Super table” through one-to-one relationships.

To avoid data redundancy, and in the interest of a more efficient architecture, if a Superclass (e.g. Resource) has subclasses that inherit its properties, its corresponding table in the database is only a list of its instances/individuals or their unique identifiers. The full list of properties will be in the subclass tables.

2.**OWL Object Properties**

- Single valued object properties will be mapped into an entity relationship relating domain and range classes through Primary and Foreign keys.
- The name of the object property will be on the arrow representing the entity relationship in the modeling diagram. A T box table will list object properties together with their domain and range classes.
-  Multi-valued object properties will be mapped into a separate table and will be assigned a primary key that’s a combination of two foreign keys. One foreign key references the primary key of domain table and other to range table. The name of the object property will be the name of Table.

3.**OWL Data Properties**

- Single–valued data type property will be mapped into a column in the table that relates to the domain of data type property. The data type property’s name will become the name of the column.
- Multi–valued data type property will be mapped into a table and will be assigned a primary key that is a
combination of corresponding columns, and a foreign key that reference to the domain table of data type property. The data type property’s name will become the name of the Table


4.**OWL Datatypes**
-Data types are converted from XSD to SQL, because OWL uses XSD data types. The table below shows how to convert different data types from XSD to SQL. An overview of the corresponding sql datatypes for their sxd counterparts can be found [here](https://pdfs.semanticscholar.org/939d/9c03cdd45016a7e242c54302ce5c73c55bb7.pdf). The most commonly used ones in our ontology are:

| xsd | sql |
| ---- | ---- |
| string | string |
| integer | integer |
| anyURI | varchar |
| datetime | timestamp |


4. **OWL Restrictions**
- To preserve all information about ontological constraints, this information is stored in Meta data tables. The table columns, are “type of restriction”, “restriction class” (this column points to the table of the related class), “property” includes the property concerned, “domain class” and “range
Class” of property. 


## Database architecture modelling
Due to time constraints, developing an actual database backend was not feasible. However, the database architecture was modeled into a UML diagram as seen below using [draw io](https://www.diagrams.net/blog/move-diagrams-net). The table is **green** if it is a superclass, **yellow** if it is a 1st level subclass and **blue** if it is a 2nd level subclass. **Purple** tables are for multi-value object properties. The upper section represents **A box** information while the lower section is for **T box**. The image itself can be accessed [here](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/eddddb679360036df4084bf2d0401d9ce40b6406/src/Architecture/Backend/ontology_mapping_to_RDB_database_schema_UML_diagram.png)

![alt text](https://github.com/WomenPlusPlus/deploy-impact-22-openedu-e/blob/6b2a97d7737a54773f7556d527f41738f1ace571/src/Architecture/Backend/ontology_mapping_to_RDB_database_schema_UML_diagram.png)




*Sources*

[Ontology Storage Models and Tools: An Authentic Survey](https://www.degruyter.com/document/doi/10.1515/jisys-2014-0167/html)

[OWLMap: Fully Automatic Mapping of Ontology into Relational Database Schema](https://pdfs.semanticscholar.org/939d/9c03cdd45016a7e242c54302ce5c73c55bb7.pdf)

[The Fundamental Importance of Keeping an ABox and TBox Split](https://www.mkbergman.com/489/ontology-best-practices-for-data-driven-applications-part-2/)

[A novel approach for learning ontology from relational database: from the construction to the evaluation](https://d-nb.info/1229820256/34)



