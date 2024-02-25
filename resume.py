from ResumeObjects import Activity, Education, Experience, Project
from docx import Document
from docx.shared import Pt
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn

name_pt = Pt(24)
body_pt = Pt(12)
section_header_pt = Pt(16)
section_space_pt = Pt(5)
font = 'Calibri'


# Stolen from stackoverflow https://stackoverflow.com/questions/39006878/python-docx-add-horizontal-line
def insert_hr(paragraph):
    p = paragraph._p  # p is the <w:p> XML element
    pPr = p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    pPr.insert_element_before(pBdr,
                              'w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap',
                              'w:overflowPunct', 'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
                              'w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind',
                              'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
                              'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap',
                              'w:outlineLvl', 'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr',
                              'w:pPrChange'
                              )
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'auto')
    pBdr.append(bottom)


def format_run(run, pt, bold=False, italic=False):
    run.font.name = 'Calibri'
    run.font.size = pt
    run.font.bold = bold
    run.font.italic = italic


class Resume:
    def __init__(self, name, city, state, email, number, objective, links):
        # string
        self.name = name
        # string
        self.email = email
        # string
        self.number = number
        # list of strings
        self.links = links
        # strings
        self.city = city
        # strings
        self.state = state
        # strings
        self.objective = objective
        self.activities = []
        self.experiences = []
        self.educations = []
        self.projects = []
        self.skills = ""

    def add_education(self, degree, date, location, gpa, description, delimiter=","):
        e1 = Education.Education(degree, date, location, gpa, description, delimiter)
        self.educations.append(e1)

    def add_activity(self, organization, location, role_title, description, delimiter=","):
        a1 = Activity.Activity(organization, location, role_title, description, delimiter)
        self.activities.append(a1)

    def add_experience(self, company, role_title, location, duration, description, delimiter=","):
        e1 = Experience.Experience(company, role_title, location, duration, description, delimiter)
        self.experiences.append(e1)

    def add_project(self, name, languages_used, description, delimiter=","):
        p1 = Project.Project(name, languages_used, description, delimiter)
        self.projects.append(p1)

    def add_skills(self, skill):
        self.skills = self.skills + ", " + skill

    def compile_resume(self):
        doc = Document()
        namep = doc.add_paragraph()
        name = namep.add_run(self.name)
        name.font.name = font
        name.font.size = name_pt
        name.font.bold = True
        namep.paragraph_format.space_after = section_space_pt
        insert_hr(namep)

        contactp = doc.add_paragraph()
        contact_field = self.city + ", " + self.state + " | " + self.email
        if len(self.links) != 0:
            contact_field = contact_field + " | " + self.links

        contact = contactp.add_run(contact_field)

        contact.font.name = font
        contact.font.size = body_pt
        contactp.paragraph_format.space_after = section_space_pt

        objective_paragraph = doc.add_paragraph()
        objective = objective_paragraph.add_run("Objective")
        format_run(objective, section_header_pt, bold=True)
        objective_paragraph.paragraph_format.space_after = Pt(0)

        objective_description_paragraph = doc.add_paragraph()
        objective_description = objective_description_paragraph.add_run(self.objective)
        objective_description_paragraph.paragraph_format.space_after = section_space_pt
        format_run(objective_description, body_pt)

        if len(self.educations) != 0:
            education_header_paragraph = doc.add_paragraph()
            education_header = education_header_paragraph.add_run("Education")
            format_run(education_header, section_header_pt, bold=True)
            education_header_paragraph.paragraph_format.space_after = Pt(0)
            for education in self.educations:
                education.import_to_doc(doc, body_pt)

        if len(self.experiences) != 0:
            experience_header_paragraph = doc.add_paragraph()
            experience_header_paragraph.paragraph_format.space_before = section_space_pt
            experience_header_paragraph.paragraph_format.space_after = Pt(0)
            experience_header = experience_header_paragraph.add_run("Experience")
            format_run(experience_header, section_header_pt, bold=True)
            for exp in self.experiences:
                exp.import_to_doc(doc, body_pt)

        if len(self.activities) != 0:
            activity_header_paragraph = doc.add_paragraph()
            activity_header_paragraph.paragraph_format.space_after = Pt(0)
            activity_header_paragraph.paragraph_format.space_before = section_space_pt
            header = "Activities"
            if len(self.activities) == 1:
                header = "Activity"
            activity_header = activity_header_paragraph.add_run(header)
            format_run(activity_header, section_header_pt, bold=True)
            for activity in self.activities:
                activity.import_to_doc(doc, body_pt)

        if len(self.projects) != 0:
            project_header_paragraph = doc.add_paragraph()
            project_header_paragraph.paragraph_format.space_before = section_space_pt
            project_header_paragraph.paragraph_format.space_after = Pt(0)
            project_header = project_header_paragraph.add_run("Projects")
            format_run(project_header, section_header_pt, bold=True)
            for project in self.projects:
                project.import_to_doc(doc, body_pt)

        return doc


if __name__ == '__main__':
    res = Resume("Nicholas Pastore", "Madison", "Wisconsin", "npastore@wisc.edu", "224-634-8752",
                 "I want to be a cs major", "links")
    edu = Education.Education("Bachelors of Science in Computer Science", "May 2027",
                              "University of Wisconsin - Madison", "4.0/4.0",
                              "Programming I - III,Intro to ML Research", ",")
    res.educations.append(edu)

    res.add_experience("Cinemark", "Assitant Manager", "Barrington, IL", "August 2018 - August 2023",
                       "Responsible for overseeing the effective completion of crew member tasks.;Train new crew members on various skills required for their job.;Compile and verify nightly deposits.;Mediate and handle guest concerns.",
                       ";")

    res.add_project("Resume Builder", "Python", "somethingidk,something else idk")

    res.add_activity("maddata", "Madison, WI", "Hackathon Participant", "test,test,test")

    res.compile_resume().save("test.docx")
