#!/bin/bash

pwd
python3 logger/ros_logger.py
python3 listener/ros_listener.py

wait -n

exit $?