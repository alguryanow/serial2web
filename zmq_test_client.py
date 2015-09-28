import zmq

ZMQ_SUB_ADDR = 'tcp://localhost:12345'

context = zmq.Context.instance()
zmq_sub_sock = context.socket(zmq.SUB)
zmq_sub_sock.setsockopt(zmq.SUBSCRIBE, '')
zmq_sub_sock.connect( ZMQ_SUB_ADDR )

poller = zmq.Poller()
poller.register( zmq_sub_sock, zmq.POLLIN )

while True:

    socks = dict(poller.poll(timeout=5000))
    if zmq_sub_sock in socks:
        print zmq_sub_sock.recv()
    else:
        print 'No data within 5 sec'
