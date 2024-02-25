import pandas as pd
from ResumeObjects import *

def scoreResume(file_path, my_resume):
    key_count = 0
    json_data = file_path
    df = pd.read_json(json_data)
    my_list = df.values.tolist()
    for i in range(len(my_list)):
        keyword = my_list[i][0]
        activities = my_resume.activities
        experiences = my_resume.experiences
        projects = my_resume.projects
        
        if keyword in my_resume.objective:
            print(keyword + " matched!")
            key_count += 1
        if keyword in my_resume.skills:
            print(keyword + " matched!")
            key_count += 1
        for activity in activities:
            if keyword in activity.get_description():
                print(keyword + " matched!")
                key_count += 1
            if keyword in activity.get_role():
                print(keyword + " matched!")
                key_count += 1
            if keyword in activity.get_organization():
                print(keyword + " matched!")
                key_count += 1
        for experience in experiences:
            if keyword in experience.get_description():
                print(keyword + " matched!")
                key_count += 1
            if keyword in experience.get_role():
                print(keyword + " matched!")
                key_count += 1
            if keyword in experience.get_company():
                print(keyword + " matched!")
                key_count += 1
        for project in projects:
            if keyword in project.description:
                print(keyword + " matched!")
                key_count += 1
            if keyword in activity.languages:
                print(keyword + " matched!")
                key_count += 1
    print(key_count)    