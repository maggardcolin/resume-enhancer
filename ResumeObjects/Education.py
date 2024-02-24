class Education:
    def __init__(self, degree, date, location, gpa, description, delimiter):
        self.degree = degree
        self.date = date
        self.location = location
        self.gpa = gpa
        self.description = description.split(delimiter)

    def get_degree(self):
        return self.degree

    def get_date(self):
        return self.degree

    def get_location(self):
        return self.location

    def get_gpa(self):
        return self.gpa

    def get_description(self):
        return self.description
