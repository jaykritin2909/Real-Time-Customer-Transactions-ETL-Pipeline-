# Real-Time-Customer-Transactions-ETL-Pipeline-
Built a real-time ETL pipeline using Kafka and PySpark to process simulated customer transactions and store them in AWS S3/MinIO in Parquet format. Containerized with Docker for easy setup, showcasing streaming data ingestion, transformation, and cloud storage integration.

# Real-Time Customer Transactions ETL Pipeline
A beginner-to-intermediate level data engineering project that simulates customer transaction streams using Kafka, processes them in real-time using PySpark Structured Streaming, and stores the results in AWS S3 or MinIO.

## Tech Stack
- Apache Kafka (stream ingestion)
- PySpark (real-time processing)
- AWS S3 / MinIO (data lake)
- Docker Compose (local setup)

## Features
- Simulates transaction events from a Python producer
- Real-time parsing and transformation of data in Spark
- Writes processed data to object storage
- Easily switch between local MinIO and AWS S3

## How to Run
(Instructions for docker-compose up, producer run, and spark submit)
