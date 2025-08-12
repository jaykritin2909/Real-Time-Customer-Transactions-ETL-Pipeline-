from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# Create Spark session
spark = SparkSession.builder \
    .appName("RealTimeCustomerTransactionsETL") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Kafka topic & server
kafka_bootstrap = "kafka:9092"
topic = "transactions"

# Define schema for transaction data
schema = StructType() \
    .add("customer_id", StringType()) \
    .add("product", StringType()) \
    .add("amount", DoubleType()) \
    .add("timestamp", StringType())

# Read from Kafka
df_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap) \
    .option("subscribe", topic) \
    .load()

# Parse value as JSON
df_parsed = df_raw.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Write to S3/MinIO in parquet format
output_path = "s3a://transactions-data/processed"

query = df_parsed.writeStream \
    .format("parquet") \
    .option("path", output_path) \
    .option("checkpointLocation", "/tmp/checkpoints") \
    .outputMode("append") \
    .start()

query.awaitTermination()
