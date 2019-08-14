#!/bin/bash
cd /home/pi/123piprint/pianowords/
eval $(ssh-agent -s)
ssh-add ~/.ssh/piano.id_rsa
git add *
git commit -a -m  $1
git pull --commit
git push
