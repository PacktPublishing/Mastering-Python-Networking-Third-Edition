#!/usr/bin/env python3
from elasticsearch import Elasticsearch

es_host = Elasticsearch("http://192.168.2.200/")

res = es_host.search(index="kibana*", body={"query": {"match_all": {}}})
print("Hits Total: " + str(res['hits']['total']['value']))


