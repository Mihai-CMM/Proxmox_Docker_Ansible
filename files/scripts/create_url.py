#!/usr/bin/env python
import json, requests, yaml,configparser, requests, yaml, os, sys, argparse, os.path
from pprint import pprint
from ConfigParser import ConfigParser

vmIP=''
superadmin=''
vmpass=''

def return_ip ():
    raw_config_settins= open('files/configuration/configuration.yml', 'r')
    config_settings = yaml.safe_load(raw_config_settins)
    vmIP = str(config_settings['vmIP'])
    return vmIP

def return_superadmin ():
    raw_cred_settings = open('files/configuration/proxcred.yml','r')
    cred_settings = config_settings = yaml.safe_load(raw_cred_settings)
    superadmin = str(cred_settings['superadmin'])
    return superadmin

def return_superadmin_pass():
    raw_cred_settings = open('files/configuration/proxcred.yml','r')
    cred_settings = config_settings = yaml.safe_load(raw_cred_settings)
    vmpass = str(cred_settings['vmpass'])
    return vmpass

def return_url():
    url = "https://"+return_superadmin()+":"+return_superadmin_pass()+"@"+return_ip()+"/sipxconfig/api"
    return url
