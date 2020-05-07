# PySpark - GraphFrames and Graph Theory

## Introduction

Sometimes, it can be difficult to explain or better comprehend certain types of dataset or data problems with just a simple distribution charts, pie charts or scatter plots. These kinds of dataset can consists of geographical data points, social networks or user interactions. This is where graphs that consists of 3 components that are edges, nodes (or vertices) and their properties are utilised to represent these kinds of data problems in a more intuitive and easier way for comprehension. The ability to simply assign nodes to anything and define their relationship (between these nodes) with edges provides a great amount of flexibility to represent the data in a different way. This can also means that it is possible to connect two seemingly disparate graphs into a common graph, as long as there is a link that can be found between the nodes of the two disparate graphs. For example, joining a social network with restaurant recommendations, number of travellers and airport delays etc.

## Breakdown of this Notebook

- An Introduction to Graph Theory and GraphFrames for Apache Spark
- Installing GraphFrames
- Data Preparation
- Building the Graph
- Running queries against the graph
- Understanding the Graph
- Utilise PageRank to determine airport ranks
- Finding the fewest number of connections (flights)
- Visualising the Graph.

## Why use GraphFrames with Spark?

One of the main problems that persist when designing and computing graphs is that the traversal and computation of these graphing algorithms are often computationally expensive and at times can be very slow. To overcome this, GraphFrames with Apache Spark is able to take advantage of the performance inherent of the DataFrames where it is distributed. 

### Under the hood of GraphFrames:

GraphFrames utilises two Spark DataFrames where one would be used for the nodes and another for the edges, it leverages the optimisations and simplicity of the DataFrame API and in addition, it can be used and interacted with by other programming languages such as Python, Java and Scala APIs.

## Datasets:

The datasets for this project are the (1) Airline On-Time Performance and Causes of Flight Delays data which consists of information about scheduled and actual departure/arrival times along with the delay causes, and (2) OpenFlights data which details the airport and airlines. More details can be found in the link below.

The Datasets are obtained from:
- https://catalog.data.gov/dataset/airline-on-time-performance-and-causes-of-flight-delays-on-time-data or https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time
- https://openflights.org/data.html

Or download the folder from this repository which should contain the following files:
- airport-codes-na.txt
- departuredelays.csv

## Summary:

From this project I was able to learn about building graphs with GraphFrames, where it is similar to GraphX (based on RDDs) but utilises DataFrames instead. This also brings about the performance improvements that is inherent to DataFrames. I was able to learn how to query the graph to gain more specifc details and draw/discover more about the dataset with methods like pageRank or BFS. Further, with the aid of NetworkX libraries, the visualisation of the connecting flights between airports were also made possible. 
