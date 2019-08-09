#!/bin/bash
sudo killall jackd
cd /home/pi/123piprint/pianowords/
#jackd --silent -d alsa -s &
amixer set Master 100%
python3 main.py
