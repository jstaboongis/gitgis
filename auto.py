import threading
import os, subprocess

def process():
    print "working"
    cmds = 'cd C:\Users\WORK\Documents\GitHub\gitgis'
    subprocess.call(cmds, shell=True)
    cmds = 'python sample2.py'
    subprocess.call(cmds, shell=True)
    cmds = 'git add -A'
    subprocess.call(cmds, shell=True)
    cmds = 'git commit -m "some message"'
    subprocess.call(cmds, shell=True)
    cmds = 'git push'
    subprocess.call(cmds, shell=True)
    print "waiting"
    threading.Timer(60, process).start()
    

process()



