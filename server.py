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
s.bind(('0.0.0.0',9999))
s.listen(5)

# Handle a connection
def tcplink(sock,addr):
    print ("Accept new connect form %s:%s..."%addr)
    while True: 
        print ("%s:%s:"%addr)
        send=input('please input your command:')
        try:
            sock.send(send.encode())
        except Exception:
            print ('send error!!client may closed!')
            break
        if send=='':
            print ('---doesn\'t recevie empty data---')
        else:
            recv=sock.recv(1024)
            if recv=='exit' or not recv: 
                print ('%s:%s closed'%addr)
                break
            else:
                print (recv)
    sock.close()
# LOOP
while True:
    print ('Waiting for connection...')
    # recvice a new connection
    sock,addr=s.accept()

    # creat a new thread to handle connection
    t=threading.Thread(target=tcplink(sock,addr)) 

