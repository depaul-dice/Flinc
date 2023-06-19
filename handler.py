#!/usr/bin/env python
import signal
import os
import psutil
import sys
import subprocess

def sigIntHandler(*_):
    print("Inside sigIntHandler")
    parent = psutil.Process(os.getpid())
    for child1 in parent.children(recursive=False):
        print("child1:", child1.exe())
        for child2 in child1.children(recursive=False):
            print("child2:", child2.exe())
            for child3 in child2.children(recursive=False):
                print("child3:", child3.exe())
                if "bin/python" in child3.exe():
                    child3.send_signal(signal.SIGINT)

def sigTermHandler(*_):
    print("Inside sigTermHandler")    
    parent = psutil.Process(os.getpid())
    for child1 in parent.children(recursive=False):
        print("child1:", child1.exe())
        for child2 in child1.children(recursive=False):
            print("child2:", child2.exe())
            for child3 in child2.children(recursive=False):
                print("child3:", child3.exe())
                if "bin/python" in child3.exe():
                    child3.send_signal(signal.SIGTERM)


sys.stdout = open('flinc.log', 'a')
sys.stderr = open('flinc.log', 'a')
signal.signal(signal.SIGINT, sigIntHandler)
signal.signal(signal.SIGTERM, sigTermHandler)
subprocess.run(sys.argv[1:])
