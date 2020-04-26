'''
    A PySpark Streaming Application - Structured Word Counts
        FileName: structured_streaming_word_count.py
        Project 6 - Structure Streaming with PySpark
    Used to perform global aggregations but represent it in a structured way like a DataFrame.

    for more info:
'''

# 1 - Import the Classes and Create a local SparkContext and Streaming Context:
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

# 2 - Define the Spark session:
spark = SparkSession.builder.appName("StructuredNetworkWordCount").getOrCreate()

# 3 - Create a DataFrame from the incoming stream of input lines from localhost:9999 connection:
lines = spark.readStream.format('socket').option('host', 'localhost').option('port', 9999).load()

# 4 - Split the input lines into individual words:
words = lines.select(
    explode(split(lines.value, ' ')).alias('word')
)

# 5 - Calculate the running counts of the words:
wordCounts = words.groupBy('word').count()

# 6 - Begin running the query that will print out the running counts to the Console:
query = wordCounts.writeStream.outputMode('complete').format('console').start()

# 7 - Wait for computation to terminate:
query.awaitTermination()