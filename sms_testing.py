from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#import pygsheets
    #this module lets us access information and data coming from the google spread sheets
    #ok, so pygsheets is just a newer verion of gspread. BRUH!
    #https://medium.com/game-of-data/play-with-google-spreadsheets-with-python-301dd4ee36eb

#ok,i decided to use gspread
#NEVERMIND, it is better to use pygsheets
import gspread
    #https://medium.com/@vince.shields913/reading-google-sheets-into-a-pandas-dataframe-with-gspread-and-oauth2-375b932be7bf

import pandas as pd

#https://oauth2client.readthedocs.io/en/latest/source/oauth2client.service_account.html

def message_rating(message):
    #here, instead of using the method proposed in the website i will just be recopying the method that i used for spam_update.py
    gc = gspread.service_account(filename = "cred.json")
    #this tells the gspread module where to look for the informations on our google sheet

    sh = gc.open_by_key("1sCqJsDP_CWZCboWy9W5mDqxyuIjPqIP3MEFvw3276xs")
    #this is part of the link for the google sheet that contains the spam messages

    worksheet = sh.sheet1
    # this tells the module which sheet that we want (because we only have one sheet, we can just write sheet #1)

    data = worksheet.get_all_values()
    #this function transforms the google sheet into a pandas dataframe that i will name data
    #make sure that we have the same number of columns in the spread sheet and in the declaration later on

    headers = data.pop(0)

#because i have previously decl
    messages = pd.DataFrame(data, columns = ["rating", "message"])

#old code:
    #df = pd.read_csv('spam.csv')
    #messages = pd.DataFrame(df, columns=['rating', 'message'])

    message_train = messages['message']
    rating_train = messages['rating']

    model = CountVectorizer()
    #create a dictionary with value of position of word

    transformed_message_train = model.fit_transform(message_train)
    #create a matrix with frequency of a word and the word

    Multi = MultinomialNB()
    Multi.fit(transformed_message_train, rating_train)

    test_counts = model.transform([message])

    final = Multi.predict(test_counts)
    chances = round((float(Multi.predict_proba(test_counts)[0][1]*100)),5)

    #print(final,type(final),chances,type(chances))

#Prediction is numpy array, another conditionnal to return a string

    if final == 'spam':
        return_statement = 'This message is spam. This message has a probability of {0}% of being spam.'.format(chances)
        final_arg = 'spam'
    else:
        return_statement = 'This message is not spam. This message has a probability of {0}% of being spam.'.format(chances)
        final_arg = 'ham'

#I removed the spam update program. I'll put later to see if it works on Android:
#If we export as APK, then we must export the database of spam messages for Bayes.

    return [str(return_statement), final_arg]
