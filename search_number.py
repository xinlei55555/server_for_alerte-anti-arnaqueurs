import gspread
import pandas as pd

# this is just a random test
# data = [['tom', 10], ['nick', 15], ['juli', 14]]
# df = pd.DataFrame(data, columns = ['Name', 'Age'])


def search_number(number_we_are_looking_for):
    #the next few lines are basically just so that i can access the files
    gc = gspread.service_account(filename = "cred.json")
    sh = gc.open_by_key("1KmGQBAx4fD9fu3MdWsyKZfwQsoSqp6q0UBPdlkCpTsw")
    worksheet = sh.sheet1   
    data = worksheet.get_all_values()
    df = pd.DataFrame(data, columns = ["number"])
    
    if df[df.number == number_we_are_looking_for].empty == False:
    #this means that there is a value that has the search value    
        return True
    return False
