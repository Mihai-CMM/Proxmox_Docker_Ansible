#!/bin/bash

scp root:12345678 
psql -U postgres SIPXCONFIG  -c "
