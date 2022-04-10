from typing import Any,Text,Dict,List
from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

class ApiAction(Action):
    def name(self):
        return "action_get_news"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]):
        category = tracker.get_slot("category")
        print(category)

        url = 'https://api.nytimes.com/svc/news/v3/content/all/{category}.json'.format(category=category)
        params = {'api-key': "2hq54bvFO0yWiRdY70reBU2GmusBtnwM", 'limit': 5}
        response = requests.get(url,params).text
        json_data = json.loads(response)["results"]
        i = 0
        for results in json_data:
            i+=1
            message = f"{str(i)}.{results['abstract']}"
            dispatcher.utter_message(message)
        return []