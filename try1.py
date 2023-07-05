import gspread
#launches a browser asking you for authentication
def try1():
    gc= gspread.oauth() 
    sh = gc.open('歐洲之旅')
    print(sh.sheet1.get('總覽!B2'))
    return 0

if __name__ == "__main__":
    try1()