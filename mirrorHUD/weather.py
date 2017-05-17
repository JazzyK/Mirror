import requests
import json
import time
#berlin pankow id= 2855598
# Uses the free OpenWeatherMap.org API / accessed with api.openweathermap.org
#my key= 28eeeb619c57cebb10ee902c8744672c

#weather only
apiurl = "http://api.openweathermap.org/data/2.5/weather?id=2855598&appid=28eeeb619c57cebb10ee902c8744672c"
raw_input('press enter to continue')
try:
    data= requests.get(apiurl)
    print 'api loaded'
    jdata = data.json()
    print json.dumps(jdata, indent = 4)
    
    #sunrise time
    sunrise = int(jdata["sys"]["sunrise"])
    print "sunrise was", str(sunrise)
    #sunset time
    sunset = int(jdata["sys"]["sunset"])
    print "Sunset will be", str(sunset)
    #temperature
    temp = int(jdata["main"]["temp"])
    temp = temp - 273.15 # from kelvin to celsius
    print str(temp), "Kelvin"
    raw_input('success')
except:
    raw_input('failed')