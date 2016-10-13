#! /usr/bin/env python

import requests, yaml,requests,os.path
from pyproxmox import *
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

node=''
vmid=''
username=''
password=''



def readNode(arg):

	try:
		os.path.isfile(arg)

		with open(arg, 'r') as stream:
			global node
        		node=yaml.load(stream)['node']



	except:
		print "EXCEPTION::Oops!  Something must be wrong with your configuration file ??node?? (./files/configuration/configuration.yml.  Try again after you check that file..."

       	try:
		os.path.isfile(arg)

		with open(arg, 'r') as stream:
			global vmid
        		vmid=yaml.load(stream)['vmid']



	except:
		print "EXCEPTION::Oops!  Something must be wrong with your configuration file ??vmid?? (./files/configuration/configuration.yml.  Try again after you check that file..."


def readCredentials(arg):


	try:
		os.path.isfile(arg)

		with open(arg, 'r') as stream:
			global username
        		username=yaml.load(stream)['proxuser']



	except:
		print "EXCEPTION::Oops!  Something must be wrong with your proxcred file ??username?? (./files/configuration/proxcred.yml.  Try again after you check that file..."

       	try:
		os.path.isfile(arg)

		with open(arg, 'r') as stream:
			global password
        		password=yaml.load(stream)['proxpass']



	except:
		print "EXCEPTION::Oops!  Something must be wrong with your proxcred file ??proxpass?? (./files/configuration/proxcred.yml.  Try again after you check that file..."





def startMachine():

	a = prox_auth(node,username,password)
	b = pyproxmox(a)
	print ">>>>>>Starting proxmox VM: ", vmid , ">>>>>>"
	b.startVirtualMachine(node,vmid)

def stopMachine():

	a = prox_auth(node,username,password)
	b = pyproxmox(a)
	print ">>>>>>Stopping proxmox VM: ", vmid , ">>>>>>"
	b.stopVirtualMachine(node,vmid)
