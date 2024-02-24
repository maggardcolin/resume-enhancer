# input - processed json file
# processing, finding top keywords
# output - even more processed json file

# author: Colin Maggard

import json, nltk, os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime

def process_data(file_path, category):
    nltk.download('stopwords')
    nltk.download('punkt') 

    with open(file_path, 'r') as file:
        data = json.load(file)

    accepted_words = []

    for field in data:
        processed_text = remove_stop_words(field)
        if processed_text:
            accepted_words.append({"text": processed_text, "value": data[field]})

    # get current time and add to json file name
    now = datetime.now()
    current_date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
    with open(f"./output/{category}_keyword_output_{current_date_time}.json", 'w') as file:
        json.dump(accepted_words, file, indent = 4)
    os.remove(file_path)

# Function to remove stop words
def remove_stop_words(text):
    # Load stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_text = [word for word in words if not word.lower() in stop_words]
    return ' '.join(filtered_text)
