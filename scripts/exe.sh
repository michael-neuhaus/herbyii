#!/bin/sh

sudo python3 herby.py &
sudo inotifywait -q -m -e CLOSE_WRITE --format="git commit -m 'auto commit' %w && git push origin main" sensor_data.js | bash &