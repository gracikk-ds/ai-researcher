#!/bin/bash
# Usage: bash start_daemon.sh
# This will start the daily research daemon in the background.

nohup python src/run_daily.py > daemon.out 2>&1 &
echo "Daemon started. Check daemon.out and daemon.log for output."
