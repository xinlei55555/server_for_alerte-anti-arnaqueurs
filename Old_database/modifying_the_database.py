#I created this code to 
    #1 remove all duplicated numbers from the spam_number database
    #2 add the frequence of the appearances in the database of duplicate numbers
import time
#this is so that i can respect the limit of google spread sheets

import gspread

gc = gspread.service_account(filename = "cred.json")
#this tells the gspread module where to look for the informations on our google sheet

sh = gc.open_by_key("1-94dkK4IAUjTJtmokQ3MC83HKaiaNEcFQZiOc5-0toU")
#this is part of the link for the google sheet that contains the spam numbers

worksheet = sh.sheet1

#this basically gives me the length of the spread sheet
all = worksheet.get_all_values()
end_row = len(all) + 1

#print(type(int(worksheet.cell(2,1).value)))

temp_value = int(worksheet.cell(2,1).value)
# temp_index = 2
temp_frequence = 1

print(type(worksheet.cell(16,2).value))

#we have to start the range at 2, because at 0, there is nothing, at 1, there is the column name
#for i in range(2, end_row):
# if i want to decrement the value of i, we cannot use a for loop, we must use a while loop, the for loop automatically increments the value of i.
i = 2
while str(type(worksheet.cell(i,2).value)) != str("<class'NoneType'>"):
        i +=1

while i < end_row:
    if int(worksheet.cell(i,2).value) > 0:
        temp_frequence = int(worksheet.cell(i, 2).value) 

    if int(worksheet.cell(i,1).value) != temp_value:
        temp_value = int(worksheet.cell(i,1).value)
        # temp_index = i
#update_cell(row, column, new_value)
        temp_frequence = 1
        worksheet.update_cell(i, 2, temp_frequence)
        # print('temporary value was changed to ', type(temp_value), temp_value)
        
    if int(worksheet.cell(i+1,1).value) == temp_value:
        temp_frequence += 1
        worksheet.update_cell(i, 2, temp_frequence)
        worksheet.delete_rows(i+1)
        i-=1

    if int(worksheet.cell(i+1,1).value) != temp_value:
        worksheet.update_cell(i, 2, 1)
       
    # time.sleep(2.5)
    i+=1



