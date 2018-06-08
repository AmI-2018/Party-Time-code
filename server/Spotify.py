from wsgiref import headers
import spotipy
import requests
import json



SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_SEARCH_URL = "https://api.spotify.com/v1/search"
API_VERSION = "v1"


def reqToken():
    headers = {
        "Authorization": "Basic NDJlMDAxZDIzNTY1NDU1OWFiMjQ2YmQwM2NjOWE5ODY6ZDA2MjBkNTI1MDlhNDM0Njg1ZDQzZDVkNDRlMzMxZTA=",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    code_payload = {
        "grant_type": "client_credentials"
    }

    post_reply = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers).json()
    access_token = post_reply["access_token"]
    return access_token

def getGenresFromTrack(track):
    "Return the list of genres from a song based on the spotify rest api"
    sp = spotipy.Spotify(auth=reqToken())
    query_result = sp.search(track, limit="1", market="IT")
    #uri_album = query_result['tracks']['items'][0]['album']['uri']
    uri_artist = query_result['tracks']['items'][0]['artists'][0]['uri']
    #uri_track = query_result['tracks']['items'][0]['uri']

    #print(uri_artist)
    artist_metadata = sp.artist(uri_artist)
    #print(artist_metadata)
    genres = artist_metadata['genres']
    #print(genres)
    return genres

if __name__ == '__main__':
    res = getGenresFromTrack("hello")
    print(res[0])

