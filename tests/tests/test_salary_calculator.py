
import unittest
from src.model.employee import Employee
from src.service.salary_calculator import SalaryCalculator

class TestSalaryCalculator(unittest.TestCase):
    def test_developer_salary_above_3000(self):
        employee = Employee("John", "john@example.com", 3500, "desenvolvedor")
        calculator = SalaryCalculator()
        salary = calculator.calculate_salary(employee)
        self.assertEqual(salary, 3500 * 0.8)

    def test_dba_salary_below_2000(self):
        employee = Employee("Jane", "jane@example.com", 1800, "DBA")
        calculator = SalaryCalculator()
        salary = calculator.calculate_salary(employee)
        self.assertEqual(salary, 1800 * 0.85)

    def test_manager_salary_above_5000(self):
        employee = Employee("Alice", "alice@example.com", 6000, "gerente")
        calculator = SalaryCalculator()
        salary = calculator.calculate_salary(employee)
        self.assertEqual(salary, 6000 * 0.7)

if __name__ == "__main__":
    unittest.main()
