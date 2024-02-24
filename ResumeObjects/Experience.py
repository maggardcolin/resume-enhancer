class Experience:
    def __init__(self, company, role_title, location, duration, description, delimiter):
        self.company = company
        self.role_title = role_title.split(delimiter)
        self.location = location
        self.duration = duration
        self.description = description.split(delimiter)

    def get_company(self):
        return self.company

    def get_role(self):
        return self.role_title

    def get_location(self):
        return self.location

    def get_duration(self):
        return self.duration

    def get_description(self):
        return self.description
