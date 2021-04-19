from flask import Flask, jsonify
from flask import request
from call_location import call_location
from add_number import add_num
from spam_update import add_message
from sms_testing_old import message_rating

# import all functions

app = Flask(__name__)

@app.route("/")
def home():
    data = {"userId": 1, "id": 1, "title": "0000000000000000HELOOOOOOOOOOOOOOOOOOOOOOOOOO"}
    return jsonify(data)


# link/phonenumber?number=.......&sender=.........

# TASK: MAKE 2 NEW LINKS FOR UPDATING UNWANTED_CALLS AND SPAM CSV, LINK FOR SPAM_UPDATE HAS 2 VARIABLES: MESSAGE AND RATING
# LINK FOR ADD_NUMBER TAKES THE PHONE NUMBER AS THE VARIABLE

# jsonify phonenumber

@app.route("/phonenumber")  # take number as variable
def send_number():
    number = request.args.get('number')  # between () is name of variable
    send_number = {'title': call_location(number)}
    return jsonify(send_number)


@app.route("/message")  # take message as variable
def send_message():
    sms = request.args.get('sms')  # between () is name of variable
    send_message = {'title': message_rating(sms)}
    return jsonify(send_message)


@app.route("/addmessage")
def message_add():
    sms = request.args.get('sms')
    rating = request.args.get('rating')
    add_message(sms, rating)
    message_add = {'title': sms + ' and ' + rating + ' was successfully added'}
    return jsonify(message_add)


@app.route("/addphonenumber")
def phonenumber_add():
    number = request.args.get('number')
    add_num(number)
    phonenumber_add = {'title': number + ' was successfully added'}
    return jsonify(phonenumber_add)


if __name__ == "__main__":
    app.run()