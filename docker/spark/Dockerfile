# Use Ubuntu (latest) as the base image
FROM ubuntu:latest

# Set environment variables
ENV SPARK_VERSION="3.5.0" \
    HADOOP_VERSION="3"

# Update system packages and install necessary tools
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y openjdk-11-jdk wget python3.11 python3-pip

# Setting python 3.11 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Install necessary Python libraries
RUN pip3 install pandas numpy scikit-learn matplotlib pyspark jupyterlab

# Download and install Apache Spark
RUN wget https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar -zxvf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz -C /opt && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz

# Set Spark home and update PATH
ENV SPARK_HOME="/opt/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION"
ENV PATH="$PATH:$SPARK_HOME/bin"

# Settings to use Jupyter notebooks with Spark
ENV PYSPARK_PYTHON=/usr/bin/python3
ENV PYSPARK_DRIVER_PYTHON='jupyter'
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --port=8889'