# author: Colin Maggard, Atiksh Shah

import pandas as pd
from ResumeObjects import *

def scoreResume(file_path, my_resume):
    key_count = 0
    json_data = file_path
    df = pd.read_json(json_data)
    word_list = df.values.tolist()
    printStatements = False
    matched_words = []

    for i in range(len(word_list)):
        keyword = word_list[i][0]
        activities = my_resume.activities
        experiences = my_resume.experiences
        projects = my_resume.projects

        if keyword in my_resume.objective:
            if printStatements:
                print(keyword + " matched!")
            key_count += 1
            matched_words.append(keyword)
        if keyword in my_resume.skills:
            if printStatements:
                print(keyword + " matched!")
            key_count += 1
            matched_words.append(keyword)
        for activity in activities:
            for line in activity.description:
                if keyword in line:
                    if printStatements:
                        print(keyword + " matched!")
                    key_count += 1
                    matched_words.append(keyword)
            if keyword in activity.role_title:
                if printStatements:
                    print(keyword + " matched!")
                key_count += 1
                matched_words.append(keyword)
            if keyword in activity.organization:
                if printStatements:
                    print(keyword + " matched!")
                key_count += 1
                matched_words.append(keyword)
        for experience in experiences:
            for line in experience.description:
                if keyword in line:
                    if printStatements:
                        print(keyword + " matched!")
                    key_count += 1
                    matched_words.append(keyword)
            if keyword in experience.role_title:
                if printStatements:
                    print(keyword + " matched!")
                key_count += 1
                matched_words.append(keyword)
            if keyword in experience.company:
                if printStatements:
                    print(keyword + " matched!")
                key_count += 1
                matched_words.append(keyword)
        for project in projects:
            if keyword in project.description:
                if printStatements:
                    print(keyword + " matched!")
                key_count += 1
                matched_words.append(keyword)
            
    print("\n" + str(key_count) + " matches found. Let's shoot for more!")
    print("Here are the top 10 matched words for job descriptions matching your query: ")
    printed_keywords = 0  # Counter for printed keywords
    for i in range(len(word_list)):
        if printed_keywords >= 10:
            break
        keyword = word_list[i][0]
        if keyword not in matched_words:
            match_count = word_list[i][1]
            if (printed_keywords + 1 < 10):
                extra_space = " "
            else:
                extra_space = ""
            print(str(printed_keywords + 1) + f"){extra_space} \"" + keyword + f"\" with {match_count} matches")
            printed_keywords += 1
