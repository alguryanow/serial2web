# serial2web
Send strings from COM-port to web

internal_temp_to_serial\internal_temp_to_serial.ino - Arduino part: sample sketch
putting some strings to serial2web. As a sample source of strings from COM-port.

serial2web_concept.py - first version of server just streaming lines to web-client

serial2web_concept2.py - version of server with Server-Send Events

index.html - main page (access point) of web-server for serial2web_concept2.py

Change the following strings in serial2web_concept[2].py:

* SERIAL_PORT_NAME = 'COM7'
* SERIAL_PORT_SPEED = 115200

* WEB_SERVER_PORT = 8000



