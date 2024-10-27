from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import requests


def get_credentials() :

    # Define the scopes your app needs (drive.file lets you create and access files)
    SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.readonly']

    # Perform the OAuth flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES, redirect_uri='http://localhost:8080/')
    creds = flow.run_local_server(port=8080)

    # Save the credentials for later use
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

    return creds


def list_file_names():
    creds = get_credentials()
    print(creds.token)

    url = "https://www.googleapis.com/drive/v3/files"

    # Set params to only get file names
    
    params = {
        "fields": "files(id, name)"

    }

    #Add the access token to the request headers
    headers = {
        "Authorization": f"Bearer {creds.token}"

    }    

    # Heres the actual get request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        file_list = response.json().get ('files', [])
        if not file_list:
            print("No files found.")
        
        else:
            for file in file_list:
                print(f"File ID: {file['id']}, File Name: {file['name']}")

    else:
        print(f"Failed to retrieve files: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    list_file_names()



