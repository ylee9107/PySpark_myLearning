# Abstracting Data with DataFrames

## Introduction:

This notebook aims to focus on furthering the understanding of PySpark fundamentals in data structures called DataFrames. Interestingly, DataFrames in PySpark takes advantage of the developments and improvements from Project Tungsten and Catalyst Optimiser.

## Project Tungsten:

The following is a direct quote from https://databricks.com/blog/2015/04/28/project-tungsten-bringing-spark-closer-to-bare-metal.html. It briefly describes the project. 

Project Tungsten will be the largest change to Spark’s execution engine since the project’s inception. It focuses on substantially improving the efficiency of memory and CPU for Spark applications, to push performance closer to the limits of modern hardware. This effort includes three initiatives:

- __Memory Management and Binary Processing__: leveraging application semantics to manage memory explicitly and eliminate the overhead of JVM object model and garbage collection.
- __Cache-aware computation__: algorithms and data structures to exploit memory hierarchy.
- __Code generation__: using code generation to exploit modern compilers and CPUs.

## Catalyst Optimiser:

The following is a direct quote from https://databricks.com/glossary/catalyst-optimizer. It briefly describes the project.

Catalyst is based on functional programming constructs in Scala and designed with these key two purposes:

- Easily add new optimization techniques and features to Spark SQL.
- Enable external developers to extend the optimizer (e.g. adding data source specific rules, support for new data types, etc.).

## Breakdown of this Notebook:
- Creating DataFrames
- Accessing underlying RDDs
- Performance optimisations
- Inferring the schema using Reflections
- Specifying the schema programmatically
- Creating a temporary Table
- Using SQL to interact with DataFrames
- Overview of the DataFrame transformations and Actions.


## Dataset:

The main dataset used here are created (contains Apple computer information). The alternative dataset used for demonstration can also be found in the following link.

Source:
- https://github.com/kavgan/spark-examples/blob/master/sample-data/description.csv

## Summary:

From this project I was able to learn and develop a better understanding of PySpark DataFrames. These includes DataFrame transformation and actions and are similar to the RDD’s transformation and actions. I was able to explore different methods of making a schema to create a DataFrame. I was also able to develop my skills in SQL queries to query the demonstration dataset using PySpark. Completing this project have helped me to have a better foundation in PySpark.
