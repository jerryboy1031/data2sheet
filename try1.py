import gspread
#the old one is deprecated: from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

#launches a browser asking you for authentication
def try1():
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    mykey_json = r'C:/Users/User/anaconda3/Lib\site-packages/gspread/credential.json'
    #credentials = ServiceAccountCredentials.from_json_keyfile_name(mykey_json, scope)
    credentials= Credentials.from_service_account_file(mykey_json, scopes=scope)
    
    client = gspread.authorize(credentials)

    sh = client.open('歐洲之旅').sheet1
    
    #gc= gspread.oauth(credentials_filename=r'C:/Users/User/anaconda3/Lib\site-packages/gspread/credential20230705.json') 
    #print(sh.get('總覽!B2'))
    print(sh.get_all_records())
    return 0


if __name__ == "__main__":
    try1()