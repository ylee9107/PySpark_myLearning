# Installing GraphFrames:

This installation is taken from https://github.com/graphframes/graphframes/issues/267, and https://github.com/graphframes/graphframes/issues/104.

## Requirements:
- GraphFrames download ZIP file: Version 0.7.0-spark2.4-s_2.11
- Spark 2.4.5
- macOS latest version

## Step-by-Step:

__Step 1__ -  Go to https://spark-packages.org/package/graphframes/graphframes and download the “ZIP” file of the version 0.7.0-spark2.4-s_2.11 . Note that this will be saved to your downloads folder. Next, rename the file as “graphframes-0.7.0-spark2.4-s_2.11”. Once done, move this folder to your spark directory. In my case it was /opt/spark/ .

__Step 2__ - As the file is in the spark directory, open Terminal and navigate to the graphframes folder, by typing in: cd /opt/spark/graphframes-0.7.0-spark2.4-s_2.11

Next, is to type in: build/ set assembly
This will compile the jar file required from the folder. Note, this will take a long time to run.

__Step 3__ -  Copy the necessary files to the project folder, in this case is: Project 8 - GraphFrames_Graph Theory with PySpark . This is where a copy of the JAR file will be placed as well as the graphframes python folder.

Note: <graphframes path>  is /opt/spark/graphframes-0.7.0-spark2.4-s_2.11

To do this in Terminal: 

cd <project path>
cp <graphframes path> /graphframes-0.7.0-spark2.4-s_2.11/target/scala-2.11/graphframes-assembly-0.7.0-spark2.4.jar .
cp -r  <graphframes path>/python/graphframes .

__Step 4__ -  Start the notebook
In Terminal type in: pyspark --master local --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11

Following this, you will get an error “error in set-chain” or something similar. This means that you need to copy the graphframes JAR file from .ivy2/jars directory.

__Step 5__ -  Copy JAR file from .ivy2/jars to /opt/spark/jars

The JAR file from .ivy2/jars should look like -> graphframes_graphframes-0.7.0-spark2.4-s_2.11.jar and this is the file that you’ll need to copy.

To do this in Terminal, type in: cp .ivy2/jar/graphframes_graphframes-0.7.0-spark2.4-s_2.11.jar /opt/spark/jars

__Step 6__ - Launch PySpark again.

In Terminal, Type in:  pyspark --master local --packages graphframes:graphframes:0.7.0-spark2.4-s_2.11

__Step 7__ - Add the following line of code before importing Graphframes

So in Jupiter Notebook:

sc.addPyFile('/opt/spark/jars/graphframes_graphframes-0.7.0-spark2.4-s_2.11.jar')

Then:

from graphframes import *

DONE. This should be working now.
