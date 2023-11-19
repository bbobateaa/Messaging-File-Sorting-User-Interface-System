# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

import LastFM
import urllib
import json
from urllib import request, error
from WebAPI import WebAPI
from OpenWeather import OpenWeather
from custom_errors import *


class LastFM(WebAPI):
    '''
    LastFM class which inherits from the WebAPI class and adapts its functions
    to sort through LastFM data and provide data for transclusion
    '''
    def __init__(self, artist="Deftones", album="Around the Fur") -> None:
        '''
        Setting class attributes
        '''
        self.artist = artist
        self.album = album

    def set_apikey(self, apikey: str) -> None:
        '''
        Uses inherited function from WebAPI to set apikey
        '''
        return super().set_apikey(apikey)

    def load_data(self) -> None:
        '''
        Calls the web api using the required values
        and stores the response in class data attributes.
        '''
        try:
            checker = True
            art = self.artist.replace(" ", "%20")
            alb = self.album.replace(" ", "%20")
            api_key = WebAPI.set_apikey(self, self.apikey)
            self.api_call = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={api_key}&artist={art}&album={alb}&format=json"
            self.track_list = []
            self.tag_list = []

            loader = WebAPI._download_url(self, self.api_call)
            if loader is not None:
                if 'tracks' in loader['album']:
                    alb_track = loader['album']['tracks']
                    track_check = alb_track['track']
                    for i in track_check:
                        if 'name' not in i:
                            checker = False
                else:
                    checker = False
                if checker is not False:
                    self.lastfm = loader['album']['name']
                    if "wiki" in loader['album']:
                        self.summary = loader['album']['wiki']['summary']
                    else:
                        self.summary = "No available summary for this album"
                    self.artist = loader['album']['artist']
                    self.playcount = loader['album']['playcount']
                    self.listeners = loader['album']['listeners']
                    tag_info = loader['album']['tags']

                    for i in alb_track['track']:
                        self.track_list.append(i['name'])

                    self.track_num = str(len(self.track_list))

                    self.track_list = str(self.track_list)
                    self.track_list = self.track_list.replace("[", "")
                    self.track_list = self.track_list.replace("]", "")

                    for i in tag_info['tag']:
                        self.tag_list.append(i['name'])

                    self.tag_list = str(self.tag_list)
                    self.tag_list = self.tag_list.replace("[", "")
                    self.tag_list = self.tag_list.replace("]", "")
                    return True
                else:
                    raise NotAnAlbumArtist
            else:
                raise UrlDownloadFailure
        except NotAnAlbumArtist:
            return False
        except ServerConnectionError:
            print('ERROR: Server is down')
            return False
        except UrlDownloadFailure:
            print('ERROR: Failed to download contents of URL')
            return False
        except AttributeError:
            print("ERROR: Invalid inputs")
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
            message2 = message.split(" ")
            for i in message2:
                if "@lastfm" in i:
                    message = message.replace("@lastfm", self.lastfm)
                if "@summary" in i:
                    message = message.replace("@summary", self.summary)
                if "@artist" in i:
                    message = message.replace("@artist", self.artist)
                if "@playcount" in i:
                    message = message.replace("@playcount", self.playcount)
                if "@listeners" in i:
                    message = message.replace("@listeners", self.listeners)
                if "@track_names" in i:
                    message = message.replace("@track_names", self.track_list)
                if "@track_num" in i:
                    message = message.replace("@track_num", self.track_num)
                if "@tags" in i:
                    message = message.replace("@tags", self.tag_list)
            return message
        except InvalidAPIKey:
            print("ERROR: This API key is invalid")
            return False
        except AttributeError:
            print("ERROR: Cannot transclude message when load_data() failed")
            return False
