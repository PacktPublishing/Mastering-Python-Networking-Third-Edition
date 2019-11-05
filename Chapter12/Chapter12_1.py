#!/usr/bin/env python3
import requests

def current_indices_list(es_host, index_prefix):
    current_indices = []
    http_header = {'content-type': 'application/json'}
    response = requests.get(es_host + "/_cat/indices/" + index_prefix + "*", headers=http_header)
    for line in response.text.split('\n'):
        if line:
            current_indices.append(line.split()[2])
    return current_indices

if __name__ == "__main__":
    es_host = 'http://192.168.2.200:9200'
    indices_list = current_indices_list(es_host, 'kibana')
    print(indices_list)

