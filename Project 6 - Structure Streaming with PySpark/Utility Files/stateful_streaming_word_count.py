'''
    A PySpark Streaming Application - Stateful Word Counts
        FileName: stateful_streaming_word_count.py
        Project 6 - Structure Streaming with PySpark
    Used to perform global aggregations.

    for more info: https://databricks.gitbooks.io/databricks-spark-reference-applications/content/logs_analyzer/chapter1/total.html
'''

# 1 - Import the Classes and Create a local SparkContext and Streaming Context:
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# 2 - Create the Spark Context: consist of 2 working cpu threads
sc = SparkContext('local[2]', 'StatefulNetworkWordCount')

# 3 - Create a Local Streaming Context with Batch Interval of 1 second:
ssc = StreamingContext(sc, 1)

# 4 - Create a checkpoint for the Local Streaming Context:
ssc.checkpoint("checkpoint")

# 5 - User define func: create a updateFunc -> sum of the (key, value) pairs
def updateFunc(new_values, last_sum):
    return sum(new_values) + (last_sum or 0)

# 6 - Create a DStream that connects with the stream of input lines from localhost:9999 connection:
lines = ssc.socketTextStream('localhost', 9999)

# 7 - Calculate the running counts:
# for Line 1 -> Split the lines into words
# for Line 2 -> Count each of the word in each batch
# for Line 3 -> Run/apply the "updateStateByKey()" to running count
running_counts = lines.flatMap(lambda line: line.split(" "))\
    .map(lambda word: (word, 1))\
    .updateStateByKey(updateFunc)

# 8 - Print the first 10 elements of each RDD generated from the DStream to the Console:
running_counts.pprint()

# 9 - Start the Computation:
ssc.start()

# 10 - Wait for computation to terminate:
ssc.awaitTermination()