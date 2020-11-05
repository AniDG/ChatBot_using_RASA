ChatBot 'Foodie' is a conversational bot (chatbot) which can help users discover restaurants across several Indian cities.
Cities can be Tier 1 and Tier 2.

It will work in the following steps:-
1.	Customers can select for which city, preferred cuisine and budget they want to fetch the search results for.

2.	The ChatBot will query Zomato API to fetch the results.

3.	It then asks the customer whether they want the email to be sent to them or not.

4.	If yes, it will ask for the email, and will send email to provided email address


Prerequisites:
Package					Version
------------------------------------
python					3.7.6
rasa                    1.10.14
rasa-sdk                1.10.3
rasa-x                  0.32.2
regex                   2020.6.8
requests                2.24.0
requests-oauthlib       1.3.0
requests-toolbelt       0.9.1
rocketchat-API          1.3.1
scikit-learn            0.22.2.post1
spacy                   2.1.9
en-core-web-md          2.1.0
tensorboard             2.1.1
tensorboard-plugin-wit  1.6.0
tensorflow              2.1.0
tensorflow-addons       0.7.1
tensorflow-estimator    2.1.0
tensorflow-hub          0.8.0
tensorflow-probability  0.9.0
ujson                   1.35
urllib3                 1.25.10


Files modified:

Data files:-
data/nlu.md
data/stories.md

Configuration files:-
config.yml
domain.yml
endpoints.yml
credentials.yml

Script files:-
actions.py
zomatopy.py

Email send screenshots:-
Email_Sent_Screenshot_1.png
Email_Sent_Screenshot_2.png
