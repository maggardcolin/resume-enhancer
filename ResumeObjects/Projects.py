class Project:
    def __init__(self, name, languages_used, description, delimiter):
        self.name = name
        self.languages = languages_used
        self.description = description.split(delimiter)

    def get_name(self):
        return self.name

    def get_language(self):
        return self.languages

    def get_description(self):
        return self.description
