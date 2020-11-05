
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - action_validate_location
* restaurant_search{"cuisine": "chinese", "location": "kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_2
* greet
	- utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
    - utter_ask_location_tier2
* affirm
	- slot{"location": "asansol"}
    - action_validate_location
	- utter_ask_cuisine
	- slot{"cuisine": "chinese"}
	- action_validate_cuisine
	- utter_ask_budget
	- slot{"price_min": 300}
	- slot{"price_max": 700}
	- action_validate_budget
	- utter_ask_email_send_or_not
	- utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
	- action_validate_email
	- action_send_email
	- utter_goodbye