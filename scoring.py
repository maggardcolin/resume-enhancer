import pandas as pd

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
        
        if keyword in my_resume.skills:
            key_count += 1
        for activity in activities:
            if keyword in activity.get_description():
                key_count += 1
            if keyword in activity.get_role():
                key_count += 1
            if keyword in activity.get_organization():
                key_count += 1
        for experience in experiences:
            if keyword in experience.get_description():
                key_count += 1
            if keyword in experience.get_role():
                key_count += 1
            if keyword in experience.get_company():
                key_count += 1
        for project in projects:
            if keyword in project.description:
                key_count += 1
            if keyword in activity.languages:
                key_count += 1
    print(key_count)    