#!/bin/bash
sudo killall jackd
cd /home/pi/123piprint/pianowords/
jackd --silent -d alsa -s -p 2048&
amixer set PCM 100%
python3 main.py
