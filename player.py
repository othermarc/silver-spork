class player:
    """docstring for """
    def __init__(self, name, grade, isMember = False):
        self.name = name
        self.isMember = isMember
        self.grade = grade

    def getGrade(self):
        return self.grade

    def getName(self):
        return self.name

    def getIsMember(self):
        return self.isMember

    
