# 123piprint

## prep system
install a clean raspbian lite
- not debian buster based in this case, espeak gives major problems
- I used 2018-10-09-raspbian-stretch-lite.zip
```
sudo raspi-config
- set hostname / password
- enable ssh
- reboot 
```
## install dependencies
```
sudo apt-get install git
sudo apt-get install espeak
sudo apt install speech-dispatcher-espeak
sudo apt-get install midisport-firmware
sudo apt install jackd
sudo apt-get install libjack-jackd2-dev
sudo apt-get install libasound2 libasound2-dev
sudo apt-get install cups libcups2-dev
sudo usermod -a -G lpadmin pi
open cups to LAN in /etc/cupsd.conf
find printerdriver http://www.starmicronics.com/support/default.aspx?printerCode=CUPS_for_Linux
tar xzvf starcupsdrv-x.xx.x_linux_yyyymmdd.tar.gz # cd starcupsdrv-x.xx.x_linux
cd SourceCode
tar xzvf starcupsdrv-src-x.xx.x.tar.gz
cd starcupsdrv # make
make install
```
## add printer from web interface

## clone pianosoftware from gitrepo
```
git clone https://github.com/kaosbeat/123piprint.git
sudo apt install python3-pip
pip3 install python-slugify mido nltk tracery tweepy python-rtmidi pyowm sh unidecode
```
## make the authkeys.py file (not in git)
touch lib/authkeys.py
vi lib/authkeys.py
# from requests_oauthlib import OAuth1
```
mashapekey = ""
owmkey = ''
# twitterkeys 
consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""
```
## install system service
### service installation

## system git config
- gen sshkey > https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- add to github . > https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account
-set new remote 
```git remote set-url origin $(git remote show origin | grep "Fetch URL" | sed 's/ *Fetch URL: //' | sed 's/https:\/\/github.com\//git@github.com:/')```



#alsa sound card issuies
not needed on stretch??
amixer cset numid=3 1
