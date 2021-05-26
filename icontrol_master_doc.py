#!/bin/python
# -----HS 26May21-----
# The requirement: update the Master Document. Create Master document csv via api
# To get the pool the idea was to get the bulk first and then search internally to Python. But, for now it is easier to generate get requests for each pool
# https://www.delftstack.com/howto/python/python-pretty-print-dictionary/
# the get request is not working when attaching the query with backslash (\) so for now will get everthing thing and extract the information

import re, json, csv, datetime, getpass
import requests
from requests.auth import HTTPBasicAuth
import urlparse

def bigip_object(i):
  # https://data-flair.training/blogs/python-switch-case/
  switcher = {
    'virtual' : '/mgmt/tm/ltm/virtual/',
    'pool' : '/mgmt/tm/ltm/pool/',
    'hostname' : '/mgmt/tm/sys/global-settings?$select=hostname'
  }
  return switcher.get(i, 'Invalid object. Possible values: virtual, pool, hostname. You provided: ' + i)

def get_request(device, username, password, url_path):
  headers = {"Content-Type": "application/json"}
  request_url = 'https://' + device + url_path
  #
  print('Running GET request...')
  response = requests.get(request_url, auth = HTTPBasicAuth(username, password), verify=False, headers=headers)
  print('GET request complete')  
  #
  response_data = response.json()
  return(response_data)

def csv_export(virtual_data_list, hostname):
  # Export to CSV
  keys = ['name', 'destination', 'pool', 'partition']
  #
  csv_data = [['Virtual Server Name,', 'VS Destination', 'Pool Name', 'Partition','Hostname']] # list initialized with the columns names
  for i in virtual_data_list:
    data = [i.get(x) for x in keys]
    for j in range(len(data)):
      try:
        data[j] = re.sub(r'%[0-9]+:', ':', data[j])   # '/Ficus_Prova/10.182.248.95%6:443'. Removes '%6'
        data[j] = re.sub(r'^/[a-zA-Z_]*/', '', data[j]) # '/Ficus_Pova/10.182.248.95%6:443'. Removes '/Ficus_Imp/'
      except:
        pass
    data.append(hostname)
    csv_data.append(data)
  #
  with open('/shared/tmp/hsingh/virtual_server_api_export.csv', 'w') as comma_file:
    wr = csv.writer(comma_file, quoting=csv.QUOTE_ALL)
    wr.writerows(csv_data)
    print('CSV exported.')

if __name__ == "__main__":
  device = raw_input("Provide BIG-IP Management IP: ")
  user = raw_input("Username: ")
  password = getpass.getpass("Password: ")
  # Get virtual server dump
  virtual_data_list = get_request(device, user, password, '/mgmt/tm/ltm/virtual/')
  virtual_data_list = virtual_data_list['items']
  #
  # Get hostname
  hostname = get_request(device, user, password, '/mgmt/tm/sys/global-settings?$select=hostname')['hostname']
  #
  # Export to CSV
  csv_export(virtual_data_list, hostname)
