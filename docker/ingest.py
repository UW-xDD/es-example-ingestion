import glob
import json
import elasticsearch as es
from elasticsearch import helpers

es_client = es.Elasticsearch(["es01:9200"])

# TODO: POST setup.json if index doesn't exist.
if not es_client.indices.exists("articles"):
    body = json.load(open("setup.json"))
    es_client.indices.create("articles", body)


N=100
body = []
for f in glob.glob("/input/articles_v6.json.split-*"):
    print(f)
    with open(f, "r") as fin:
        n=0
        for line in fin:
            doc = json.loads(line)
            body.append({'_index': "articles", '_id': doc['_id'], "_source" : doc['_source']})
            if "abstract" in doc["_source"] and doc["_source"]['abstract'] == {}:
                doc["_source"]["abstract"] = ''
            if len(body) == N:
                n+=N
                print(n)
                try:
                    es.helpers.bulk(es_client, body, request_timeout=30, max_retries=5, max_chunk_bytes=50)
                except es.exceptions.ConnectionTimeout:
                    print("!!WARNING!! - Timeout indexing documents! Skipping this chunk.")
                body = []

response = es_client.bulk(body=body)

