import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


user_year = input("Which year of music would you like to listen to? Use format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{user_year}/"

result = requests.get(url=URL).text


soup = BeautifulSoup(result, "html.parser")


song_names = soup.find_all(name="h3", class_="a-no-trucate")

song_names_list = [song.getText().strip() for song in song_names]
print(song_names_list)

SPOTIFY_CLIENT_ID = "b4d90e186db64bc4b76cbebceedfdcbf"
SPOTIFY_SECRET = "4c273f9e1ff34359830edb43a85623e5"
REDIRECT_URI = "https://example.com/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

for song in song_names_list:
    result = sp.search(q=f"track:{song}", type="track")
    print(result)

