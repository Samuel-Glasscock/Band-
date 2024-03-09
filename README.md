# Spotify Playlist to Google Sheet Automation

**Description:** This project integrates Spotify playlists with Google Sheets, offering an effective solution for music enthusiats, bands, and collaborative teams to dynamically rate and discuss playlist songs asynchronously. At its core, the automation simplifies the task of transferring songs and artists as added directly from Spotify into a Google Sheet, where participants can easily rate each song and share insights or feedback.


## Table of Contents

- [Usage (Practical)](#usage-practical)
- [Installation](#installation)
- [Usage (Code)](#usage-code)
- [Tech Stack](#tech-stack)

## Usage (Practical)

**General Usage:** This project can be used for any needs for automating adding songs and artists from any spotify playlist to Google Sheets for any response/discussion need such as being used in a classroom to record student responses to educational podcasts or book clubs to automate members rating audiobooks.

**Specific Usage:** I use this project to automate adding songs to Google Sheets for my band's communications about potential songs to add to our performing set list. We add potential songs to our shared Spotify playlist for the rest of us to listen to. To keep a record of our thoughts, I integrated Google Sheets so that we could rate each of the songs on our Spotify Playlist in various categories and give our feedback (Overall rating, Playability, Comments). This data is then used in an overall calculation, which determines which songs to add to our playlist based on specified thresholds.

## Installation

1. Clone the repo using `git clone https://github.com/Samuel-Glasscock/Spotify-Playlist-Automation.git` and then navigate to the project directory using `cd Spotify-Playlist-Automation`
2. Install dependencies from the requirements.txt using a package manager such as pip using `pip install -r requirements.txt`

#### Handling API keys

**Spotify Web API**

1. Follow the directions for steps 1, 2, 3 at https://developer.spotify.com/documentation/web-api for logging into your spotify account dashboard and creating an app
2. Once your app is created, you can use environment variables to store your Spotify Client ID and Client Secret
3. You will need to specify a directory path for a file that will store your automatically generated access token such as in a hidden .cache file in your project directory
4. You will need to access your Spotify playlist's ID which can be found by going to the "..." and then "copy link" and then paste the hash for that as the playlist to read in, or leverage environment variables to store your playlist ID. See https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids for more details on extracting the playlist ID from the playlist's link

**Google Sheets API**

1. Visit https://console.cloud.google.com and sign in and create a new project
2. On the navigation menu for your project, go to "APIs & Services"
3. Search for Google sheets API and click enable. Then search Google Drive API and enable.
4. While under "APIs & Services", go to "Credentials" and "Create Credentials" and select "Service Account" from the dropdown, which will be your automation bot account. Fill in the other fields and click "Create". Set the service account role to at least "Editor" and then click done
5. Under the Service accounts on your dashboard, select your newly created account then go to "Keys" on the top menu. Then select "Add Key" and "Create New Key" and "JSON". Your browser will download a JSON key file
6. In your project you will now need to specify a path to your downloaded JSON key file. The file can be added to your project and kept under a "secrets/" directory or such if you wish to store it in your project and keep it unversioned
7. In your Google Console under your service account details, copy the email of your service account and share your Google Worksheet with your service account email

## Usage (Code)

#### Constants to be changed for your local project:

**`spotify.py`**

- `SPOTIFY_CLIENT_ID`: the client ID of your spotify app as referenced in Step 2 of _Spotify Web API_ in [Handling API keys](#handling-api-keys)
- `SPOTIFY_CLIENT_SECRET`: the client secret of your spotify app as referenced in Step 2 of _Spotify Web API_ in [Handling API keys](#handling-api-keys)
- `SPOTIFY_CACHE_PATH`: path to where you setup for spotify to store your access token as referenced in Step 3 of _Spotify Web API_ in [Handling API keys](#handling-api-keys)

**`google_sheets.py`**

- `SERVICE_ACCOUNT_FILE`: path to your JSON file for Google Sheet API key

**`main.py`**

- `PLAYLIST_ID`: ID of what playlist you want to read in as referenced in Step 4 of _Spotify Web API_ in [Handling API keys](#handling-api-keys)
- `setup_google_sheet()`: specify arguemnts for your specific Google Worksheet. See docstring for function in `google_sheets.py` file
- `batch_update_sheet()`: specify arguments for what cell to start writing data. See docstring for function in `google_sheets.py` file

####Scheduling Automated updates
Based on the needs of your project for frequency of updates, this can be either scheduled on your local machine or delegated to cloud based options. I use Windows Task Manager since our band only adds a small amount of songs daily, which is comparable to launchd or cron on a macOS or Linux system respectively. Some cloud options could be Google Cloud Scheduler, AWS Lambda and Amazon CloudWatch Events, or Heroku.

## Tech Stack

####APIs

- **Spotify Web API:** Provides access to Spotify's music database, allowing account authenticatation and playlist access (https://developer.spotify.com/documentation/web-api)
- **Google Drive API:** Provides broader access to user's files such as permission management and file creation and deletion by automation bot (https://developers.google.com/drive/api/guides/about-sdk)
- **Google Sheets API:** Enables read and write permission to Google Sheets programmatically (https://developers.google.com/sheets/api/guides/concepts)

####Libaries

- **spotipy:** Lightweight Python library that simplifies interacting with the Spotify Web API. Handles authentication and making requests to Spotify's endpoints (https://spotipy.readthedocs.io/en/2.22.1/)
- **gspread:** Python library that comes with Google Sheet CRUD functions out of the box and acts as a wrapper for the Google Sheets API to provide a more dev friendly interface (https://docs.gspread.org/en/v6.0.0/)
