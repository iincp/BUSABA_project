import re

class PasswordVerifier:
    MINIMUM_PASSWORD_LENGTH = 6
    def is_minimum_length(self, password):
        return len(password) >= PasswordVerifier.MINIMUM_PASSWORD_LENGTH

    def has_uppercase(self, password):
        return not password.islower()

    def has_lowercase(self, password):
        return not password.isupper()

    def has_digit(self, password):
        return bool(re.search(r'\d', password))

