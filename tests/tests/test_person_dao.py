import unittest
from src.dao.person_dao import PersonDAO
from src.model.person import Person
from src.model.email import Email

class TestPersonDAO(unittest.TestCase):
    def test_valid_person(self):
        person = Person(1, "John Doe", 25, [Email("john.doe@example.com")])
        dao = PersonDAO()
        errors = dao.is_valid_to_include(person)
        self.assertEqual(len(errors), 0)

    def test_invalid_name(self):
        person = Person(1, "John123", 25, [Email("john.doe@example.com")])
        dao = PersonDAO()
        errors = dao.is_valid_to_include(person)
        self.assertIn("Name must only contain letters.", errors)

    def test_invalid_age(self):
        person = Person(1, "John Doe", 300, [Email("john.doe@example.com")])
        dao = PersonDAO()
        errors = dao.is_valid_to_include(person)
        self.assertIn("Age must be between 1 and 200.", errors)

    def test_invalid_email(self):
        person = Person(1, "John Doe", 25, [Email("invalidemail")])
        dao = PersonDAO()
        errors = dao.is_valid_to_include(person)
        self.assertIn("Email must be in the correct format.", errors)

if __name__ == "__main__":
    unittest.main()
