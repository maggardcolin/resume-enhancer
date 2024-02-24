links = []
college = ""
degree = ""
experience = []
projects = []
skills = ""

print("Welcome to Resume Creator!")

#personal info at the top

#prompts input for full name
name = input("Please enter your full name: ")
#prompts input for city
city = input("Please enter your city: ")
#prompts input for state
state = input("Please enter your state: ")
#prompts input for email
email = input("Please enter your email: ")
#prompts input for number
phone = input("Please enter your number: ")
#prompts input for amount of links
linkscnt = input("How many links would you like to have in your resume (integer)?: ")
#prompts input for all links for linkscnt worth of links
for i in range(linkscnt):
    link = input("Please provide your shortened link: ")
    links.append(link)

#prompts input for the objective section
objective = input("Please input your objective/summary \
about youself (a brief, targeted statement that \
clearly communicates the purpose of your resume): ")

#prompts for the education section
#prompt for college
educnt = input("Please enter the number of educations you would like to list (integer): ")
for i in range(educnt):
    college = input("Please enter your college/university name: ")
    #prompt for degree
    degree = input("Please enter your degree or degrees as it would appear in a transcript: ")
    #prompt for expected grad month/year
    grad = input("Please enter your expected graduation date (e.g. 'May 2026'): ")
    #prompt for gpa
    gpa = input("Please enter your GPA (e.g '3.90/4.00'): ")
    #prompt for description
    description = input("Please enter your description using commas to separate your bullet points: ")


