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

# Quickstart
```
# update paths in example.env to point to permanent ES directory and location of the input dumps
mv example.env .env
docker-compose up
```
