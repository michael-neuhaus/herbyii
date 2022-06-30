#!/bin/sh
cd / 
cd /home/pi/HerbyBackup
sudo bash -c '/usr/bin/python3 /home/pi/HerbyBackup/herby.py > /home/pi/HerbyBackup/startup.log 2>&1' &
