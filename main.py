 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import coinmarketcap
import os
import sys
reload(sys)
crypto = 'bitcoin'
sys.setdefaultencoding('utf8')
app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
quitkeywords = ['quit', 'exit', 'cancel', 'leave']

@ask.launch

def new_game():
    print "here"

    welcome_msg = render_template('welcome', crypto = crypto)

    return question(welcome_msg)


@ask.intent("YesIntent", convert={'yon': str})
def next_round(yon):
    print yon
    round_msg = render_template('round_msg', crypto = crypto)
    help = render_template('help', crypto = crypto)
    if yon == 'help':
        print "here"
        return question(help)
    if yon in quitkeywords:
        return statement("")
    return question(round_msg)

        

@ask.intent("AnswerIntent")

def answer():
        price = coinmarketcap.price(crypto)
        priceresponse = render_template('priceresponse', crypto = crypto , price = price)
        return statement(priceresponse) \
            .simple_card(title='Bitcoin Price', content="The " + crypto + " price is " + price)
@ask.session_ended
def session_ended():
    return statement("")
def run():
    app.run(debug=True)
run()
