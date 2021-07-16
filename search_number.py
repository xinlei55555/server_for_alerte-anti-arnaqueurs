import gspread
#import pandas as pd
#import pygsheets


def return_row_from_cell(cell_with_value):
    last_index = str(cell_with_value)[7:].find('C')
    row_value = str(cell_with_value)[7:7+last_index]
    return int(row_value)

def search_number(number):
    number = str(number)
    #the next few lines are basically just so that i can access the files
    gc = gspread.service_account(filename = "cred.json")
    sh = gc.open_by_key("1zGbjjH2ibHh6SEctWO_PYxvhkVinMK_0SJvYO4DXtDo")
    worksheet = sh.sheet1   
    # data = worksheet.get_all_values()

#this returns a list of all the instances of the value we are looking for
    cell_with_value = worksheet.findall(number, in_column = 1)

    #if there is such a value, then it will return the value of the frequence
    if cell_with_value != []:
        row_value = return_row_from_cell(cell_with_value[0])
        return int(worksheet.cell(row_value,  2).value)
    return 0
#--------------------
    # df = pd.DataFrame(data, columns = ["number"])
    
    # if df[df.number == number_we_are_looking_for].empty == False:
    # #this means that there is a value that has the search value    
    #     return True
    # return 

#print(search_number(10))