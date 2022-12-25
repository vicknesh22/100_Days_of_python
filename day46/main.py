import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

travel_date = input("Which year do you want to travel to? \n Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{travel_date}/"
response = requests.get(URL)
url_html_data = response.text

# making soup out of the url response
soup = BeautifulSoup(url_html_data, "html.parser")
chart_data = soup.select("li ul li h3")
song_list = [song.get_text(strip=True) for song in chart_data]

# # using spotipy to work with spotify web api
SPOTIPY_CLIENT_ID = "98846cba57ae49439a29d913c1e613dd"
SPOTIPY_CLIENT_SECRET = "386481ad7ae74ad484b2382dea87b4f1"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                               redirect_uri="http://example.com",
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               client_id=SPOTIPY_CLIENT_ID,
                                               show_dialog=True, cache_path="Token.txt"))

user_id = sp.current_user()["id"]

# ################################# search song in spotify #############################
songs_uri = []
year = travel_date.split("-")[0]

for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on spotify. Skipping it.")

# print(songs_uri)

#################################### create playlist from searched song list ########################

bill_playlist = sp.user_playlist_create(user=user_id, name=f"{travel_date}-Billboard 100",
                                        description="This playlist has the billboard top songs of this timeperiod.",
                                        public=False)

# print(user_playlist)


add_playlist = sp.playlist_add_items(playlist_id=bill_playlist["id"], items=songs_uri)
