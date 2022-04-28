class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
        self.total_marks = 300
    def totalObtained(self):
        self.total = self.phy+self.chem+self.bio
        return self.total

    def percentage(self):
        self.percent = (self.total*100)/self.total_marks
        return self.percent

student = Student("Hritu", 80, 90, 40)
print("Total marks obtained by " , student.name ,student.totalObtained())
print("Percentage obtained by ", student.name , student.percentage())


