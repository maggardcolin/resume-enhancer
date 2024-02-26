# input - processed json file
# processing, finding top keywords
# output - even more processed json file

# author: Colin Maggard

import json, nltk, os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from datetime import datetime
from bannedwords import banned_words

def process_data(file_path, category):

    # download natural language toolkit packages if not on computer
    nltk.download('stopwords', quiet = True, raise_on_error = True)
    nltk.download('punkt', quiet = True, raise_on_error = True)

    with open(file_path, 'r') as file:
        data = json.load(file)

    accepted_words = []
    wordsCompleted = 1

    print("\nAnalyzing your resume...")
    print_progress_bar(wordsCompleted, len(data), prefix = 'Progress:', suffix = 'Complete', length = 50)

    for field in data:
        processed_text = remove_stop_words(field)
        if processed_text:
            if not any(banned_word in processed_text for banned_word in banned_words):
                accepted_words.append({"text": processed_text, "value": data[field]})
        wordsCompleted += 1        

    # get current time and add to json file name
    now = datetime.now()
    current_date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
    with open(f"./output/{category}_keyword_output_{current_date_time}.json", 'w') as file:
        json.dump(accepted_words, file, indent = 4)
    os.remove(file_path)
    return (f"./output/{category}_keyword_output_{current_date_time}.json")

# Function to remove stop words
def remove_stop_words(text):
    # Load stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_text = [word for word in words if not word.lower() in stop_words]
    return ' '.join(filtered_text)

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    if iteration == total: 
        print()