# PySpark - Machine Learning with ML Module

## Introduction

In the previous Project 4, the topics covered were from the MLlib Module, however this has be deprecated recently. Therefore in this project 5, the currently support machine learning module will be explored and is called the ML module. Similar to the MLlib, this ML module consists of a wide variety of machine learning models, with the exception that it operates on Spark DataFrames. This also means that it can leverage the tungsten execution optimisations. 

## Breakdown of this Notebook

- Transformers introduction
- Estimators introduction
- Pipelines introduction
- Selecting the most predictable features
- Predicting forest coverage types
- Estimating forest elevations
- Clustering forest cover types
- Tuning Hyperparameters
- Extracting features from text
- Discretising continuous variables
- Standardising continuous variables
- Topic Mining

## Dataset:

The dataset used for this project is the forest cover type dataset. It is used to predict the forest cover type from cartographic variables, meaning that there is no remote sensed data. The forest area included in this dataset are the four wilderness areas (Rawah (area 1), Neota (area 2), Comanche Peak (area 3), Cache la Poudre (area 4)) that is located in Roosevelt National Forest of Northern Colorado.

Source: https://archive.ics.uci.edu/ml/datasets/covertype or https://www.kaggle.com/uciml/forest-cover-type-dataset

## Summary:

From this project, I learnt how to implemnent data processing and model training into pipelines to streamline the process. I was also able to implement feature extraction that contributed more predictive power to the model. During this project, several models were implemented for classification, regression and clustering. Each of these models were also evaluated and compared on its performance. I was also able to learn more about treating continuous variables, by discretising or standardising them, and its drawbacks in modeling. Lastly, I was able to gain an introduction into topic mining with LDA on text data, the preprocessing requirements when deaaling with text data.
