import requests
import json
import time
from Tkinter import*
#from PIL import ImageTk, Image

#dictionary that links different weather states to respective icons
icons = {#e.g. 'clear' : 'clear.png',...} 

class FullscreenWindow:
    
    def __init__(self):
        self.window = Tk()
        self.window.configure(background = "black")
        self.window.title("mirrorHUD")
        self.window.overrideredirect(1)
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (self.width, self.height))
        
        self.weather = Weather()
        
class Weather:

    def __init__(self):
        self.get_weather()
    
    def get_weather(self):
        #berlin pankow id= 2855598
        # Uses the free OpenWeatherMap.org API / accessed with api.openweathermap.org
        #my key= 28eeeb619c57cebb10ee902c8744672c
        self.apiurl = "http://api.openweathermap.org/data/2.5/weather?id=2855598&appid=28eeeb619c57cebb10ee902c8744672c"
        self.data = ""
        self.jdata = ""
        self.sunrise_time = None
        self.sunset_time = None
        self.temp = None
        try:
            self.data= requests.get(self.apiurl)
            print 'api loaded'
            self.jdata = self.data.json()
            
            #mere purpose is to make it more readable for me, the programmer - yay!
            print json.dumps(self.jdata, indent = 4)#can be deleted after
            
            #sunrise time 
            self.sunrise_time = int(self.jdata["sys"]["sunrise"])
            print "sunrise was", str(self.sunrise_time)
            
            #sunset time
            try:
                self.sunset_time = int(jdata["sys"]["sunset"])
                print "Sunset will be", str(self.sunset_time)
                
            except: #not found == it is night
                self.sunset_time = None
                raw_input("sunset_time not found")
            #temperature
            self.temp = int(self.jdata["main"]["temp"])
            self.temp = self.temp - 273.15 # from kelvin to celsius
            self.temp = round(self.temp, 1)
            print str(self.temp), "Celsius"
            raw_input('success')
            
        except:

            raw_input('failed')
    
if __name__ == "__main__":
    w = FullscreenWindow()
    w.window.mainloop()
    
