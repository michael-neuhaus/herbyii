#!/bin/sh

cd /home/pi/HerbyBackup/

sudo python3 herby.py &

# find .git/objects/ -type f empty | xargs rm
# git fetch -p
# git fsck --full

sudo inotifywait -q -m -e CLOSE_WRITE --format="git commit -m 'auto commit' %w && git push origin main" sensor_data.js | bash &
