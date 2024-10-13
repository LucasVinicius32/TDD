import re

class PersonDAO:
    def is_valid_to_include(self, person):
        errors = []
        name_parts = person.get_name().split(" ")
        if len(name_parts) < 2:
            errors.append("Name must have at least 2 parts.")
        if not all(part.isalpha() for part in name_parts):
            errors.append("Name must only contain letters.")
        if not (1 <= person.get_age() <= 200):
            errors.append("Age must be between 1 and 200.")

        if not person.get_emails():
            errors.append("Person must have at least one email.")
        else:
            for email in person.get_emails():
                if not re.match(r"\S+@\S+\.\S+", email.get_name()):
                    errors.append("Email must be in the correct format.")

        return errors
