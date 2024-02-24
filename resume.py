from ResumeObjects import Activity, Education, Experience, Projects
from docx import Document

class Resume:
    def __init__(self):
        self.activities = []
        self.experiences = []
        self.educations = []
        self.projects = []
        self.skills = ""

    def addEducation(self, degree, date, location, gpa, description, delimiter):
        pass

    def addActivity(self, organization, location, role_title, description , delimiter):
        a1 = Activity(organization, location, role_title, description, delimiter)
        self.activities.append(a1)

    def addExperience(self, company, role_title, location, duration, description, delimiter):
        e1 = Experience(company, role_title, location, duration, description, delimiter)
        self.experiences.append(e1)

    def addProject(self, name, languages_used, description, delimiter):
        p1 = Projects(name, languages_used, description, delimiter)
        self.projects.append(p1)

    def addSkills(self, skill):
        self.skills = self.skills + ", " + skill

    def compileResume(self):
        doc = Document()
        p = doc.add_paragraph("test")
        p
        doc.save("test.docx")

if __name__ == '__main__':
    res = Resume()
    res.compileResume()
