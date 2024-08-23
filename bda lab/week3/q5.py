from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("WordCount Example") \
    .getOrCreate()

# Create a SparkContext from SparkSession
sc = spark.sparkContext

# Sample data
data = [
    "Hello world",
    "Hello from PySpark",
    "PySpark is great for big data",
    "Hello big data world"
]

# Parallelize the data to create an RDD
rdd = sc.parallelize(data)

# Perform WordCount
word_counts = (rdd.flatMap(lambda line: line.split(" "))  # Split each line into words
                  .map(lambda word: (word, 1))           # Map each word to (word, 1)
                  .reduceByKey(lambda a, b: a + b))     # Reduce by key (sum the counts)

# Collect the results
results = word_counts.collect()

# Print the results
print("Word counts:")
for word, count in results:
    print(f"{word}: {count}")

# Stop the SparkSession
spark.stop()
