# input - processed json file
# processing, finding top keywords
# output - processed even more json file

import json, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime

def process_data(file_path):
    nltk.download('stopwords')
    nltk.download('punkt') 

    with open(file_path, 'r') as file:
        data = json.load(file)

    accepted_words = []

    for field in data:
        processed_text = remove_stop_words(field)
        if processed_text:
            accepted_words.append(processed_text)

    # get current time and add to json file name
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    with open(f"./output/filtered{current_date_time}.json", 'w') as file:
        json.dump(accepted_words, file, indent = 4)

# Function to remove stop words
def remove_stop_words(text):
    # Load stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_text = [word for word in words if not word.lower() in stop_words]
    return ' '.join(filtered_text)
