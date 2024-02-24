class Project:
    def __init__(self, name, languages_used, description, delimiter):
        self.name = name
        self.languages = languages_used
        self.description = description.split(delimiter)
    def getName(self):
        return self.name
    def getLanguage(self):
        return self.languages
    def getDescription(self):
        return self.description
