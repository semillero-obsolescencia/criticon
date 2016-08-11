#!/bin/bash

source /usr/local/bin/virtualenvwrapper.sh
workon criticon
which python
cd /home/pi/code/criticon
python criticon2.py
