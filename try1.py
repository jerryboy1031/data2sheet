import gspread
#the old one is deprecated: from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

#launches a browser asking you for authentication
def try1():
    scope = ['https://www.googleapis.com/auth/spreadsheets']#, 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']
    #credentials = ServiceAccountCredentials.from_json_keyfile_name(mykey_json, scope)
    credentials= Credentials.from_service_account_file("secret_credential.json", scopes=scope)
    
    client = gspread.authorize(credentials)

    sh = client.open('EU tour') #error--------------
    
    #gc= gspread.oauth(credentials_filename=r'C:/Users/User/anaconda3/Lib\site-packages/gspread/credential20230705.json') 
    #print(sh.get('總覽!B2'))
    wks= sh.worksheet("總覽")
    print(wks.get_all_records())
    
    wks.insert_row("hello",2)
    return 0


if __name__ == "__main__":
    try1()