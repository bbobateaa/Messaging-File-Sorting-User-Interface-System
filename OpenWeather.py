# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

from pathlib import Path
import OpenWeather
from LastFM import LastFM
from WebAPI import WebAPI
import urllib
import json
from urllib import request, error
from custom_errors import *


class OpenWeather(WebAPI):
    '''
    OpenWeather class which inherits from the
    WebAPI class and adapts its functions
    to sort through OpenWeather data and
    provide data for transclusion
    '''
    def __init__(self, zipcode=92697, ccode="US") -> None:
        '''
        Setting class attributes
        '''
        self.zipcode = str(zipcode)
        self.ccode = str(ccode)

    def set_apikey(self, apikey: str) -> None:
        return super().set_apikey(apikey)

    def load_data(self):
        '''
        Calls the web api using the required values
        and stores the response in class data attributes.
        '''
        try:
            api_key = WebAPI.set_apikey(self, self.apikey)
            if type(int(self.zipcode)) != int:
                raise ValueError
            else:
                z = self.zipcode.replace(" ", "")
                c = self.ccode.replace(" ", "")
                self.api_call = f"http://api.openweathermap.org/data/2.5/weather?zip={z},{c}&appid={api_key}"
                self.loader = WebAPI._download_url(self, self.api_call)
                loader = self.loader
                if loader is not None:
                    self.temperature = loader['main']['temp']
                    self.high_temp = loader['main']['temp_max']
                    self.low_temp = loader['main']['temp_min']
                    self.longitude = loader['coord']['lon']
                    self.latitude = loader['coord']['lat']
                    self.weather = loader['weather'][0]['description']
                    self.humidity = loader['main']['humidity']
                    self.pressure = loader['main']['pressure']
                    self.wind_s = loader['wind']['speed']
                    self.wind_d = loader['wind']['deg']
                    self.city = loader['name']
                    self.sunset = loader['sys']['sunset']
                    self.sunrise = loader['sys']['sunrise']
                    return True
                else:
                    raise UrlDownloadFailure
        except ValueError:
            print("\nERROR: Zipcode is an invalid integer")
            return False
        except ServerConnectionError:
            print('ERROR: Server is down')
            return False
        except UrlDownloadFailure:
            print('ERROR: Failed to download contents of URL')
            return False
        except ConnectionError:
            print("ERROR: Connection lost")
            return False
        except InvalidUrlError:
            print("ERROR: Url is invalid")
            return False

    def transclude(self, message: str) -> str:
        '''
        Takes data attributes from load.data() and uses
        it to transclude keywords to class data attributes
        '''
        try:
            msg = message
            message2 = msg.split(" ")
            for i in message2:
                if "@weather" in i:
                    msg = msg.replace("@weather", self.weather)
                if "@high_temp" in i:
                    msg = msg.replace("@high_temp", str(self.high_temp))
                if "@low_temp" in i:
                    msg = msg.replace("@low_temp", str(self.low_temp))
                if "@longitude" in i:
                    msg = msg.replace("@longitude", str(self.longitude))
                if "@latitude" in i:
                    msg = msg.replace("@latitude", str(self.latitude))
                if "@temp" in i:
                    msg = msg.replace("@temp", str(self.temperature))
                if "@humidity" in i:
                    msg = msg.replace("@humidity", str(self.humidity))
                if "@pressure" in i:
                    msg = msg.replace("@pressure", str(self.pressure))
                if "@wind_speed" in i:
                    msg = msg.replace("@wind_speed", str(self.wind_s))
                if "@wind_degree" in i:
                    msg = msg.replace("@wind_degree", str(self.wind_d))
                if "@city" in i:
                    msg = msg.replace("@city", self.city)
                if "@sunset" in i:
                    msg = msg.replace("@sunset", str(self.sunset))
                if "@sunrise" in i:
                    msg = msg.replace("@sunrise", str(self.sunrise))
            return msg
        except ConnectionError:
            print("ERROR: Connection lost")
            return False
        except AttributeError:
            print("ERROR: Cannot transclude message when load_data() failed")
            return False
