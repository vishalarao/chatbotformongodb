# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from flask import Flask,request
from flask_mongoalchemy import MongoAlchemy

app=Flask(__name__)
 
app.config["MONGOALCHEMY_DATABASE"]="User"
db=MongoAlchemy(app)

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class Users(db.Document):
    username=db.StringField()
    password=db.StringField()
    admin=db.BoolField()

class ActionInform(Action):

    def name(self) -> Text:
        return "action_inform"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        util = Utils()
        response = util.get_users(tracker.get_slot('person'))    
        dispatcher.utter_message(response)
        return [SlotSet('person', None)]

class Utils():
    def get_users(self,person=None):
        response='"Below are the user details:\n'
        if person:
            users=Users.query.filter(Users.username==person).all()
            if users:
                for user in users:
                    response = response + 'Username: {}, Admin:{}\n'.format(user.username,user.admin)
                return response
            else:
                return 'Username {} is not present in our database'.format(person)
        else:
            return 'Please provide a username'