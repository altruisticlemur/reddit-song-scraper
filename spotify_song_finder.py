import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import time

client_id = "client_id"
client_secret = "client_secret"
redirect = "http://localhost:8888/callback/"

username = "username"

scope = "playlist-modify-private"

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect)

sp = spotipy.Spotify(auth=token)

def get_saved_comments():
    with open("comments.txt", "r") as f:
            comments = f.read()
            comments = comments.split("\n")

    return comments

comments = get_saved_comments()

c = 0

with open("songs.txt", "a+") as f:
    for comment in comments:
        c += 1
        print(c)
        track_id = 0
        try:
            track_id = sp.search(q=comment, type='track')
            track_id = track_id['tracks']['items'][0]['id']
        except:
            pass

        if track_id != 0 and type(track_id) == str:
            f.write(track_id + "\n")
            print(track_id)
    
    
