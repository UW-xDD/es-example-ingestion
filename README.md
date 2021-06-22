# Overview
This repo holds a simple way to quickly spin up an ES instance and ingest sample
xDD documents, creating a local development instance for exploration. This instance
has analyzers and field definitions identical to that of the production xDD instance.

Requirements:
docker-compose
Sample data

A `.env` file must be created defining 
1. A local directory to permanently store the ES data2
2. The local directory holding the input files
An `example.env` file is included with sample definitions.

Elasticsearch will start up in a docker container, and an ingest process will
also start up, wait for ES to become available, create the index, and ingest
the example data. By default, port 9200 on the localhost is forwarded to the ES
port (9200) within the container, to allow easy querying from the host machine.

**NOTE** - this is not a production-ready, secure setup. It is meant for quick
explorations and experimentation.

# Quickstart
```
# update paths in example.env to point to permanent ES directory and location of the input dumps
mv example.env .env
docker-compose up
```
