# -*- coding: cp936 -*- 
'''
Created on December 13th, 2013

Global variables in multi files

@author: Damon
'''


enc_status = {}

max_enc = 100

for i in range (101, max_enc + 101):
    enc_status[i] = 0

ipaddr = '192.168.2.'

interval = 60 * 30 #30 minutes

test_round = 1