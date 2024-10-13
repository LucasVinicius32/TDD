
class Employee:
    def __init__(self, name: str, email: str, base_salary: float, role: str):
        self.name = name
        self.email = email
        self.base_salary = base_salary
        self.role = role

    def get_base_salary(self):
        return self.base_salary

    def get_role(self):
        return self.role
