class Subject:
    def __init__(self,subject):
        self.sub = subject().add_sub()
        self.name = subject().add_name()

class IPT:
    def add_sub(self):
        return IPTsub()
    def add_name(self):
        return IPTname()

class CC105:
    def add_sub(self):
        return CC105sub()
    def add_name(self):
        returnCC105name()

class IM101:
    def add_sub(self):
        return IM101sub()
    def add_name(self):
        return IM101name()

class MS102:
    def add_sub(self):
        return MS102sub()
    def add_name(self):
        return MS102name()

class IPTsub:
    def subject_type(self):
        return 'Integrative Programming and Technology'

class CC105sub:
    def subject_type(self):
        return 'Information Management'

class IM101sub:
    def subject_type(self):
        return 'Fundamentals of Database'

class MS102sub:
    def subject_type(self):
        return 'Quantitative Methods'

class IPTname:
    def subject_type(self):
        return 'IPT'

class CC105name:
    def subject_type(self):
        return 'CC105'

class IM101name:
    def subject_type(self):
        return 'IM101'

class MS102name:
    def subject_type(self):
        return 'MS102'


firstsubject = Subject(IPT)
print(firstsubject.sub.subject_type())
print(firstsubject.name.subject_type())

secondsubject = Subject(CC105)
print(secondsubject.sub.subject_type())
print(secondsubject.name.subject_type())

thirdsubject = Subject(IM101)
print(thirdsubject.sub.subject_type())
print(thirdsubject.name.subject_type
thirdsubject = Subject(MS102)
print(fourthsubject.sub.subject_type())
print(fourthsubject.name.subject_type

