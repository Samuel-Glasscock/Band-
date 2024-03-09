from spotify import get_playlist_tracks
from google_sheets import setup_google_sheet, batch_update_sheet
import os
from dotenv import load_dotenv

load_dotenv()

PLAYLIST_ID = os.getenv("PLAYLIST_ID")


def main():
    # use Spotify API to fetch playlist tracks
    playlist_tracks = get_playlist_tracks(PLAYLIST_ID)

    # Specify which google sheet to update
    # This is dependent on your sheet name in Google Sheets, in this case, mine is called "Band Playlist"
    # Keep in mind this is the workbook title/Spreadsheet title, not the individual worksheet title
    worksheet = setup_google_sheet("Band Playlist", 1)

    # Update google sheet with fetched tracks
    batch_update_sheet(worksheet, playlist_tracks, 'A', 3)


if __name__ == "__main__":
    main()