# 123piprint




#prep system
install a clean raspbian lite (debian buster based in this case)
set hostname / password
enable ssh
log in 
find printerdriver http://www.starmicronics.com/support/default.aspx?printerCode=CUPS_for_Linux
##install dependencies
sudo apt-get install git
sudo apt-get install espeak
sudo apt install speech-dispatcher-espeak
sudo apt-get install midisport-firmware
#sudo apt-get install libjack-dev
sudo apt-get install libjack-jackd2-dev
sudo apt install jackd
sudo apt-get install libasound2 libasound2-dev
sudo apt-get install cups libcups2-dev
sudo usermod -a -G lpadmin pi
open cups to LAN in /etc/cupsd.conf

# tar xzvf starcupsdrv-x.xx.x_linux_yyyymmdd.tar.gz # cd starcupsdrv-x.xx.x_linux
# cd SourceCode
# tar xzvf starcupsdrv-src-x.xx.x.tar.gz
# cd starcupsdrv # make
# make install

git clone https://github.com/kaosbeat/123piprint.git

sudo apt install python3-pip
pip3 install python-slugify mido nltk tracery pyttsx3 tweepy python-rtmidi pyowm
make the authkeys.py
# from requests_oauthlib import OAuth1

# nounauth = OAuth1("")

mashapekey = ""
owmkey = ''

# twitterkeys 
consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""

###install system service



# service installation


#alsa sound card issuies
amixer cset numid=3 1
