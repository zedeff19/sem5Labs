from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("RecommendationSystem") \
    .getOrCreate()

# Load the dataset
# Assuming you have a dataset file named 'ratings.csv' with columns: userId, movieId, rating, timestamp
file_path = "ratings.csv"
data = spark.read.csv(file_path, header=True, inferSchema=True)

# Display the schema and first few rows
data.printSchema()
data.show(5)
