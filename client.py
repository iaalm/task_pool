#!/usr/bin/python3 

import zmq

def send_task(endpoint,cmd):
    ct = zmq.Context()
    socket = ct.socket(zmq.PUSH)
    socket.connect(endpoint)
    socket.send_unicode(cmd)

if __name__ == '__main__':
    send_task('tcp://localhost:5050','ls')
