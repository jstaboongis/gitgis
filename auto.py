import threading
import os, subprocess
import time
global counter
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
    print "dont stop now"

    
while True:
    time.sleep(5)
    process()
    
process()



