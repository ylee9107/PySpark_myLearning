# Abstracting Data with RDDs

## Introduction:

#### What are RDDs?

RDDs are called __Resilient Distributed Datasets__, where these are a collection of 
immutable JVM objects that are distributed across an Apache Spark Cluster. It is also the most fundamental dataset type for Apache Spark, whereby actions that are on a Spark DataFrame will get translated into highly optimised execution of transformations and actions on RDDs. 
The data would be split up into chunks based on a key and subsequently dispersed to all the executor nodes. The advantages of RDDs are its high resilience and ability to be recovered quickly as the same data chunks are replicated across multiple executor nodes. It also allows functional calculations on all the dataset quickly using mulitple nodes. Further, RDDs keep a log of the execution steps that were applied to each chunk which also combat against data lost by execution error. 

__This notebook will then go through the basics of using PySpark__.

## Breakdown for this Notebook:

- Creating RDDs
- Reading Data from Files
- Overview of RDD Transformations
- Overview of RDD actions
- Pitfalls of using RDDs


## Dataset:

The dataset used here are the following:

1. Airport-codes.txt
2. departure_delays.csv

Source:
- https://openflights.org/data.html
- https://catalog.data.gov/dataset/airline-on-time-performance-and-causes-of-flight-delays-on-time-data


## Summary:

From this project I was able to learn and develop a better understanding of PySpark RDDs. These includes RDD transformation and actions. I was also able to examine how and what Spark is performing behind the scenes with the DAG visualisations. Completing this project have helped me to have a better foundation in PySpark.
