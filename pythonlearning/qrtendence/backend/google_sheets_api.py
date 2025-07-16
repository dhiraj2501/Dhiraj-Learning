
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def get_sheets_service():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        return service
    except HttpError as err:
        print(err)
        return None

def read_sheet_data(spreadsheet_id, range_name):
    service = get_sheets_service()
    if service:
        try:
            result = (
                service.spreadsheets()
                .values()
                .get(spreadsheetId=spreadsheet_id, range=range_name)
                .execute()
            )
            values = result.get("values", [])
            return values
        except HttpError as err:
            print(f"Error reading sheet: {err}")
            return None
    return None

def write_sheet_data(spreadsheet_id, range_name, values):
    service = get_sheets_service()
    if service:
        try:
            body = {"values": values}
            result = (
                service.spreadsheets()
                .values()
                .update(
                    spreadsheetId=spreadsheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body,
                )
                .execute()
            )
            return result
        except HttpError as err:
            print(f"Error writing to sheet: {err}")
            return None
    return None

if __name__ == "__main__":
    # Example usage (replace with your spreadsheet ID and range)
    SPREADSHEET_ID = "YOUR_SPREADSHEET_ID_HERE"
    RANGE_NAME = "Sheet1!A1:C"

    # Read data
    # data = read_sheet_data(SPREADSHEET_ID, RANGE_NAME)
    # if data:
    #     print("Read data:")
    #     for row in data:
    #         print(row)

    # Write data
    # values_to_write = [
    #     ["Name", "Age", "City"],
    #     ["Alice", 30, "New York"],
    #     ["Bob", 24, "London"],
    # ]
    # write_result = write_sheet_data(SPREADSHEET_ID, "Sheet1!A1", values_to_write)
    # if write_result:
    #     print("Write successful:", write_result)
