# -*- coding: utf-8 -*-

import zmq
import time
import serial

_SERIAL_PORT_NAME = 'COM7'
_SERIAL_PORT_SPEED = 115200

_ZMQ_PUB_ADDR = 'tcp://*:12345'

def work( serial_port_name, serial_port_speed, zmq_pub_addr ):

    context = zmq.Context.instance()

    pub_sock = context.socket(zmq.PUB)
    pub_sock.bind( zmq_pub_addr )

    ser = serial.Serial(serial_port_name, serial_port_speed, timeout=0.03)
    
    count=0
    while True:
        line = get_full_line_from_serial(ser)
        if line is not None:
            count += 1
            print line.decode('utf-8')
            pub_sock.send( time.strftime( '%Y.%m.%d %H:%M:%S' ) + ': строка № %d' % count + '<br>' +  line )


_captured = ''
def get_full_line_from_serial(ser):
    """ returns full line from serial or None 
        Uses global variable '_captured'
    """
    global _captured
    part = ser.readline()
    if part:
        _captured += part
        parts = _captured.split('\n', 1);
        if len(parts) == 2:
            _captured = parts[1]
            return parts[0]
            
    return None
    

if __name__ == '__main__':
    work( _SERIAL_PORT_NAME, _SERIAL_PORT_SPEED, _ZMQ_PUB_ADDR )