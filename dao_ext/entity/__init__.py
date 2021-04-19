class Student:
    def __init__(self, id_, name, age, sex):
        self.id_ = id_
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return "%s->%s(%s)" % (self.name, self.age, self.sex)

    def __repr__(self):
        return self.__str__()
