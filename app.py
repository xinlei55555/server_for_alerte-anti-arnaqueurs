#!/usr/bin/python3

from flask import Flask, jsonify
from flask import render_template
from flask import request
from call_location import call_location
from add_number import add_num
from spam_update import add_message
from sms_testing_old import message_rating

#FOR RATING: 3 possibilities: spam, ham, empty string
#empty string = cannot find location or invalid number, dont return any icon in flutter
#for flutter: verify sender's number with phonenumber call_location module

app = Flask(__name__)

@app.route("/")
def home():
  data = {"title": "HELOOO"}
  return jsonify(data)

@app.route("/phonenumber") #take number as variable
def send_number():
  number = request.args.get('number') #between () is name of variable
  result = call_location(number)    #call location returns a list with title being result, rating being ham, spam or empty string
  print(result)
  send_number = {'title': result[0], 'rating': result[1]}
  return jsonify(send_number)

@app.route("/message")
def send_message():
  sms = request.args.get('sms')
  result = message_rating(sms)
  send_message = {'title': result[0], 'rating': result[1]}
  return jsonify(send_message)

@app.route("/addmessage")
def message_add():
  sms = request.args.get('sms')
  rating = request.args.get('rating')
  add_message(sms, rating)
  message_add = {'title': sms + ' was successfully added as ' + rating}
  return jsonify(message_add)


@app.route("/addphonenumber")
def phonenumber_add():
  number = request.args.get('number')
  add_num(number)
  phonenumber_add = {'title': number + ' was successfully added'}
  return jsonify(phonenumber_add)
  
if __name__ == "__main__":
  app.run()