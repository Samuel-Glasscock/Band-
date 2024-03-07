from dotenv import load_dotenv
import os
import gspread

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_PATH')

# Authenticate bot with GoogleSsheets API
client = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)

