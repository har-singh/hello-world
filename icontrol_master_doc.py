#!/bin/python
# -----HS 26May21-----
# The requirement: update the Master Document. Create Master document csv via api
# To get the pool the idea was to get the bulk first and then search internally to Python. But, for now it is easier to generate get requests for each pool
# https://www.delftstack.com/howto/python/python-pretty-print-dictionary/
# the get request is not working when attaching the query with backslash (\) so for now will get everthing thing and extract the information
# https://likegeeks.com/terminating-python-scripts/

import re, json, csv, datetime, getpass, sys
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
  print('Running GET ' + request_url)
  response = requests.get(request_url, auth = HTTPBasicAuth(username, password), verify=False, headers=headers)
  if response.status_code == 200:
    print('GET request complete')  
    response_data = response.json()
    return(response_data)
  else:
    print('HTTP request error. Reason: %s; Status Code: %s') % (response.reason, response.status_code)
    quit(1)

def get_reference_path(dictionary, key_for_path):
  # https://realpython.com/python-defaultdict/
  # Data example:
  # {
  #   "name": "demo_443_pool",
  #   "membersReference": {
  #     "isSubcollection": true,
  #     "link": "https://localhost/mgmt/tm/ltm/pool/~Ficus_Prova~demo_443_pool/members?ver=14.1.4"
  #   },
  # }
  #
  value_path = ''
  if key_for_path in dictionary:
    value_url = dictionary[key_for_path]['link']
    value_path = urlparse.urlparse(value_url).path
    return(value_path)

def csv_export(data_list, column_keys, hostname):
  # Export to CSV
  #column_keys = ['name', 'destination', 'pool', 'partition']
  #
  #csv_data = [['Virtual Server Name,', 'VS Destination', 'Pool Name', 'Partition','Hostname']] # list initialized with the columns names
  csv_data = [['Virtual Server Name', 'VS Destination', 'Pool Name', 'Pool Member', 'Node Address', 'Partition', 'Hostname']] # list initialized with the columns names
  #csv_data = []
  for i in data_list:
    data = [i.get(x) for x in column_keys]
    for j in range(len(data)):
      try:
        data[j] = re.sub(r'%[0-9]+', '', data[j])   # '/Ficus_Prova/10.182.248.95%6:443'. Removes '%6'
        data[j] = re.sub(r'^/[0-9a-zA-Z_-]*/', '', data[j]) # '/Ficus_Prova/10.182.248.95%6:443'. Removes '/Ficus_Prova/'
      except:
        pass
    data.append(hostname)
    csv_data.append(data)
  #
  file_path_name = '/shared/tmp/hsingh/bigip_' + hostname + '_api_export.csv'
  with open(file_path_name, 'w') as comma_file:
    wr = csv.writer(comma_file, quoting=csv.QUOTE_ALL)
    wr.writerows(csv_data)
    print('CSV exported.')

def csv_virtual_export(device, username, password):
  keys = ['name', 'destination', 'pool', 'partition']
  csv_data = [['Virtual Server Name,', 'VS Destination', 'Pool Name', 'Partition','Hostname']] # list initialized with the columns names
  #
  virtual_data_list = get_request(device, username, password, '/mgmt/tm/ltm/virtual/')
  virtual_data_list = virtual_data_list['items']
  hostname = get_request(device, username, password, '/mgmt/tm/sys/global-settings?$select=hostname')['hostname']
  #
  csv_export(virtual_data_list, keys, hostname)

def csv_pool_member_export(device, username, password):
  keys = ['vs_name', 'vs_destination', 'pool_name', 'member_name', 'address', 'partition']
  csv_data = [['Virtual Server Name', 'VS Destination', 'Pool Name', 'Pool Member', 'Node Address', 'Partition', 'Hostname']] # list initialized with the columns names
  pool_member_data = []
  pool_dict = {}
  #
  virtual_data_list = get_request(device, username, password, '/mgmt/tm/ltm/virtual/')
  virtual_data_list = virtual_data_list['items']
  #
  pool_data_list = get_request(device, username, password, '/mgmt/tm/ltm/pool/')
  pool_data_list = pool_data_list['items']
  for pool in pool_data_list:
    pool_dict[pool['fullPath']] = pool
  #
  hostname = get_request(device, username, password, '/mgmt/tm/sys/global-settings?$select=hostname')['hostname']
  #
  for vs in virtual_data_list:
    if 'pool' in vs:
      pool_data = pool_dict[vs['pool']]
      if 'membersReference' in pool_data:
        member_path = get_reference_path(pool_data, 'membersReference')
        member_data = get_request(device, username, password, member_path)
        member_data = member_data['items']
        for member in member_data:
          member_dict = {}
          member_dict['vs_name'] = vs['name']
          member_dict['vs_destination'] = vs['destination']
          member_dict['pool_name'] = vs['pool']
          member_dict['partition'] = vs['partition']
          member_dict['member_name'] = member['name']
          member_dict['address'] = member['address']
          pool_member_data.append(member_dict)
  #
  csv_export(pool_member_data, keys, hostname)


if __name__ == "__main__":
  #
  pattern_ip = re.compile('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$') #pattern to match ip address e.g. 10.182.129.65
  pattern_comma = re.compile('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3},') # pattern to match ip address with comma e.g. 10.182.129.65
  device = [sys.argv[0]]
  #
  # Get access details
  # If no IP are provided the users will be prompted. The list can be separated by spaces or commas
  if len(sys.argv) == 1:
    device_ip = raw_input("Provide BIG-IP Management IP: ")
    device.append(device_ip)
  elif pattern_comma.match(sys.argv[1]):
    addr_list = re.split(',', sys.argv[1])
    for addr in addr_list:
      device.append(addr)
  else:
    device = sys.argv
  #
  #
  username = raw_input("Username: ")
  password = getpass.getpass("Password: ")


  for index in range(1, len(device)):
    if pattern_ip.match(device[index]):
      csv_pool_member_export(device[index], username, password)
    else:
      print('Error. ' + device[index] + ' is not an IP address.')
  
  #
  #
  # Export to CSV
#  csv_virtual_export(device, username, password)
#  csv_pool_member_export(device, username, password)
