from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import requests
import json
import re
import pandas as pd

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

import requests
import json

class ActionValidateLocation(Action):
    def name(self):
        return 'action_validate_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')

        # Restaurant search 
        base_url = "https://developers.zomato.com/api/v2.1/"
        headers = {'Accept': 'application/json', 'user-key': '2571df5d87374d79b42cd9744efec6a0'}

        r = (requests.get(base_url + "locations?query=" + str(loc), headers=headers).content).decode("utf-8")

        d1 = json.loads(r)

        if d1['location_suggestions'] == 0:
            dispatcher.utter_message("Unfortunately, we do not operate in this area yet. Please try with some other location.")
            return [SlotSet('location',None)]
        else:
            return [SlotSet('location',loc)]


class ActionValidateCuisine(Action):
    def name(self):
        return 'action_validate_cuisine'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"2571df5d87374d79b42cd9744efec6a0"}
        zomato = zomatopy.initialize_app(config)
        cuisine = tracker.get_slot('cuisine')
        cuisine_list = ["chinese","north indian","south indian","american","italian","mexican"]
        if cuisine.lower() in cuisine_list:
            return [SlotSet('cuisine',cuisine)]
        else:
            dispatcher.utter_message("Unfortunately we do not serve this cuisine")
            return [SlotSet('cuisine',None)]


class ActionValidateBudget(Action):
    def name(self):
        return 'action_validate_budget'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"2571df5d87374d79b42cd9744efec6a0"}
        zomato = zomatopy.initialize_app(config)
        price_min = tracker.get_slot('price_min')
        price_max = tracker.get_slot('price_max')
        
        if price_max > price_min:
            # Do operation
            return [SlotSet('price_min',price_min)],[SlotSet('price_max',price_max)]
        else:
            dispatcher.utter_message("Budget range not defined correctly.") 
            return [SlotSet('price_min',None)],[SlotSet('price_max',None)]
        

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price_min = int(tracker.get_slot('price_min'))
        price_max = int(tracker.get_slot('price_max'))

        # Restaurant search 
        base_url = "https://developers.zomato.com/api/v2.1/"
        headers = {'Accept': 'application/json', 'user-key': '2571df5d87374d79b42cd9744efec6a0'}

        r = (requests.get(base_url + "locations?query=" + str(loc), headers=headers).content).decode("utf-8")

        location_json = json.loads(r)
        location_results = len(location_json['location_suggestions'])
        lat=location_json["location_suggestions"][0]["latitude"]
        lon=location_json["location_suggestions"][0]["longitude"]

        cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}
        cuisines = str(cuisines_dict[cuisine])

        headers = {'Accept': 'application/json', 'user-key': '2571df5d87374d79b42cd9744efec6a0'}
        r = (requests.get(base_url + "search?q=" + str('') + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(cuisines), headers=headers).content).decode("utf-8")

        d1 = json.loads(r)
        d = d1['restaurants']

        df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                            'restaurant_address': x['restaurant']['location']['address'],
                            'budget_for2people': x['restaurant']['average_cost_for_two'],
                            'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating']} for x in d])
        df2 = df1.loc[(df1['budget_for2people']>=price_min) & (df1['budget_for2people']<=price_max),:] 
        df2 = df2.sort_values(['restaurant_rating','budget_for2people'],ascending=[False,True])
        df2 = df2.reset_index(drop=True)
        df2 = df2.head()

        response=""
        if len(df2) == 0:
            response= "Unfortunately,we could not find any restaurant based on your criteria."
        else:
            for index,restaurant in df2.iterrows():
                response = response+restaurant['restaurant_name']+ " in "+ str(restaurant['restaurant_address'])+" has been rated "+restaurant['restaurant_rating']+". \n"
        
        dispatcher.utter_message(response)
        return[SlotSet('location',loc)]


class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"2571df5d87374d79b42cd9744efec6a0"}
        zomato = zomatopy.initialize_app(config)
        email = tracker.get_slot('email')
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.search(pattern,email):
            return [SlotSet('email',email)]
        else:
            dispatcher.utter_message("Please enter a valid email.")
            return [SlotSet('email',None)]
        


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"2571df5d87374d79b42cd9744efec6a0"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price_min = int(tracker.get_slot('price_min'))
        price_max = int(tracker.get_slot('price_max'))

        # Restaurant search 
        location_detail=zomato.get_location(loc, 1)

        base_url = "https://developers.zomato.com/api/v2.1/"
        headers = {'Accept': 'application/json', 'user-key': '2571df5d87374d79b42cd9744efec6a0'}

        r = (requests.get(base_url + "locations?query=" + str(loc), headers=headers).content).decode("utf-8")

        d1oc = json.loads(location_detail)
        lat=d1oc["location_suggestions"][0]["latitude"]
        lon=d1oc["location_suggestions"][0]["longitude"]

        cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}
        cuisines = str(cuisines_dict[cuisine])
 
        r = (requests.get(base_url + "search?q=" + str('') + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(cuisines), headers=headers).content).decode("utf-8")
        d1 = json.loads(r)
        d = d1['restaurants']
        df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                            'restaurant_address': x['restaurant']['location']['address'],
                            'budget_for2people': x['restaurant']['average_cost_for_two'],
                            'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating']} for x in d])
        df2 = df1.loc[(df1['budget_for2people']>=price_min) & (df1['budget_for2people']<=price_max),:] 
        df2 = df2.sort_values(['restaurant_rating','budget_for2people'],ascending=[False,True])
        df2 = df2.reset_index(drop=True)

        email = tracker.get_slot('email')
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.search(pattern,email):
            # Send Email
            gmail_user = 'chatbot.upgrad.assignment@gmail.com'
            gmail_password = 'chatbot123'

            sent_from = gmail_user
            to = email
            
            msg = MIMEMultipart()
            msg['From'] = gmail_user
            msg['To'] = email
            msg['Subject'] = 'Top 10 Restaurant Details of '+cuisine+" food in "+loc
            
            if len(df2) == 0:
                # No Restaurant
                html = """\
                        <html>
                          <head></head>
                          <body>
                           <p>Hi </p>
                           <p>Thanks for contacting Foodie.</p>
                           <p>Unfortunately,we could not find any restaurant based on your criteria.</p>
                          </body>
                        </html>
                        """
            else:
                # Restaurant Found [Consider Top 10 Records]
                df_10 = df2.head(10)
 
                html = """\
                        <html>
                          <head></head>
                          <body>
                           <p>Hi </p>
                           <p>Thanks for contacting Foodie.</p>
                           <p> Please find the search results below.</p>
                            {0}
                           <p> Please visit again!
                           <p> Thanks and regards
                           <p> Foodie
                          </body>
                        </html>
                        """.format(df_10.to_html())

            part1 = MIMEText(html, 'html')
            msg.attach(part1)

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, msg.as_string())
                server.close()

                dispatcher.utter_message("Email has been sent to the address provided by you")

            except:
                dispatcher.utter_message("Please enter a valid email.")

        else:
            dispatcher.utter_message("Please enter a valid email.")
