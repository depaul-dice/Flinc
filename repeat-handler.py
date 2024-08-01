#!/usr/bin/env python
import signal
import os
import psutil
import sys
import subprocess
from sciunit2.records import ExecutionManager

def sigIntHandler(*_):
    print("Inside sigIntHandler")
    parent = psutil.Process(os.getpid())
    print("parent:", parent.exe())
    for child in parent.children(recursive=True):
        print("child:", child.exe())
        child.send_signal(signal.SIGKILL)

def sigTermHandler(*_):
    print("Inside sigTermHandler")
    parent = psutil.Process(os.getpid())
    print("parent:", parent.exe())
    for child in parent.children(recursive=True):
        print("child:", child.exe())
        child.send_signal(signal.SIGKILL)

def get_last_execution():
    em = ExecutionManager(os.path.expanduser('~') + '/sciunit/audit-kernel')
    return em.get_last_id()

print("Repeat Kernel")
sys.stdout = open('flinc.log', 'a')
sys.stderr = open('flinc.log', 'a')
signal.signal(signal.SIGINT, sigIntHandler)
signal.signal(signal.SIGTERM, sigTermHandler)

sys.argv[5] = 'e' + str(get_last_execution())
subprocess.run(sys.argv[1:])
