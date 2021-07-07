import gspread
#this module lets us enter data into the google spread sheet

gc = gspread.service_account(filename = "cred.json")
#this tells the gspread module where to look for the informations on our google sheet

sh = gc.open_by_key("1fRTG968E91rLvPs9TCVf1Z9c1q6opwVNccd8EpY7O8Y")
#this is part of the link for the google sheet that contains the spam numbers

worksheet = sh.sheet1
# this tells the module which sheet that we want (because we only have one sheet, we can just write sheet #1)

def add_num(number):
  #this adds the number to the spam number database
    worksheet.append_row([number])
   


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