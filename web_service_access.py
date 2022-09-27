# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:45:47 2021

@author: oguzhan.alptekin
"""

import httplib2
import re
h = httplib2.Http()
h.follow_all_redirects = True
headers = {'Content-Type': 'text/xml; charset=utf-8'}

#put your xml here
body    = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <Get_enVision_Version xmlns="http://tempuri.org/" />  </soap:Body>

</soap:Envelope>
"""

uri     = "put asmx url here"
resp, content = h.request(uri, "POST", body=body3, headers=headers)

print(content.decode())
root = content.decode()
print('-'*30)
