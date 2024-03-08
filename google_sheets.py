from dotenv import load_dotenv
import os
import gspread

load_dotenv()


def setup_google_sheet(spreadsheet_title, worksheet_number):
    """Authenticate bot with Google Sheets API and open the specified worksheet within the spreadsheet

    Args:
        spreadsheet_title (String): title of spreadsheet to open
        worksheet_number (int): worksheet number of sheet to open within the spreadsheet; note this is 1-based and correctly corresponds to excel's numbering

    Returns:
        Object: gspread.Worksheet: Worksheet object from gspread representing worksheet within the spreadsheet for operations (read, update)

    Raises:
        gspread.SpreadsheetNotFound: If the spreadsheet title is not found in the user's Google Drive
        IndexError: If the worksheet number is out of range for the spreadsheet
    """
    SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_PATH')

    # Authenticate bot with GoogleSsheets API
    client = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)

    # Open the workbook and then the specific worksheet 
    # -1 is added since gspread's worksheet index is 0-based
    worksheet = client.open(spreadsheet_title).get_worksheet(worksheet_number - 1)

    return worksheet


def batch_update_sheet(sheet, data, start_col, start_row):
    """Batch updates Google sheet with song title and artists for less API calls than individual cell updates

    Args:
        sheet (Object): Worksheet object from gspread to update
        data (List): List of tuples containing song name and artist name [(song_title, artist_name)...]
        start_col (String): String of a character representing what column to start populating with data; note this is case-insensitive
        start_row (int): row number to start populating with data
    """
    end_row = start_row + len(data) - 1
    end_col = chr(ord(start_col) + 1)
    range = f"{start_col}{start_row}:{end_col}{end_row}"

    sheet.update(range, data)
