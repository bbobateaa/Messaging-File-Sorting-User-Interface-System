# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

from abc import ABC, abstractmethod
import urllib
import json
from urllib import request, error
from custom_errors import *


class WebAPI(ABC):
    '''
    Parent class that will be inherited by
    children classes: LastFM and OpenWeather
    '''
    def _download_url(self, url: str) -> dict:
        '''
        Function to open given url with request from urllib
        and reads the response from the server and then loads
        the response with json to get the data
        '''
        try:
            response = urllib.request.urlopen(url)
            results = response.read()
            loader = json.loads(results)
            return loader
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise UrlDownloadFailure
            elif e.code == 503:
                raise ServerConnectionError
        except urllib.error.URLError:
            raise InvalidUrlError

    def set_apikey(self, apikey: str) -> None:
        '''
        Function to set api key to class attributes
        '''
        apikey = apikey.replace(" ", "")
        self.apikey = apikey
        return self.apikey

    @abstractmethod
    def load_data(self):
        '''
        Abstract method for loading data that children
        classes can use and define
        '''
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        '''
        Abstract method for transcluding message
        that children classes can use and define
        '''
        pass
