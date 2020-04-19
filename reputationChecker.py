# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:22:24 2020

@author: vishal.bhaskar

Input: 
List of IPs to check against abuseIPDB's database
API key for abuseIPDB

Output: 
IPs which have a bad reputation score of more than 75% refer"https://www.abuseipdb.com/faq.html#confidence"

"""
import requests
import json
import time

response = ''
filename = input("enter path to IP list eg c://IPs.txt : ")
with open(filename) as f:
    IPs = f.read().splitlines()
APIkey = input ("enter API key for abuseIPDB : ")
print (IPs)
url = 'https://api.abuseipdb.com/api/v2/check'

for i in IPs:
    
    querystring = {
        'ipAddress': i,
        'maxAgeInDays': '90', 
        
    }
    
    headers = {
        'Accept': 'application/json',
        'Key': APIkey
    }
    time.sleep(0.5) #Added sleep for API call
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)#dict
    if int(decodedResponse['data']['abuseConfidenceScore']) > 75:
        print (json.dumps(decodedResponse, sort_keys=True, indent=4)) 
        
