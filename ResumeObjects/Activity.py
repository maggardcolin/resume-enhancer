class Activity:
    def __init__(self, organization, location, role_title, description, delimiter):
        self.organization = organization
        self.location = location
        self.role_title = role_title.split(delimiter)
        self.description = description.split(delimiter)

    def get_organization(self):
        return self.organization

    def get_location(self):
        return self.location

    def get_role(self):
        return self.role_title

    def get_description(self):
        return self.description
