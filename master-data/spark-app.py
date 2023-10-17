from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("SampleApp").getOrCreate()

# Create a DataFrame
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["Name", "Value"])

# Show the DataFrame
df.show()

# Stop the SparkSession
spark.stop()