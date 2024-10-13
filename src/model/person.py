class Person:
    def __init__(self, person_id: int, name: str, age: int, emails: list):
        self.id = person_id
        self.name = name
        self.age = age
        self.emails = emails

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_emails(self):
        return self.emails
