import requests
import urllib.parse

URL_APPLE_MUSIC_SEARCH = "https://itunes.apple.com/search"

def getGenresByTitle(title):
    "return the genre from the title passed as arg, using apple music API"
    arguments = {
        "term":title,
        "country":"IT",
        "media":"music",
        "limit":"1"
    }
    arguments = urllib.parse.urlencode(arguments)
    search_reply = requests.get(URL_APPLE_MUSIC_SEARCH, params=arguments)
    if search_reply.json()['resultCount'] == 0:
        genre = 'nope'
    else:
        genre = search_reply.json()['results'][0]['primaryGenreName']
    return genre


if __name__ == '__main__':
    ret = getGenresByTitle("The Other Guy")
    print(ret)
