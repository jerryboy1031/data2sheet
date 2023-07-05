import gspread
from oauth2client import client

# Load client secret file and initiate OAuth flow
flow = client.flow_from_clientsecrets('path/to/client_secret.json', ['https://spreadsheets.google.com/feeds'])

# Perform OAuth authorization
credentials = client.tools.run_flow(flow, client.Storage(), flags=tools.argparser.parse_args())

# Authorize gspread using the obtained credentials
gc = gspread.authorize(credentials)

# Open the Google Sheets document
sheet = gc.open('Your Google Sheets Document').sheet1
