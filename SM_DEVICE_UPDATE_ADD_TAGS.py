#!/usr/bin/python
# Update the information for a device in Systems Manager

import json
import time
import requests
import cred

KEY = cred.key
NETWORK_ID = cred.ht_sm_networkid
DASHBOARD = 'https://api.meraki.com/api/v0/networks/%s/sm/device/fields' % NETWORK_ID
HEADERS = {'X-Cisco-Meraki-API-Key': (KEY), 'Content-Type': 'application/json'}

DASHBOARD_TAGS = 'https://api.meraki.com/api/v0/networks/%s/sm/devices/tags' % NETWORK_ID

#SERIAL = input("What is the S/N for the device: ")
#NAME = input("What name are we giving it? ")


READFILE = open("data.txt", "r")
for line in READFILE:
    time.sleep(1)
    DATA = line.split(",")
    SERIAL = DATA[0]
    NAME = DATA[1]
    TAGS = (DATA[2].strip('\n'))
    UPDATE_JSON = {}
    UPDATE_DATA = {}
    UPDATE_DATA["name"] = NAME
    UPDATE_JSON["serial"] = SERIAL
    UPDATE_JSON["deviceFields"] = UPDATE_DATA
    UPDATE_DEVICE = requests.put(DASHBOARD, data=json.dumps(UPDATE_JSON), headers=HEADERS)
    #Update the tags on a device
    ADD_TAGS = {}
    ADD_TAGS["serial"] = SERIAL
    ADD_TAGS["updateAction"] = 'add'
    ADD_TAGS["tags"] = TAGS
    TAGS_URL = requests.put(DASHBOARD_TAGS, data=json.dumps(ADD_TAGS), headers=HEADERS)
    print(NAME)
    print(UPDATE_DEVICE.status_code)
    print(TAGS_URL.status_code)
