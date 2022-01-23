import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

client_id = "client_id"
client_secret = "client_secret"
redirect = "http://localhost:8888/callback/"

username = "31xznsjqsv3r6xd3t5vjzrnmjkii"

scope = "playlist-modify-private"

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect)

sp = spotipy.Spotify(auth=token)

def get_saved_songs():
    with open("songs.txt", "r") as f:
            songs = f.read()
            songs = songs.split("\n")

    return songs

playlist = "0kEVbXM9LM5pQi5vUUFRzN"
tracks = get_saved_songs()
print(len(tracks))

# removes duplicates
tracks = list(set(tracks))
print(len(tracks))

# first item of list was an empty string
# skipped over it
tracks = tracks[1:]
print(len(tracks))

for i in range(100, len(tracks), 100):
    sp.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=tracks[i-100:i])
