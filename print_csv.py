#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:44:50 2018

@author: karthik
"""

import csv

f = open('Hosts.csv')
csv_f = csv.reader(f)

for row in csv_f:
    hostname = row[1]
    nport = row[2]
    conf_file = row[3]
    print(hostname)
    print(nport)
    print(conf_file)
    