#input - json file with job description information
#processing - count each occurrence of word, not case sensitive (not including field names)
#output json file with each word getting its own field and having a value equal to its frequency

import json
import re
from collections import defaultdict
from datetime import datetime

# List of software development related keywords
keywords = ['python', 'java', 'c++', 'sql', 'javascript', 'linux', 'git', 'docker', 'agile', 'scrum']

#Remove extra spaces, newlines and convert to lower case.
def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip().lower()

#processes json file made by the scraper
def process_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        resumes = json.load(file)
    
    # Initialize a dictionary to hold keyword counts
    keyword_counts = defaultdict(int)

    # Process each resume
    for resume in resumes:
        # Extract relevant fields and clean them
        fields = [resume.get('title', ''), resume.get('description', ''), resume.get('job_description', '')]
        cleaned_text = ' '.join(clean_text(field) for field in fields)
        
        # Count the occurrences of each keyword
        for keyword in keywords:
            keyword_counts[keyword] += cleaned_text.count(keyword)

    write_output(keyword_counts)

#write keyword counts to a json file
def write_output(keyword_counts):
    output_data = dict(keyword_counts)
    # get current time and add to json file
    now = datetime.now()
    current_date_time = now.strftime("%Y-%m-%d %H-%M-%S")
    with open(f"parsed{current_date_time}.json", 'w') as file:
        json.dump(output_data, file, indent=4)