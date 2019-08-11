#!/bin/bash
cd /home/pi/123piprint/pianowords/
amixer set Master 100%
python3 main.py&
