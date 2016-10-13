#!/bin/bash
yum clean all && yum update -y
rm -rf /etc/sipxpbx/sipxecs-setuprc
