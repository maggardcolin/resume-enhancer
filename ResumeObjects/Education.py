class Education:
    def __init__(self, degree, date, location, gpa, description, delimiter):
        self.degree = degree
        self.date = date
        self.location = location
        self.gpa = gpa
        self.description = description.split(delimiter)
    def getDegree(self):
        return self.degree
    def getDate(self):
        return self.degree
    def getLocation(self):
        return self.location
    def getGPA(self):
        return self.gpa
    def getDescription(self):
        return self.description