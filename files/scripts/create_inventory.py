#! /usr/bin/env python

import configparser, requests, yaml, os, sys, argparse
from pprint import pprint
from ConfigParser import ConfigParser
import os.path


vmIP=""
proxuser=""
proxpass=""
def readConfig(arg):
	try:
		os.path.isfile(arg)
                
		with open(arg, 'r') as stream:
			global vmIP
        		vmIP=yaml.load(stream)['vmIP']
			
			
	except:
		print "EXCEPTION::Oops!  Something must be wrong with your configuration file (./files/configuration/configuration.yml.  Try again after you check that file..."  


def readCredentials(arg):

	try:
		os.path.isfile(arg)
		with open(arg, 'r') as stream:
			global proxuser
        		proxuser=yaml.load(stream)['vmuser']
	
			
			
		with open(arg, 'r') as stream:
			global proxpass
	       		proxpass =str(yaml.load(stream)['vmpass'])
			
			
	except:
 		print "EXCEPTION::Oops!  Something must be wrong with your proxmox credential file (./files/configuration/proxcred.yml.  Try again after you check that file..." 

def createInventory():

	with open('inventory.ini', 'w') as outfile:
        	outfile.write("[proxmox]\n")
        	outfile.write(vmIP)
              	outfile.write(" ansible_ssh_user=" + "\"" + proxuser +"\"")
	      	outfile.write(" ansible_ssh_pass=" + "\"" + proxpass + "\"")



