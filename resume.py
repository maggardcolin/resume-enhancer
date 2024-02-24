from ResumeObjects import Activity
from ResumeObjects import Experience
from ResumeObjects import Projects
activities = []
experiences = []
educations = []
projects = []
skills = ""
def addEducation(degree, date, location, gpa, description, delimiter):
    pass

def addActivity(organization, location, role_title, description , delimiter):
    a1 = Activity(organization, location, role_title, description, delimiter)
    activities.append(a1)

def addExperience(company, role_title, location, duration, description, delimiter):
    e1 = Experience(company, role_title, location, duration, description, delimiter)
    experiences.append(e1)

def addProject(name, languages_used, description, delimiter):
    p1 = Projects(name, languages_used, description, delimiter)
    projects.append(p1)

def addSkills(skill):
    skills += skill
    
def compileResume():
    print("ble")