#here are two links that really did help
#https://www.youtube.com/watch?v=n2aQ6QOMJKE&ab_channel=SessionWithSumit
#

import gspread
#this module lets us enter data into the google spread sheet

gc = gspread.service_account(filename = "cred.json")
#this tells the gspread module where to look for the informations on our google sheet

sh = gc.open_by_key("1sCqJsDP_CWZCboWy9W5mDqxyuIjPqIP3MEFvw3276xs")
#this is part of the link for the google sheet that contains the spam messages

worksheet = sh.sheet1
# this tells the module which sheet that we want (because we only have one sheet, we can just write sheet #1)

def spam_update(message, analysed_rating):
  # this should change the value of the analysed_rating
  if analysed_rating == 'spam':
    worksheet.append_row(["ham", message])
    #this should add a row in the sheet
  else:
    worksheet.append_row(["spam", message])
  print("successfully added message and corrected error")

def add_message(message, verdict):
  if verdict == 'spam':
    worksheet.append_row(["spam", message])
    #this should add a row in the sheet

  else:
    worksheet.append_row(["ham", message])
  print("successfully added message")


#Test message:


#------------------------
#old version, when we used to use csv

#!/usr/bin/python3

# from csv import writer
# import pandas as pd

# df = pd.read_csv('spam.csv')
# messages = pd.DataFrame(df, columns=['rating', 'message'])
# print(messages)

# def append_list_as_row(file_name, list_of_elem):
#   with open(file_name, 'a+', newline='') as write_obj:

#         # Create a writer object from csv module
#         csv_writer = writer(write_obj)

#         # Add contents of list as last row in the csv file
#         csv_writer.writerow(list_of_elem)

# def spam_update(message, analysed_rating):
#   if analysed_rating[0] == 'spam':
#     append_list_as_row('spam.csv', ['ham', message + ',,,'])
#   else:
#     append_list_as_row('spam.csv', ['spam', message + ',,,'])

# def add_message(message, verdict):
#   if verdict[0] == 'spam':
#     append_list_as_row('spam.csv', ['spam', message + ',,,'])
#   else:
#     append_list_as_row('spam.csv', ['ham', message + ',,,'])
