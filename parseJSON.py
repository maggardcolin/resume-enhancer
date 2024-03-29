#input - json file with job description information
#processing - count each occurrence of word, not case sensitive (not including field names)
#output json file with each word getting its own field and having a value equal to its frequency

# author: Colin Maggard, Shorya Haziza

import json, re, os
from collections import defaultdict
from datetime import datetime
from dataWrangler import *

# remove whitespace and convert to lower case.
def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip().lower()

# processes json file made by the scraper
def process_json(file_path, category):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        jobs = json.load(file)
    
    # Initialize a dictionary to hold keyword counts
    keyword_counts = defaultdict(int)

    # Process each job listing
    for job in jobs:
        # Extract relevant fields and clean them
        fields = [job.get('job_title', ''), job.get('description', '')]
        cleaned_text = ' '.join(clean_text(field) for field in fields)
        
        # Count the occurrences of each keyword, split by whitespace, commas, parentheses, etc
        keywords = re.split(r'\W+', cleaned_text)
        for keyword in keywords:
            if keyword:
                keyword_counts[keyword] += 1

    the_final_file = write_output(keyword_counts, category)
    os.remove(file_path)
    return the_final_file

# write keyword counts to a json file
def write_output(keyword_counts, category):
    # sort the fields
    output_data = dict(sorted(keyword_counts.items(), key = lambda item: item[1], reverse = True))
    # get current time and add to json file name
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    with open(f"./output/parsed{current_date_time}.json", 'w') as file:
        json.dump(output_data, file, indent = 4)
    the_final_file = process_data(f"./output/parsed{current_date_time}.json", category)
    return the_final_file