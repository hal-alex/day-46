import requests
from bs4 import BeautifulSoup

user_year = input("Which year of music would you like to listen to? Use format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{user_year}/"

result = requests.get(url=URL).text


soup = BeautifulSoup(result, "html.parser")


song_names = soup.find_all(name="h3", class_="a-no-trucate")

song_names_list = [song.getText().strip() for song in song_names]
print(song_names_list)

