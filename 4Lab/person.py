from datetime import datetime

class Person:
    def __init__(self, surname, name, birth_date):
        self.surname = surname
        self.name = name
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d')

    def age(self):
        return (datetime.now() - self.birth_date).days // 365