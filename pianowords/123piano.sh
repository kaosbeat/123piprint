#!/bin/bash
cd /home/pi/123piprint/pianowords/
eval $(ssh-agent -s)
ssh-add ~/.ssh/piano.id_rsa
git pull --commit&
amixer set Master 100%
