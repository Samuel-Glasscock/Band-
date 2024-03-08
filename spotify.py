from dotenv import load_dotenv
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv() 

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_CACHE_PATH = os.getenv("SPOTIFY_CACHE_PATH")
PLAYLIST_ID = os.getenv("PLAYLIST_ID")

# Configure app info
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://localhost:8888/callback",
    scope="playlist-read-collaborative",
    cache_path=SPOTIFY_CACHE_PATH,
))


def get_playlist_tracks(playlist_id):
    """
    Retrieve tracks from a Spotify playlist

    Args:
        playlist_id (string): hashcode retrieved from playlist when you go to the '...' and then 'share' on a specific playlist

    Returns:
        list: list of tuples containing track name and artist name
    """
    tracks_data = []
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    # handle pagination through tracks if playlist exceeds 100 songs
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # extract song names and associated artists
    for track_entry in tracks:
        track = track_entry['track']
        track_name = track['name']
        artist_names = ", ".join([artist['name'] for artist in track['artists']])
        tracks_data.append((track_name, artist_names)) 

    return tracks_data

# For testing your how your playlist data displaying

# playlist_tracks = get_playlist_tracks(PLAYLIST_ID)
# for track_name, artist_name in playlist_tracks:
#     print(f"{track_name} by {artist_name}")
