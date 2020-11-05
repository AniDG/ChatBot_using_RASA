
## interactive_story_1
* greet
    - utter_greet
    - utter_about
    - utter_ask_location_tier

## interactive_story_2
* greet
    - utter_about
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "700"}
    - slot{"price_min": "700"}
    - utter_ask_email_send_or_not
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_2
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier1
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_3
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier2
* restaurant_search{"location": "Durgapur"}
    - slot{"location": "Durgapur"}
    - action_validate_location
    - slot{"location": "Durgapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - action_search_restaurants
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_4
* greet
    - utter_about
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Dakshineswar"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Dakshineswar"}
    - action_validate_location
    - slot{"location": "Dakshineswar"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - utter_ask_email_send_or_not
* email_received{"email": "heymavik@gmail.com"}
    - slot{"email": "heymavik@gmail.com"}
    - action_validate_email
    - slot{"email": "heymavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_5
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier2
* restaurant_search{"location": "Asansol"}
    - slot{"location": "Asansol"}
    - action_validate_location
    - slot{"location": "Asansol"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - action_search_restaurants
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye
	
## interactive_story_6
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier2
* restaurant_search{"location": "Kolhapur"}
    - slot{"location": "Kolhapur"}
    - action_validate_location
    - slot{"location": "Kolhapur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - action_search_restaurants
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye
	
## interactive_story_7
* greet
    - utter_about
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Bhopal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bhopal"}
    - action_validate_location
    - slot{"location": "Bhopal"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - utter_ask_email_send_or_not
* email_received{"email": "heymavik@gmail.com"}
    - slot{"email": "heymavik@gmail.com"}
    - action_validate_email
    - slot{"email": "heymavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_8
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier2
* restaurant_search{"location": "Indore"}
    - slot{"location": "Indore"}
    - action_validate_location
    - slot{"location": "Indore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - action_search_restaurants
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye
	
## interactive_story_9
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier2
* restaurant_search{"location": "Meerut"}
    - slot{"location": "Meerut"}
    - action_validate_location
    - slot{"location": "Meerut"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - action_search_restaurants
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_10
* greet
    - utter_about
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Purulia"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Purulia"}
    - action_validate_location
    - slot{"location": "Dakshineswar"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - utter_ask_email_send_or_not
* email_received{"email": "heymavik@gmail.com"}
    - slot{"email": "heymavik@gmail.com"}
    - action_validate_email
    - slot{"email": "heymavik@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_11
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier2
* restaurant_search{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - action_validate_location
    - slot{"location": "Shimla"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - action_search_restaurants
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye
	
## interactive_story_12
* greet
    - utter_about
    - utter_greet
* restaurant_search
    - utter_ask_location_tier
* mood_unhappy
    - utter_ask_location_tier2
* restaurant_search{"location": "Vellore"}
    - slot{"location": "Vellore"}
    - action_validate_location
    - slot{"location": "Vellore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price_min": "300", "price_max": "700"}
    - slot{"price_max": "700"}
    - slot{"price_min": "300"}
    - action_validate_budget
    - action_search_restaurants
    - utter_ask_email_send_or_not
* affirm
    - utter_ask_for_email
* email_received{"email": "anindyavik@gmail.com"}
    - slot{"email": "anindyavik@gmail.com"}
    - action_validate_email
    - slot{"email": "anindyavik@gmail.com"}
    - action_send_email
    - utter_goodbye