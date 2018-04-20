#!/usr/bin/env python
"""
Check to see if an process is running. If not, restart.
Run this in a cron job
"""
import os
import globals

globals.init()

process_name= "program.py" # change this to the name of your process
tmp2 = os.popen("ps -Af").read()

if process_name not in tmp2[:] and globals.auto_program:
    newprocess="nohup python %s/%s &" % (globals.install_directory, process_name)
    os.system(newprocess)
