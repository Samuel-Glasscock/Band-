from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv() 

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_CACHE_PATH = os.getenv("SPOTIFY_CACHE_PATH")

# config app info
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-read-collaborative",
    cache_path=SPOTIFY_CACHE_PATH,
))

results = sp.current_user_saved_tracks()