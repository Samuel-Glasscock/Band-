from dotenv import load_dotenv
import os
import gspread

load_dotenv()


def setup_google_sheet(sheet_title):
    SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_PATH')

    # Authenticate bot with GoogleSsheets API
    client = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
    
    worksheet1 = client.open(sheet_title).sheet1

    return worksheet1


def batch_update_sheet(sheet, data, start_row, start_col):
    end_row = start_row + len(data) - 1
    end_col = chr(ord(start_col) + 1)
    range = f"{start_col}{start_row}:{end_col}{end_row}"

    sheet.update(range, data)
