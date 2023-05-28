from account import Account
from password_verifier import PasswordVerifier


class DetailsVerifier(Account, PasswordVerifier):
    def check_username_exists(self, username):
        # Check if username already exists in the database
        return self.unique_userName(username)

    def check_email_exists(self, email):
        # Check if email already exists in the database
        return self.unique_email(email)

    def check_phone_exists(self, phone):
        # Check if phone number already exists in the database
        return self.unique_phone(phone)

    def password_valid(self, password):
        # Check if password is valid (e.g. more than 6 characters, contains upper/lower case)
        if not self.is_minimum_length(password):
            raise Exception(
                "Password must be at least {} characters long".format(
                    self.MINIMUM_PASSWORD_LENGTH))
        if not self.has_uppercase(password):
            raise Exception(
                "Password must contain at least one uppercase letter")
        if not self.has_lowercase(password):
            raise Exception(
                "Password must contain at least one lowercase letter")
        if not self.has_digit(password):
            raise Exception("Password must contain at least one digit")

        return True

    def verify_details_for_register(self, username, email, phone, password):
        # Verify if username, email, phone number, and password are valid
        if self.check_username_exists(username) and self.check_email_exists(email) and self.check_phone_exists(phone):
            raise Exception("Username, Email, and Phone number already exist")
        elif self.check_username_exists(username) and self.check_email_exists(email):
            raise Exception("Username and Email already exist")
        elif self.check_username_exists(username) and self.check_phone_exists(phone):
            raise Exception("Username and Phone number already exist")
        elif self.check_email_exists(email) and self.check_phone_exists(phone):
            raise Exception("Email and Phone number already exist")
        elif self.check_username_exists(username):
            raise Exception("Username already exists")
        elif self.check_email_exists(email):
            raise Exception("Email already exists")
        elif self.check_phone_exists(phone):
            raise Exception("Phone number already exists")
        elif not self.password_valid(password):
            raise Exception("Password not valid")
        else:
            return True

    def verify_details_for_edit_info(self, email, phone, password):
        # Verify if email, phone number, and password are valid
        if self.check_email_exists(email) and self.check_phone_exists(phone):
            raise Exception("Email and Phone number already exist")
        elif self.check_email_exists(email):
            raise Exception("Email already exists")
        elif self.check_phone_exists(phone):
            raise Exception("Phone number already exists")
        elif not self.password_valid(password):
            raise Exception("Password not valid")
        else:
            return True
