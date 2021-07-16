import phonenumbers
from phonenumbers import geocoder
import pandas as pd

from search_number import search_number

def call_location(number):
    if '+' in number:
        num = number
    else:
        num = '+' + number

    try:
        x = phonenumbers.parse(num, None)
        location = geocoder.description_for_number(x, 'en')
    except phonenumbers.phonenumberutil.NumberParseException:
        return ['Invalid number.', '']
    
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

    if not location:
        if list(str(number))[1:4] == ['8', '3', '3'] or list(str(number))[1:4] == ['8', '4', '4'] or list(str(number))[1:4] == ['8', '5', '5'] \
                or list(str(number))[1:4] == ['8', '8', '8'] or list(str(number))[1:4] == ['8', '6', '6'] or list(str(number))[1:4] == ['8', '0', '0']\
                or list(str(number))[1:4] == ['8', '7', '7']:
            return [number + " is a toll-free scam number.", 'spam']

    if location == 'Quebec':
        number1 = list(str(number))
        # this means the number comes from canada or the u.s.
        if number1[1:4] == ['5', '1', '4'] or number1[1:4] == ['4', '3', '8']:
            # this means the number is from montreal
            location = "Montreal, QC"
        if number1[1:4] == ["3", "5", "4"] or number1[1:4] == ['4', '5', '0'] \
                or number1[1:4] == ['5', '7', '9']:
            location = "Montreal Suburbs, QC"
        if number1[1:4] == ['4', '1', '8'] or number1[1:4] == ['5', '8', '1'] \
                or number1[1:4] == ['3', '6', '7']:
            location = "Quebec East, QC"
        if number1[1:4] == ['8', '1', '9'] or number1[1:4] == ['8', '7', '3']:
            # this means that the number is from quebec
            location = "Quebec North or West, QC"

#this has been moved to the search_number.py file
    # df = pd.read_csv('unwanted_calls.csv')
    # numbs = pd.DataFrame(df)

    # for ele in numbs['Number']:
    #     numb = str(ele).replace('-', '')
    #     if numb == '' or numb == 'None':
    #         continue
    #     else:
    #         if number == numb:
    #             if not location:
    #                 return [number + " has been previously marked spam.", 'spam']
    #             else:
    #                 return [number + " is from " + location + '. ' + "This number has been previously marked spam.", 'spam']

#these return the good thing based on if the number was marked spam or nah
    number_of_times_the_number_was_marked = search_number(number)
    if number_of_times_the_number_was_marked != 0:
        if location:
            return [number + " is from " + location + '. ' + "This number has been previously marked spam by " + str(number_of_times_the_number_was_marked) + ' users.', 'spam']
        return [number + " has been previously marked spam by " + str(number_of_times_the_number_was_marked) + ' users.', ' spam']

    else:
        if location:
            return [number + " is from " + location + '.', 'ham']
        return ["Cannot find the location.", '']

# print(call_location("1(514)857-3943)"))