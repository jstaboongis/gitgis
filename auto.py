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
    print "time to stop this program"
    threading.Timer(300, process).start()
    print "dont stop now"
    

process()



