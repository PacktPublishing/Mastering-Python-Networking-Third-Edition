#!/usr/bin/env python3
import json
import boto3

region = 'us-east-1'
vpc_name = 'mastering_python_networking_demo'

ec2 = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2')


filters = [{'Name': 'tag:Name', 'Values': [vpc_name]}]

vpcs = list(ec2.vpcs.filter(Filters=filters))

for vpc in vpcs:
    print(vpc.id)
    response = client.describe_vpcs(
                 VpcIds=[vpc.id]
                )
    print(json.dumps(response, sort_keys=True, indent=4))


