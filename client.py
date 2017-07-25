#-*- coding: utf-8 -*-

"""
Created on 2017/7/14 22:13:31
Author: CHIFE NG
"""
import socket
import time

port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
i=0
while i<10:
    i=i+1
    time.sleep(1)
    try:
        print ('trying to connect...%d'%i)
        s.connect(('39.108.227.217',port))
        print (s.recv(1024))
        for data in [b'CHIFE',b'NG',b'WU']:
            s.send(data)
            print (s.recv(1024))
        s.send(b'exit')
        break
    except Exception:
        print ('Server port %d not connect'%port)
s.close()
