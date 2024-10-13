class SalaryCalculator:
    def calculate_salary(self, employee):
        base_salary = employee.get_base_salary()
        role = employee.get_role().lower()

        if role == "desenvolvedor":
            return base_salary * 0.8 if base_salary >= 3000 else base_salary * 0.9
        elif role in ["dba", "testador"]:
            return base_salary * 0.75 if base_salary >= 2000 else base_salary * 0.85
        elif role == "gerente":
            return base_salary * 0.7 if base_salary >= 5000 else base_salary * 0.8
        else:
            return base_salary
