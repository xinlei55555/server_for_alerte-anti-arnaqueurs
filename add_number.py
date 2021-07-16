import gspread
#this module lets us enter data into the google spread sheet

#i tried using time, to slow down the process, so to respect he quota that was imposed by google
#import time
    #yet, i believe it still does not work, so i will simply start by transforming the data into a pandas dataframe that will later be repushed to the spreadsheet

gc = gspread.service_account(filename = "cred.json")
#this tells the gspread module where to look for the informations on our google sheet

sh = gc.open_by_key("1zGbjjH2ibHh6SEctWO_PYxvhkVinMK_0SJvYO4DXtDo")
#this is part of the link for the google sheet that contains the spam numbers

worksheet = sh.sheet1
# this tells the module which sheet that we want (because we only have one sheet, we can just write sheet #1)


#this function returns the row from the notation that was <cell blabla>
def return_row_from_cell(cell_with_value):
    last_index = str(cell_with_value)[7:].find('C')
    row_value = str(cell_with_value)[7:7+last_index]
    return int(row_value)

def add_num(number):
  #these remove any useless symbols
    if '+' in number:
        number = number.replace('+', '')
    if '-' in number:
        number = number.replace('-', '')
    if ')' in number:
        number = number.replace(')', '')
    if '(' in number:
        number = number.replace('(', '')
    if ' ' in number:
        number = number.replace(' ', '')

    #here, i am getting the length of the whole sheet 
    end_row = len(worksheet.get_all_values())

#I made it so it is impossible that the value can exceed the last value
    # if int(number) > int(worksheet.cell(end_row,  1).value):
    #     worksheet.append_rows([[number, 1]])
    #     return 'successfully inserted ' + str(number) + ' at row of index ' + str(end_row)
        #VERY IMPORTANT, append_rows, takes a 2D array!
        #if all the rows have been exhausted, it will append

    cell_with_value = worksheet.findall(number, in_column = 1)

    if cell_with_value != []:
        row_value = return_row_from_cell(cell_with_value[0])
        worksheet.update_cell(row_value, 2, int(worksheet.cell(row_value,2).value) + 1)
        return 'successfully inserted ' + str(number) + ' at row of index ' + str(row_value)
    
#here, I am setting the range that I will serach through
    #VERY IMPORTANT TO START AT THE i = 2 BECAUSE THE WORKSHEET ONLY STARTS AT INDEX 2
    # cells = 'A2:A'+str(end_row)
    # range_of_cells = worksheet.range(cells)
    #using this line of code, i won't need to call worksheet.cell(i, 1)
#'''------------------------------------
    #this is highly inefficient, looping through all the values???
        #here i am looping through these values    
        #instead of being an index, cell is now the whole cell
   
    # for cell in range_of_cells:
    #     # if int(cell.value) == number:
    #     #     worksheet.update_cell(i, 2, int(cell.value) + 1)
    #     #     return 'successfully inserted at ' + str(i) + ' value'

    #     #this adds the number to the spam number database at the specific position
    #     # check out this link
    #         # https://docs.gspread.org/en/latest/api.html'''
#-----------------------------------------------
#now, i am searching the data base using an algorithm that is just like quicksort -- divide and conquer...
    number = int(number)
    up_limit = end_row
    down_limit = 1
    #checking_row = int((up_limit + down_limit)/2)
    while up_limit - down_limit > 1:
        checking_row = int(round((up_limit + down_limit)/2))
        #BIG ERROR: I placed checking row at the end of the while loop, so even when the loop was supposed to be over, it still modified one last time checking row, fucking everything up
        # if int(worksheet.cell(checking_row,1).value) == number:
        #     worksheet.update_cell(checking_row, 2, int(worksheet.cell(checking_row,2).value) + 1)
        #     return 'successfully inserted ' + str(number) + ' at row of index ' + str(checking_row)
        
        #print('check ', checking_row, ' up ', up_limit, ' down ', down_limit)
        if int(worksheet.cell(checking_row,1).value) > number:
            up_limit = checking_row
        
        if int(worksheet.cell(checking_row,1).value) < number:
            down_limit = checking_row

#now, this leaves us with 3 more iterations, to make sure that we insert at the good place. 
    for i in range(checking_row-1 ,checking_row +2): 
        #print(range(checking_row-1, checking_row +2))   
        if int(worksheet.cell(i,1).value) > number:
            worksheet.insert_row([number, 1], index = (i))
            #when we insert a row, every row BEYONd the first row gets its index + 1
            #insert_row takes a 1D array
            return 'successfully inserted ' + str(number) + ' at row of index ' + str(i)
        
        # if int(worksheet.cell(i,1).value) == number:
        #     worksheet.update_cell(checking_row, 2, int(worksheet.cell(checking_row,2).value) + 1)
        #     return 'successfully inserted ' + str(number) + ' at row of index ' + str(i)


        

#------------------------
    #old version, when we used to use csv
    # from csv import writer

    # def append_list_as_row(file_name, list_of_elem):
    #   with open(file_name, 'a+', newline='') as write_obj:

    #         # Create a writer object from csv module
    #         csv_writer = writer(write_obj)

    #         # Add contents of list as last row in the csv file
    #         csv_writer.writerow(list_of_elem)

    # def add_num(number):
    #     if '+' in number:
    #         number = number.replace('+', '')
    #     if '-' in number:
    #         number = number.replace('-', '')
    #     if ')' in number:
    #         number = number.replace(')', '')
    #     if '(' in number:
    #         number = number.replace('(', '')
    #     if ' ' in number:
    #         number = number.replace(' ', '')
    #     append_list_as_row('unwanted_calls.csv', [number])