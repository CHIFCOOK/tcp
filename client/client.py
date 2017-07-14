#-*- coding: utf-8 -*-

"""
Created on 2017/7/14 22:13:31
Author: CHIFE NG
"""
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',9999))

print (s.recv(1024))

for data in [b'CHIFE',b'NG',b'WU']:
    s.send(data)
    print (s.recv(1024))

s.send(b'exit')
s.close()