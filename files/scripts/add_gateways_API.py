#!/usr/bin/env python
import json, requests, yaml,configparser, requests, yaml, os, sys, argparse, os.path
from pprint import pprint
from ConfigParser import ConfigParser

# to import local modules
sys.path.append('files/scripts')
import create_url


output_json =  yaml.load(open('files/json/gateways.json'))
headers = {'content-type': 'application/json'}

url= create_url.return_url()+'/gateways'


for i in output_json:
	for k in output_json[i]:
		data=json.dumps(k,ensure_ascii=False)
		new_data=data.encode("utf-8")
		r = requests.post(url,data=new_data,verify=False,headers=headers)
