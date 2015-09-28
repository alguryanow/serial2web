# serial2web
Send strings from COM-port to web for multiple clients using ZMQ, Flask and AJAX

First version with ugly page, without ZMQ, Flask and AJAX see in rev. 9f36c242e2cb

index.html - demo page builded with bootstrap, jQuery and AJAX

serial_to_zmq.py + zmq2web_using_flask.py - two parts of backend:  
+    serial_to_zmq.py - reads _strings_ from serial (COM-port) and publishes them to ZMQ
+    zmq2web_using_flask.py - uses Flask to process http-requests and servicing web-clients
 
master.py - master script that parses command line arguments and launches both parts of backend

master.spec - command file for pyInstaller 2.1

hook-zmq.py - patched file from pyInstaller 2.1 module for ZMQ 14.0+  
                See: https://github.com/pyinstaller/pyinstaller/pull/110/files

serial_to_zmq_demo.py + zmq_test_client.py - demonstration of ZMQ's beauty