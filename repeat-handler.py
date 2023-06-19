#!/usr/bin/env python
import signal
import os
import psutil
import sys
import subprocess

def sigIntHandler(*_):
    parent = psutil.Process(os.getpid())
    print(parent.exe())
    for child in parent.children(recursive=True):
        print(child.exe())
        child.send_signal(signal.SIGKILL)

def sigTermHandler(*_):
    parent = psutil.Process(os.getpid())
    print(parent.exe())
    for child in parent.children(recursive=True):
        print(child.exe())
        child.send_signal(signal.SIGKILL)


sys.stdout = open('test.log', 'a')
sys.stderr = open('test.log', 'a')
signal.signal(signal.SIGINT, sigIntHandler)
signal.signal(signal.SIGTERM, sigTermHandler)
subprocess.run(sys.argv[1:])
