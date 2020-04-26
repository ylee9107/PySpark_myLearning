'''
    A PySpark Streaming Application - Word Counts
        FileName: streaming_word_count.py
        Project 6 - Structure Streaming with PySpark

'''

# 1 - Import the Classes and Create a local SparkContext and Streaming Context:
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# 2 - Create the Spark Context: consist of 2 working cpu threads
sc = SparkContext('local[2]', 'NetworkWordCount')

# 3 - Create a Local Streaming Context with Batch Interval of 1 second:
ssc = StreamingContext(sc, 1)

# 4 - Create a DStream that connects with the stream of input lines from localhost:9999 connection:
lines = ssc.socketTextStream('localhost', 9999)

# 5 - Split the lines into words:
words = lines.flatMap(lambda line: line.split(" "))

# 6 - Count each word in each batch:
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# 7 - Print the first 10 elements of each RDD generated from the DStream to the Console:
wordCounts.pprint()

# 8 - Start the Computation:
ssc.start()

# 9 - Wait for computation to terminate:
ssc.awaitTermination()