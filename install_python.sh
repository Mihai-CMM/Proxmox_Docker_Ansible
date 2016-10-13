#!/bin/bash
yum groupinstall -y 'development tools'
yum install -y zlib-devel bzip2-devel openssl-devel xz-libs wget curl

curl https://bootstrap.pypa.io/get-pip.py | python

pip install requests
