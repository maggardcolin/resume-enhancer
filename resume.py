from ResumeObjects import Activity, Education, Experience, Project
from docx import Document


class Resume:
    def __init__(self, name, contact, objective):
        self.name = name
        self.contact = contact
        self.objective = objective
        self.activities = []
        self.experiences = []
        self.educations = []
        self.projects = []
        self.skills = ""

    def add_education(self, degree, date, location, gpa, description, delimiter):
        e1 = Education.Education(degree, date, location, gpa, description, delimiter)
        self.educations.append(e1)

    def add_activity(self, organization, location, role_title, description, delimiter):
        a1 = Activity.Activity(organization, location, role_title, description, delimiter)
        self.activities.append(a1)

    def add_experience(self, company, role_title, location, duration, description, delimiter):
        e1 = Experience.Experience(company, role_title, location, duration, description, delimiter)
        self.experiences.append(e1)

    def add_project(self, name, languages_used, description, delimiter):
        p1 = Project.Project(name, languages_used, description, delimiter)
        self.projects.append(p1)

    def add_skills(self, skill):
        self.skills = self.skills + ", " + skill

    def compile_resume(self):
        doc = Document()
        name = doc.add_paragraph(self.name)
        contact_info = doc.add_paragraph(self.contact)


        doc.save("test.docx")


if __name__ == '__main__':
    res = Resume("name", "npastore@wisc.edu | 224-634-8752", "I want to be a CS major lol")
    res.compile_resume()
