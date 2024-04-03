'''from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionMovieSearch(Action):
    def name(self) -> Text:
        return "action_movie_search"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']
        
        # Use model to find the movie
        new_doc = preprocess_string(user_message)
        test_doc_vector = model.infer_vector(new_doc)
        sims = model.dv.most_similar(positive=[test_doc_vector])
        
        # Get first 5 matches
        movies = [df['Title'].iloc[s[0]] for s in sims[:5]]
        
        if movies:
            bot_response = f"I found the following movies: {movies}"
        else:
            bot_response = "I couldn't find any movies matching your query."
        
        dispatcher.utter_message(text=bot_response)
        return []'''

from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from gensim.models import Word2Vec,Doc2Vec
from gensim.parsing.preprocessing import preprocess_string

from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionMovieSearch(Action):
    def name(self) -> Text:
        return "action_movie_search"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message['text']
        model = Word2Vec.load(r'C:\Users\vamsi\Documents\COMP-5313-WA - Artificial Intelligence\moviechatbot\actions\my_movie_plots_doc2vec.model')
        df = pd.read_csv(r'C:\Users\vamsi\Documents\COMP-5313-WA - Artificial Intelligence\moviechatbot\actions\wiki_movie_plots_deduped', sep=',', usecols=['Release Year', 'Title', 'Plot'])
        df = df[df['Release Year'] >= 2000]
        
        # Use model to find the movie
        new_doc = preprocess_string(user_message)
        test_doc_vector = model.infer_vector(new_doc)
        sims = model.dv.most_similar(positive=[test_doc_vector])
        
        # Get first 5 matches
        movies = [df['Title'].iloc[s[0]] for s in sims[:5]]
        
        if movies:
            bot_response = f"I found the following movies: {movies}"
        else:
            bot_response = "I couldn't find any movies matching your query."
        
        dispatcher.utter_message(text=bot_response)
        
        return [SlotSet("movie_search_performed", True)]  # Returning a slot indicating the action was performed
