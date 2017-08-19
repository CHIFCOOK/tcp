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
    while True: 
        send=input('%s:%s>>'%addr)
        try:
            sock.send(send.encode())
        except Exception:
            print ('send error!!client may closed!')
            break
        if send=='':
            print ('')
            print ('---doesn\'t recevie empty data---')
            print ('---type \'help\' or \'?\' for help---')
            print ('')
        elif send=='help' or send=='?':
            print ('')
            print ('    shut        --to shutdown current client\'s computer')
            print ('    EXIT        --to disconnect current client')
            print ('')
            print ('    help,?      --show this page')
            print ('')
        else:
            recv=sock.recv(1024)
            if recv==b'exit' or not recv: 
                print ('%s:%s closed!'%addr)
                break
            else:
                print (recv)
# LOOP
while True:
    print ('')
    print ('Waiting for connection...')
    print ('(Press \'ctrl\'+\'c\' to interrupt!!)')
    # recvice a new connection
    print ('')
    sock,addr=s.accept()
    print ("Accept new connect form %s:%s..."%addr)
    print ('')
    # creat a new thread to handle connection
    t=threading.Thread(target=tcplink(sock,addr)) 
    sock.close()
