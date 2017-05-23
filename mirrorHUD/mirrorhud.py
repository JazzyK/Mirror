import requests
import json
import time
from Tkinter import*
#from PIL import ImageTk, Image

#dictionary that links different weather states to respective icons
icons = {}#e.g. 'clear' : 'clear.png',...} 
bg_colour = "black"
fg_colour = "white"
degree_sign= u'\N{DEGREE SIGN}'

class FullscreenWindow:
    
    def __init__(self):
        self.window = Tk()
        self.window.configure(background = bg_colour)
        self.window.title("mirrorHUD")
        self.window.overrideredirect(1)
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (self.width, self.height))
        
        self.weather = Weather()
        
        #displays temperature on screen
        self.temp_label = Label(self.window, text = (str(self.weather.temp) + degree_sign), bg = bg_colour, fg = fg_colour, font = ("Helvetica", 60))
        self.temp_label.pack()

        
class Weather:

    def __init__(self):
        self.apiurl = "http://api.openweathermap.org/data/2.5/weather?id=2855598&appid=28eeeb619c57cebb10ee902c8744672c"
        self.data = ""
        self.jdata = ""
        self.sunrise_time = None
        self.sunset_time = None
        self.temp = None
        self.condition = "" #i.e. clear, cloudy, snow, rain --> icons
        self.get_weather()
    
    def get_weather(self):
        #berlin pankow id= 2855598
        # Uses the free OpenWeatherMap.org API / accessed with api.openweathermap.org
        #my key= 28eeeb619c57cebb10ee902c8744672c

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
            self.sunset_time = int(self.jdata["sys"]["sunset"])
            print "Sunset will be", str(self.sunset_time)

            #temperature
            self.temp = int(self.jdata["main"]["temp"])
            self.temp = round((self.temp - 273.15), 1) # from kelvin to celsius
            print str(self.temp), "Celsius"
            raw_input('success')
            
        except:

            raw_input('failed')


class Time:
    
    def __init__():
            #format hh:mm - 24-hour
if __name__ == "__main__":
    w = FullscreenWindow()
    w.window.mainloop()
    
