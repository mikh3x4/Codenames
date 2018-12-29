
"""
This is a simple library to enable communication between different processes (potentially on different machines) over a network using UDP. It's goals a simplicity and easy of understanding and reliability

mikadam@stanford.edu
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import socket
import struct
from collections import namedtuple

import json

from sys import version_info
if version_info[0] < 3:
    from time import time as monotonic
else:
    from time import monotonic

timeout = socket.timeout

MAX_SIZE = 65507


def get_broadcast_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    ip_list = ip.split('.')
    ip_list[-1] = '255'
    return '.'.join(ip_list)


class Publisher:
    def __init__(self, port):
        """ Create a Publisher Object

        Arguments:
            port         -- the port to publish the messages on
            local        -- if True publisher will only publish to only this computer but it will 
                            work even if the computer isn't connected to a rover network. Useful for
                            development
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.broadcast_ip = get_broadcast_ip()

        self.sock.settimeout(0.2)
        self.sock.connect((self.broadcast_ip, port))

        self.port = port

    def send(self, obj):
        """ Publish a message. The arguments are the message fields """
        msg = json.dumps(obj)
        assert len(msg) < MAX_SIZE, "Encoded message too big!"
        self.sock.send(msg)

    def __del__(self):
        self.sock.close()


class Subscriber:
    def __init__(self, port, timeout=0.2):
        """ Create a Subscriber Object

        Arguments:
            port         -- the port to listen to messages on
            timeout      -- how long to wait before a message is considered out of date
        """
        self.max_size = MAX_SIZE

        self.port = port
        self.timeout = timeout

        self.last_data = None
        self.last_time = float('-inf')

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, "SO_REUSEPORT"):
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        self.sock.settimeout(timeout)
        self.sock.bind(("", port))

    def recv(self):
        """ Receive a message. Returns a namedtuple matching the messages fieldnames 
            If no message is received before timeout it raises a UDPComms.timeout exception"""

        self.last_data, address = self.sock.recvfrom(self.max_size)
        self.last_time = monotonic()
        return json.loads(self.last_data)

    def get(self):
        """ Returns the latest message it can without blocking. If the latest massage is 
            older then timeout seconds it raises a UDPComms.timeout exception"""
        try:
            self.sock.settimeout(0)
            while True:
                self.last_data, address = self.sock.recvfrom(self.max_size)
                self.last_time = monotonic()
        except socket.error:
            pass
        finally:
            self.sock.settimeout(self.timeout)

        current_time = monotonic()
        if (current_time - self.last_time) < self.timeout:
            return json.loads(self.last_data)
        else:
            raise socket.timeout("timeout=" + str(self.timeout) + \
                                 ", last message time=" + str(self.last_time) + \
                                 ", current time=" + str(current_time))

    def __del__(self):
        self.sock.close()


if __name__ == "__main__":
    msg = 'very important data'

    a = Publisher(1000)
    a.send( {"text": "magic", "number":5.5, "bool":False} )
