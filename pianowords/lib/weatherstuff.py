import pyowm
import filestuff
from authkeys import owmkey
import datetime
datechecked = datetime.datetime.utcnow()
API_key = owmkey
owm = pyowm.OWM(API_key)
try:
    observation = owm.weather_at_place('Ghent,be')
    filestuff.object2File(observation, "lib/lastweather.object")
except:
    print("it did not work as expected")
    observation = filestuff.file2Object("lib/lastweather.object")
w = observation.get_weather()
# w.get_temperature(unit='celsius') 
# w.get_wind()
# print(dir(w))

print(w.get_temperature(unit='celsius') )

def checkweather():
    global w
    if ((datetime.datetime.utcnow() - datechecked).total_seconds() < 3600):
        #recheck weather, an hour or more has passed
        w = observation.get_weather()
    else:
        pass
    
def getweather():
    temp = w.get_temperature(unit='celsius')['temp']
    if (temp < 12):
        tempstatus = 'cold'
    elif (temp < 20):
        tempstatus = 'chilly'
    elif (temp < 24 ):
        tempstatus = 'warm'
    elif (temp >= 24) :
        tempstatus = 'hot'
    

    
    wstatus = {"temp": tempstatus, }
    return wstatus

getweather()