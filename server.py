#-*- coding: utf-8 -*-

"""
Created on 2017/7/14 21:51:31
Author: CHIFE NG
"""

import socket
import threading
import time
import os


# Creat Socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Listen Port
s.bind(('127.0.0.1',9999))
s.listen(5)
print ('Waiting for connection...')

# Handle a connection
def tcplink(sock,Saddr):
    print ("Accept new connect form %s:%s..."%addr)
    sock.send(b"Welcome!!")
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send(b"Hello,%s!"%data)
    sock.close()
    print ('Connection from %s:%s closed.'%addr)


# LOOP
while True:
    # recvice a new connection
    sock,addr=s.accept()

    # creat a new thread to handle connection
    t=threading.Thread(target=tcplink(sock,addr))
  

os.system('pause')