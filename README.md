# data2sheet
Setting up a Google Cloud Platform (GCP) project and enabling the Google Sheets API is one approach to authenticate and access Google Sheets from your Python code. However, it is not the only method available. If you prefer an alternative approach without using GCP, you can consider using the OAuth 2.0 authorization flow to authenticate and access Google Sheets.

Here's a high-level overview of the alternative approach:
1. Install the necessary libraries:
- Install the gspread library using pip install gspread.
- Install the oauth2client library using pip install oauth2client.
2. Authenticate and access Google Sheets:
- Follow the steps to create a client secret file:
-- Go to the Google Developers Console (console.developers.google.com).
- -Create a new project (if not already created).
- -Enable the Google Sheets API for your project.
- -Create OAuth 2.0 credentials (Client ID and Client Secret).
- -Download the client secret JSON file.
- Use the gspread library and the OAuth 2.0 flow to authenticate and access Google Sheets:
