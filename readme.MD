# Spark Lab
The purpose of this Docker file and compose is to have a self contained environment where a developer can practice their PySpark skills.

# Instructions

- Install Docker Desktop (if not already installed)
- Clone this repository

**(ON VS CODE)**

- Open a terminal
- Change directory to docker/spark
- docker compose build
- docker compose --env-file spark.env up

**(ON YOUR BROWSER)**

- Spark Master GUI http://localhost:8080
- Spark Worker GUI http://localhost:8081
- Spark Application GUI http://localhost:4040
- Jupyter Notebook Lab http://localhost:8888
