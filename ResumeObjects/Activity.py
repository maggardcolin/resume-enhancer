class Activity:
    def __init__(self, organization, location, role_title, description, delimiter):
        self.organization = organization
        self.location = location
        self.role_title = role_title.split(delimiter)
        self.description = description.split(delimiter)
