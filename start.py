#! /usr/bin/env python

#Created by Mihai for QA and for fun
#this is the main entry point for configuring and populating a full openuc server on proxmox
#for how to use -README and blog entry on ezuce.com or follow code it is commented:)
#you need python and pip installed
#you need to ssh-copy-id for the ip of template you use centos/uniteme

try:
 import pip
except ImportError, e:
 pass # pip module doesn't exist, deal with it.


#Step1 Create an inventory.ini file to be used by Ansible
# we need to import a few python modules first


import sys,requests,os
sys.path.append('files/scripts')  # needed to import local modules in that path
import create_inventory , start_proxmox_machine
create_inventory.readConfig("files/configuration/configuration.yml")
create_inventory.readCredentials("files/configuration/proxcred.yml")
create_inventory.createInventory()

#Step 2 make sure pypromox (proxmox API wrapper is installed) on the current machine

try:
        from pyproxmox import *
except ImportError:
        pip.main(['install', '--user', 'pyproxmox'])
        from pyproxmox import *


#Step 3 prompt user for upgrade or install
os.system('clear')
action = raw_input('Do you want to Upgrade/Install/Stop or Populate a new uniteme machine? Answer with Upgrade/Install/Stop/Populate\n')
action=action.lower()

if action == "install":

#	- Start proxmox vm with proxmox API call ----
	start_proxmox_machine.readCredentials("files/configuration/proxcred.yml")
	start_proxmox_machine.readNode("files/configuration/configuration.yml")
	start_proxmox_machine.startMachine()

#	- Run ansible playbook to install openuc ----
	os.system('ansible-playbook install.yml')



elif action == "upgrade":
	#	- Start proxmox vm with proxmox API call ----
    start_proxmox_machine.readCredentials("files/configuration/proxcred.yml")
    start_proxmox_machine.readNode("files/configuration/configuration.yml")
    start_proxmox_machine.startMachine()
    #	- Run ansible playbook to upgrade openuc ----
    os.system('ansible-playbook upgrade.yml')


elif action == "stop":
	#	- Stopping proxmox vm with proxmox API call ----
    start_proxmox_machine.readCredentials("files/configuration/proxcred.yml")
    start_proxmox_machine.readNode("files/configuration/configuration.yml")
    start_proxmox_machine.stopMachine()
    exit()

elif action == "populate":
    os.system('ansible-playbook populate.yml')
    exit()

else:
	print "You can only chose install;upgrade or stop!!!"
	exit()

action2 = raw_input('Do you want to setup your server? Y/N\n')
action2=action2.lower()
if action2 == 'y':
    os.system('ansible-playbook populate.yml')
else:
    exit()
