#!/usr/bin/env python3

import os
import operator
import csv

try:
    file = open('syslog.log')
except FileNotFoundError as e:
    print("The file was not found.")
    print(e)
for line in file:
    print(line)
    