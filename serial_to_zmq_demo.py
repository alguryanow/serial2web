# -*- coding: utf-8 -*-

import zmq
import time

ZMQ_PUB_ADDR = 'tcp://*:12345'

context = zmq.Context.instance()

pub_sock = context.socket(zmq.PUB)
pub_sock.bind( ZMQ_PUB_ADDR )



count = 0
def get_full_line_from_serial():
    """ returns full line from serial or None 
        Uses global variables 'ser' and 'captured'
    """
    global count
    
    count += 1
    return time.strftime( '%Y.%m.%d %H:%M:%S' ) + ': string N %d' % count


while True:
    line = get_full_line_from_serial()
    print line
    pub_sock.send( line )
    time.sleep(1)