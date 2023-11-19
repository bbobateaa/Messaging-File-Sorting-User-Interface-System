# transclude.py

# Transclude function code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

from OpenWeather import OpenWeather
from LastFM import LastFM
from file_class import File
from custom_errors import *

# API INPUTS
API_OP = "Which API would you like to use? (OpenWeather or LastFM or both): "
ZIPCODE = "Enter a valid zipcode: "
CCODE = "Enter a valid country code: "
ARTIST = "Enter an existing artist or band: "
ALBUM = "Enter an existing album belonging to the artist or band: "
W_API_KEY = "Enter your API key for OpenWeather: "
F_API_KEY = "Enter your API key for LastFM: "

# TRANSCLUDE OPTIONS
WEATHER_TRANS = """
Use any of the following keywords for OpenWeather to transclude your message!

@weather - get the weather description
@temp - get the temperature
@low_temp - get the lowest temperature it will be
@high_temp - get the highest temperature it will be
@longitude - get the longitude
@latitude - get the latitude
@humidity - get the humidity level
@pressure - get the pressure level
@wind_speed - get the wind speed
@wind_degree - get the wind degree
@city - get the city of given zipcode and state
@sunset - get the time of sunset
@sunrise - get the time of sunrise

Your message: """

LASTFM_TRANS = """
Use any of the following keywords for LastFM to transclude your message!

@lastfm - get the album name
@summary - get the summary of the album
@artist - get the name of the artist
@playcount - get the total playcounts for given album
@listeners - get the total listeners for given album
@track_names - get the names of each track in given album
@track_num - get the number of how many tracks there are in given album
@tags - get the tags associated with the album or artist

Your message: """

BOTH_TRANS = """
Use any of the following keywords for OpenWeather to transclude your message!

@weather - get the weather description
@temp - get the temperature
@low_temp - get the lowest temperature it will be
@high_temp - get the highest temperature it will be
@longitude - get the longitude
@latitude - get the latitude
@humidity - get the humidity level
@pressure - get the pressure level
@wind_speed - get the wind speed
@wind_degree - get the wind degree
@city - get the city of given zipcode and state
@sunset - get the time of sunset
@sunrise - get the time of sunrise

Use any of the following keywords for LastFM to transclude your message!

@lastfm - get the album name
@summary - get the summary of the album
@artist - get the name of the artist
@playcount - get the total playcounts for given album
@listeners - get the total listeners for given album
@track_names - get the names of each track in given album
@track_num - get the number of how many tracks there are in given album
@tags - get the tags associated with the album or artist

Your message: """

ERROR_WHITE = "ERROR: You cannot enter just whitespace!"


def transclude_msg():
    '''
    Serves as a transclude function for neater implementation in ui3.py which
    asks user for options of choosing which API to transclude with and then
    asking user for inputs for API parameters and returning them their
    transcluded message
    '''
    try:
        file = File()
        tran_op = input(API_OP)
        if tran_op == "OpenWeather":
            apikey = input(W_API_KEY)
            while file.white_space(apikey) is False:
                print(ERROR_WHITE)
                apikey = input(W_API_KEY)
            zipcode = input(ZIPCODE)
            while file.white_space(zipcode) is False:
                print(ERROR_WHITE)
                zipcode = input(ZIPCODE)
            ccode = input(CCODE)
            while file.white_space(ccode) is False:
                print(ERROR_WHITE)
                ccode = input(CCODE)
            weather = OpenWeather(zipcode, ccode)
            weather.set_apikey(apikey)
            w_load = weather.load_data()
            if w_load is not False:
                message = input(WEATHER_TRANS)
                while file.white_space(message) is False:
                    print(ERROR_WHITE)
                    message = input(WEATHER_TRANS)
                post = weather.transclude(message)
            else:
                raise InvalidAPIKey
        elif tran_op == "LastFM":
            apikey = input(F_API_KEY)
            while file.white_space(apikey) is False:
                print(ERROR_WHITE)
                apikey = input(F_API_KEY)
            artist = input(ARTIST)
            while file.white_space(artist) is False:
                print(ERROR_WHITE)
                artist = input(ARTIST)
            album = input(ALBUM)
            while file.white_space(album) is False:
                print(ERROR_WHITE)
                album = input(ALBUM)
            last_fm = LastFM(artist, album)
            last_fm.set_apikey(apikey)
            fm_load = last_fm.load_data()
            if fm_load is not False:
                message = input(LASTFM_TRANS)
                while file.white_space(message) is False:
                    print(ERROR_WHITE)
                    message = input(LASTFM_TRANS)
                post = last_fm.transclude(message)
            else:
                raise NotAnAlbumArtist
        elif tran_op == "both" or tran_op == "Both":
            w_apikey = input(W_API_KEY)
            while file.white_space(w_apikey) is False:
                print(ERROR_WHITE)
                w_apikey = input(W_API_KEY)

            zipcode = input(ZIPCODE)
            while file.white_space(zipcode) is False:
                print(ERROR_WHITE)
                zipcode = input(ZIPCODE)

            ccode = input(CCODE)
            while file.white_space(ccode) is False:
                print(ERROR_WHITE)
                ccode = input(CCODE)

            fm_apikey = input(F_API_KEY)
            while file.white_space(fm_apikey) is False:
                print(ERROR_WHITE)
                fm_apikey = input(F_API_KEY)

            artist = input(ARTIST)
            while file.white_space(artist) is False:
                print(ERROR_WHITE)
                artist = input(ARTIST)

            album = input(ALBUM)
            while file.white_space(album) is False:
                print(ERROR_WHITE)
                album = input(ALBUM)

            weather = OpenWeather(zipcode, ccode)
            weather.set_apikey(w_apikey)
            w_load = weather.load_data()

            if w_load is not False:
                last_fm = LastFM(artist, album)
                last_fm.set_apikey(fm_apikey)
                fm_load = last_fm.load_data()
                if fm_load is not False:
                    message = input(BOTH_TRANS)
                    while file.white_space(message) is False:
                        print(ERROR_WHITE)
                        message = input(BOTH_TRANS)
                    trans_msg = weather.transclude(message)
                    post = last_fm.transclude(trans_msg)
                else:
                    raise NotAnAlbumArtist
            else:
                raise InvalidAPIKey
        print(f"\nHere is your transcluded message:\n{post}")
        return post
    except InvalidAPIKey:
        print("\nERROR: Invalid API key or Zipcode or Country Code")
        return False
    except NotAnAlbumArtist:
        print("\nERROR: Invalid API key or Album or Artist")
        return False
