# PySpark - Structure Streaming with PySpark

## Introduction

This project aims to explore the workings of Structured Streaming with PySpark. As there are an abundance of machine generated data from things like IoT, sensors, devices and beacons. Gaining an insight from these data is becoming more important and requires a quicker response. Streaming such analytics can therefore be a huge differentiator and can be an advantage in business. 

This project will be combining batch and real time processing to develop continuous applications. The data can be analysed by utilising Spark SQL in batch or in real time, machine learning models will be trained (with MLlib) and followed by scoring these models using Spark Streaming. 

Apache Spark has been widely adopted due to its ability to unify the disparate data processing paradigms such as Machine learning, SQL and streaming. Companies that uses this are Netflix, Uber, Pinterest etc.

The key abstraction in Structure Streaming with PySpark is a discretised stream (DStream) where it represents a stream of data that is divided up into smaller batches. As these are built on Spark's RDDs, it allows for Spark Streaming to integrate into any other of Spark's components seamlessly such as MLlib or SQL. This unification is one of the key reason of its rapid adaptation in business. It allows developers to use a single framework to perform all processing needs. In short, developers and system administrators can just focus more of their energy on developing smarter solutions/applications.

More information:
- https://www.datanami.com/2015/11/30/spark-streaming-what-is-it-and-whos-using-it/
- https://www.datanami.com/2015/10/05/how-uber-uses-spark-and-hadoop-to-optimize-customer-experience/
- https://databricks.com/session/spark-and-spark-streaming-at-netflix

## Running Spark Streaming:

Majority of this project will be ran within the System Terminals. This notebook will be used to show the screenshots of the events and its description, like how things are working.

## Breakdown of this Notebook

- Develope an understanding on DStreams
- Develope an understanding on Global Aggregations
- Overview of Structured Streaming
- Continuous Aggregations with Structured Streaming

## Summary:

From this project, I was able to gain a better understanding (although not every aspects with 100% certainty) of Spark Structured Streaming. I was to learn about the Spark SQL Engine Catalyst Optimiser and its 4 main components such as Analysis, Logical Optimisation, Physical Planning and Code generation. I have also learnt the basics of developing a continuous application with batch or real-time processing. These were conducted in two terminal windows whereby using Netcat Window and a Spark streaming window respectively. For the streaming window, I was able to create .py scripts/files to intake, process and output the incoming streamed data to be outputted as DStreams (batched processes), Global Aggregations (sum of events in a time window) and Structured Streaming (Incremental Execution plan).
