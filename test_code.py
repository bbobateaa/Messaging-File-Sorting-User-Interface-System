
from LastFM import LastFM
from OpenWeather import OpenWeather
from WebAPI import WebAPI
from custom_errors import *
import unittest
import pytest


class APITester(unittest.TestCase):
    '''
    Class for testing api modules
    '''
    def test_api(self):
        '''
        Tests if OpenWeather class generate expected transcluded message
        '''
        webapi = OpenWeather()
        apikey = "1ec3e21ff40944b3d0db556b0ba35065"
        message = "Testing the weather: @weather"

        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)

        assert result == f"Testing the weather: {webapi.weather}"

    def test_api2(self):
        '''
        Checks if OpenWeather class generates False if APIkey is incorrect
        '''
        webapi = OpenWeather()
        apikey = "1ec3e213d0db556b0ba35065"
        message = "Testing the weather: @weather"

        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)

        assert result is False

    def test_api3(self):
        '''
        Checks if LastFM class generates expected transcluded message
        '''
        webapi = LastFM()
        apikey = "d88be937d0fa05f83b623efda45e6110"
        message = "Testing the lastfm: @lastfm"

        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)

        assert result == "Testing the lastfm: Around the Fur"

    def test_api4(self):
        '''
        Checks if LastFM class generates False if api key is incorrect
        '''
        webapi = LastFM()
        apikey = "d88b3b623efda45e6110"
        message = "Testing the lastfm: @lastfm"

        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)

        assert result is False

    def test_api5(self):
        '''
        Checks if LastFM class returns expected transcluded message
        '''
        webapi = LastFM()
        apikey = "d88be937d0fa05f83b623efda45e6110"
        message = "@lastfm is a album by @artist"

        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)

        assert result == f"{webapi.lastfm} is a album by {webapi.artist}"

    def test_api6(self):
        '''
        Checks if LastFM class returns false if album is not a valid album
        '''
        webapi = LastFM(artist="SZA", album="Broken Clocks")
        apikey = "d88be937d0fa05f83b623efda45e6110"
        message = "Testing the lastfm: @lastfm is a album by @artist"

        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)

        assert result is False

    def test_api7(self):
        '''
        Checks if LastFM class generates expected
        transcluded message with more keywords
        '''
        webapi = LastFM(artist="SZA", album="Ctrl")
        apikey = "d88be937d0fa05f83b623efda45e6110"
        message = "@lastfm by @artist. Summary: @summary"

        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)
        ex = f"{webapi.lastfm} by {webapi.artist}. Summary: {webapi.summary}"
        assert result == ex

    def test_api8(self):
        '''
        Checks if OpenWeather class raises
        UrlDownloadFailure exception with invalid inputs
        '''
        zipcode = 129301280
        ccode = 'USA'
        api_key = "1ec3e21ff40944b3d0db556b0ba35065"
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},{ccode}&appid={api_key}"
        with pytest.raises(Exception) as e:
            WebAPI._download_url(WebAPI, url)
        assert e.type == UrlDownloadFailure

    def test_api9(self):
        '''
        Checks if LastFM class returns False if inputs are invalid
        '''
        webapi = LastFM(artist="awdjap", album="oidhaiwd")
        apikey = "d88be937d0fa05f83b623efda45e6110"
        message = "Testing the lastfm: @lastfm is a album by @artist"

        webapi.set_apikey(apikey)
        assert webapi.load_data() is False

    def test_api10(self):
        '''
        Checks if OpenWeather class raises a InvalidUrlError
        if url link used is incorrect
        '''
        zipcode = 91733
        ccode = 'USA'
        api_key = "1ec3e21ff40944b3d0db556b0ba35065"
        url = f"http://wwapi.openweathermap.org/data/2.5/weather?zip={zipcode},{ccode}&appid={api_key}"
        with pytest.raises(Exception) as e:
            WebAPI._download_url(WebAPI, url)
        assert e.type == InvalidUrlError

    def test_api11(self):
        '''
        Checks if LastFM class raises a InvalidUrlError
        if url link used is incorrect
        '''
        art = "aowdioawd"
        alb = "aowjdoiaw"
        api_key = "1ec3e21ff40944b3d0db556b0ba35065"
        url = f"http://wwws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={api_key}&artist={art}&album={alb}&format=json"
        with pytest.raises(Exception) as e:
            WebAPI._download_url(WebAPI, url)
        assert e.type == InvalidUrlError

    def test_api12(self):
        '''
        Checks if LastFM class returns None if artist and album are not valid
        '''
        art = "aowdioawd"
        alb = "aowjdoiaw"
        api_key = "1ec3e21ff40944b3d0db556b0ba35065"
        url = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={api_key}&artist={art}&album={alb}&format=json"
        assert WebAPI._download_url(self, url) is None


if __name__ == "__main__":
    unittest.main()
