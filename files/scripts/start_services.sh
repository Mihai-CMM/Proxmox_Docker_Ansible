#!/usr/bin/env bash

psql -U postgres SIPXCONFIG << EOF
INSERT INTO feature_global (feature_id) VALUES ('natTraversal');
INSERT INTO feature_global (feature_id) VALUES ('snmp');
INSERT INTO feature_global (feature_id) VALUES ('sipxlogwatcher');
INSERT INTO feature_global (feature_id) VALUES ('mail');
INSERT INTO feature_global (feature_id) VALUES ('ntpd');
INSERT INTO feature_global (feature_id) VALUES ('alarms');
INSERT INTO feature_local (feature_id, location_id) VALUES ('sipxdns', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('systemaudit', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('phonelog', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('ftp', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('provision', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('tftp', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('freeSwitch', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('ivr', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('moh', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('park', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('registrar', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('sipxcdr', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('sipxsqa', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('mwi', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('proxy', 1);
INSERT INTO feature_local (feature_id, location_id) VALUES ('conference', 1);

EOF

service sipxconfig restart
