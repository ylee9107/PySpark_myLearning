# PySpark - Preparing the Data For Modeling

## Introduction

This project aims to explore the methods for preparing the dataset for modeling purposes. It is important to note that any dataset is dirty until proven otherwise and that it should be proven to be sufficiently clean before using it. However, no dataset can be entirely clean. Below will list some of the problems that can occur in a dataset. Majority of the time, 80% of the work is getting familiar and cleaning up the dataset. The remaining 20% would be building the model.

For this project, the dataset used will only consist of 22 records, as this is to get a feel for data cleaning with PySpark and should be transferable to other datasets.

## Problems that a Dataset can have:
- __Duplicated Observations__: These types of duplication comes from systemic and operator's faults.
- __Missing Observations__: These types of errors can come about due to sensor problems, data corruption or unwilling participant that would not provide answers.
- __Anomalous Observations__: Observations that stands out when compared to the rest of the dataset. Like Outliers.
- __Encoding__: This is when text fields are not normalised, in different languages, gibberish text inputs, or when date and date time fields were not encoded similarly.
- __Untrustworthy answers__: These are true when it comes to surveys. When the response is a lie for any number of reasons. This type is much harder to work with and clean up.


## Breakdown of this Notebook

- Handling Duplicates in data records
- Handling missing observations in dataset
- Handling outliers
- Exploring the descriptive statistics
- Computing Correlations
- Drawing Histograms to describe the data
- Visualising the interactions between features

## Dataset:

The main dataset used here was self generated and can be seen within the Notebook file.

## Summary:

From this project I was able to learn and develop a better understanding of data preparation, cleaning and visualisation with PySpark. These also includes on how to deal with problematic dataset sets. finding features that are useful and correlating them.
