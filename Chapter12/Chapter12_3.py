#!/usr/bin/env python3
from elasticsearch import Elasticsearch
from datetime import datetime
import argparse
import json
import logging

# parse options
parser = argparse.ArgumentParser(description='Elasticsearch Query Options')
parser.add_argument("-i", "--index", help="index to query")
parser.add_argument("-q", "--query", help="query file")

args = parser.parse_args()


# logging
today = str(datetime.today())
logging.basicConfig(filename='elastic_query.log', level=logging.INFO)


# load elastic index and query body information
query_file = args.query
with open(query_file) as f:
    query_body = json.loads(f.read())


# Elasticsearch instance
es = Elasticsearch(['http://192.168.2.200:9200'])


# Query both index and put into dictionary
index = args.index
res = es.search(index=index, body=query_body)
print(res['hits']['total']['value'])


