#I created this code to 
    #1 remove all duplicated numbers from the spam_number database
    #2 add the frequence of the appearances in the database of duplicate numbers
import pandas as pd

import gspread

gc = gspread.service_account(filename = "cred.json")
#this tells the gspread module where to look for the informations on our google sheet

sh = gc.open_by_key("1KmGQBAx4fD9fu3MdWsyKZfwQsoSqp6q0UBPdlkCpTsw")
#this is part of the link for the google sheet that contains the spam numbers

worksheet = sh.sheet1

#this basically gives me the length of the spread sheet
data = worksheet.get_all_values()

df = pd.DataFrame(data, columns = ["Number", "Frequence"])

#i made i=1 because i want to exclude the header 

temp_number = -1
temp_index = 1
i=0
try:
    while i < 35482:
        if int(df.iloc[i, 0]) != temp_number:
            temp_number = int(df.iloc[i,0])
            temp_index = i
            i= i+1
            #print(i, "first")

        if int(df.iloc[i, 0]) == temp_number:
            df.iloc[temp_index, 1] = int(df.iloc[temp_index, 1]) +1
            df.drop(index = i, inplace = True)
            #print(i, "second")
            #here, i don't want to add 1 to the index. The reason is that the .drop removes an index completely. Thus, if I added 1, it wouldn't check the value that had replaced the previous value.

        if i%10000 == 0:
            print("almost done")
        df.reset_index(drop = True, inplace = True)    
        
#i decided to use except, cuz i saw that my code was doing everything right until the end, and then, it didn't work, so yea
except:
    #here, i will be exporting my pandas dataframe into a csv
    df.to_csv('test.csv', header = False, index = False)
    print('You made it')

df.to_csv('test.csv', header = False, index = False)
print('You made it')

    #------------------------------------------------------------------
    #too many bugs, back to 0
    #these two prints show us that the the index used for pandas start at 0, while the index used for the gspread start at the conventionnal 1
    #to make these two values the same, i deccided to add 1 to the indexes for gspread dataframe, when gspread and pandas are equal 1, the gspread is actually equal the equivalent of 0
    # print(type(df.iloc[1, 1]), df.iloc[1,1])
    # print(type(worksheet.cell(1+1,1+1).value), worksheet.cell(1+1,1+1).value)

    # temp_value = 0
    # temp_index = 1
    # i = 1


    # #if i want to decrement the value of i, we cannot use a for loop, we must use a while loop, the for loop automatically increments the value of i.
    # try:
    #     while i < len(data):
    #         # print("Loop reset, index = ", i," temp_value = ", temp_value, "the real value at that index = ", df.iloc[i,0])
    #         if int(df.iloc[i,0]) != temp_value:
    #             # print(int(df.iloc[i,0]) != temp_value, "the value is not equal")
    #             # print(i, df.iloc[i, 0], temp_value)
    #             temp_value = int(df.iloc[i,0])
    #             temp_index = i
    #             #update_cell(row, column, new_value)   
    #             # print('temporary value was changed to ', type(temp_value), temp_value)
    #             # print(i, df.iloc[i, 0], temp_value)
            
    #         if int(df.iloc[i,0]) == temp_value:
    #             # print(int(df.iloc[i,0]) == temp_value, "the value is equal")   
    #             # print(i, df.iloc[i, 0], temp_value)
    #             df.iloc[temp_index, 1] = int(df.iloc[temp_index, 1]) + 1
    #             df.drop(index = i, inplace = True)
    #             df.reset_index(drop = True, inplace = True)
    #             # print(i, df.iloc[i, 0], temp_value)
    #     #     if int(worksheet.cell(i+1,1).value) != temp_value:
    #     #         worksheet.update_cell(i, 2, 1)
    #             # i=-1
    #         #     end_row =-1
    #         i+=1

    # except KeyError:
    #     print("something isn't right with the indexes") 
