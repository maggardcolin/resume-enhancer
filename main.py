# author: Colin Maggard, Atiksh Shah

import subprocess, sys, os
# install needed modules
try:
    import selenium
except ImportError:
    print("'selenium' is not installed. Please wait while it is installed...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
    import selenium
try:
    import nltk
except ImportError:
    print("'nltk' is not installed. Please wait while it is installed...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nltk"])
    import nltk
try:
    import docx
except ImportError:
    print("'nltk' is not installed. Please wait while it is installed...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    import docx
from scrapeIndeed import searchJobs
from resume import Resume
from scoring import scoreResume

# displays the menu
def display_menu():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print("Add Content to Resume")
    command = None
    while (command is None):
        try:
            command = int(input("[1]: Add Education \n[2]: Add Professional Experience \
                \n[3]: Add Activity \n[4]: Add Project\n[5]: Add Skills\n[6]: Export Resume \
                \n[7]: Quit\n"))
        except:
            print("Please enter an integer.")
    if command == 1:
        add_edu()
        display_menu()
    elif command == 2:
        add_exp()
        display_menu()
    elif command == 3:
        add_act()
        display_menu()
    elif command == 4:
        add_proj()
        display_menu()
    elif command == 5:
        add_skill()
        display_menu()
    elif command == 6:
        my_resume.compile_resume()
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    elif command == 7:
        print("Thank you for using the resume builder.")
    else:
        print("No command entered")
        display_menu()

# add an education
def add_edu():
    # university name 
    college = input("Please enter your college/university name: ")
    # prompt for location
    college_location = input("Please enter the city and state of your school (e.g. 'Madison, WI): ")
    # prompt for degree
    degree = input("Please enter your degree name (e.g. Bachelor of Science in Computer Engineering): ")
    # prompt for expected grad month/year
    grad = input("Please enter your graduation month and year (e.g. 'May 2026'): ")
    # prompt for gpa
    gpa = input("Please enter your current GPA/total possible GPA (e.g '3.90/4.00'): ")
    # prompt for description
    description = input("Please enter any additional fields you would like to display, using '@' to separate each line: ")
    my_resume.add_education(degree, grad, college, college_location, gpa, description, delimiter="@")

# add an experience
def add_exp():   
    company = input("Enter name of employer: ")
    role_title = input("Enter your role title: ")
    exp_location = input("Enter the city and state of your experience (e.g 'Madison, Wisconsin'): ")
    duration = input("Enter the time frame in which you were employed (e.g 'August 2023 - December 2024'): ")
    description = input("Please enter the description of this experience using '@' to separate each bullet point: ")
    my_resume.add_experience(company, role_title, exp_location, duration, description, delimiter = "@")

# add an activity
def add_act():
    org = input("Enter organization name: ")
    role_title = input("Enter your role title: ")
    act_location = input("Enter the city and state of your activity (e.g 'Madison, Wisconsin'): ")
    description = input("Please enter your description using '@' to separate each bullet point: ")
    my_resume.add_activity(org, act_location, role_title, description, delimiter = "@")

# add a project
def add_proj():
    project_name = input("Enter project name: ")
    langs = input("Enter any technologies/languages used (e.g 'Java, Python, C'): ")
    description = input("Please enter the description of this project using '@' to separate the bullet points: ")
    my_resume.add_project(name, langs, description, delimiter = "@")

# add skills
def add_skill():
    skills = input("Please enter your skills, separated by commas (e.g 'Python, Java, React'): ")
    my_resume.add_skills(skills)

# global vars
links = ""
skills = ""
objective = ""

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("Welcome to Resume Creator!")

#personal info at the top of resume
#prompts input for full name
name = input("Please enter your full name: ")
# prompts input for city
city = input("Please enter your city: ")
# prompts input for state
state = input("Please enter your state abbreviation (e.g. WI): ")
# prompts input for email
email = input("Please enter your email: ")
# prompts input for number
phone = input("Please enter your phone number: ")
# prompts input for amount of links
linkscnt = -1
# handles if linkscnt isn't an integer
while linkscnt < 0:
    try: 
        linkscnt = int(input("How many links would you like to have in your resume in the info section?: "))
    except ValueError:
        print("Invalid integer, please enter a number.")
#prompts input for all links for linkscnt worth of links
for i in range(1, linkscnt + 1):
    link = input(f"Please provide link #{i}: ")
    links = links + link
    if (i != linkscnt):
        links += " | "

obj_consent = None
while obj_consent is None:
    try:
        obj_consent = input("Would you like to add an objective statement (y/n): ")
        # prompts input for the objective section
    except:
        print("enter True or False")
    if obj_consent == "y":
        objective = input("Please input your objective statement (a brief, targeted statement that clearly communicates the purpose of your resume): ")
    else:
        print("")

# inits the resume object
my_resume = Resume(name, city, state, email, phone, objective, links)
display_menu()

#basically entire backend
job = input("Finally, what type of job are you trying to apply for? ")
the_final_file = searchJobs(job)

# data analysis
scoreResume(the_final_file, my_resume)

my_resume.compile_resume().save(f"./output/{name}_Resume.docx")