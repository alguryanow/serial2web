# -*- coding: utf-8 -*-

from multiprocessing import Process, freeze_support
import serial_to_zmq
import zmq2web_using_flask
import time


def main():
    args = get_command_line_params()
    
    p1 = Process( target=serial_to_zmq.work, args=(args.serial_port_name, args.serial_port_speed, args.zmq_pub_addr) )
    p1.start()
    
    p2 = Process(target=zmq2web_using_flask.work, args=(args.zmq_sub_addr,))
    p2.start()    
    
    print 'Press Ctrl+C to stop...',
    while True:
        time.sleep(10)
    
    
def get_command_line_params():
    import argparse

    parser = argparse.ArgumentParser(description="Start 'serial_to_zmq' and 'zmq2web_using_flask'")
    parser.add_argument('-n', '--serial-port-name', metavar='', type=str, default='COM1',
                        help='name of Serial (COM-) port, e.g. COM7 or /dev/ttyS7')
    parser.add_argument('-b', '--serial-port-speed', metavar='', type=int, default=9600,
                        help='baudrate')
    parser.add_argument('-p', '--zmq-pub-addr', metavar='',  type=str, default='tcp://*:12345',
                        help="ZMQ-address of PUB socket that will be used by 'serial_to_zmq' to publish readed data")
    parser.add_argument('-s', '--zmq-sub-addr', metavar='',  type=str, default='tcp://localhost:12345',
                        help="ZMQ-address of SUB socket that will be used by 'zmq2web_using_flask' to listen for data published by 'serial_to_zmq' readed from serial (COM-port)")

    args = parser.parse_args()

    return args
    
if __name__ == '__main__':
    freeze_support()       #-- hack for multiprocessing module while running inside pyinstaller. See
                           #-- http://stackoverflow.com/questions/11802438/multiprocessing-runs-new-instances-of-the-main-window-when-frozen-as-an-executab
    main()
