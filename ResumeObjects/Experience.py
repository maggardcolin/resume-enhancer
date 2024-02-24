class Experience:
    def __init__(self, company, role_title, location, duration, description, delimiter):
        self.company = company
        self.role_title = role_title.split(delimiter)
        self.location = location
        self.duration = duration
        self.description = description.split(delimiter)
    def getCompany(self):
        return self.company
    def getRole(self):
        return self.role_title
    def getLocation(self):
        return self.location
    def getDuration(self):
        return self.duration
    def getDescription(self):
        return self.description