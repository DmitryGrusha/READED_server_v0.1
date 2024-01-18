from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import phonenumbers


def utils_validate_email(email) -> (bool, str):
    email_validator = EmailValidator()
    try:
        email_validator(email)
        return True, "Email is correct."
    except ValidationError as e:
        return False, "Wrong email address."


def utils_validate_phone_number(phone_number: str, country_code: str) -> (bool, str):
    full_phone_number = f"+{country_code}{phone_number}"
    try:
        parsed_number = phonenumbers.parse(full_phone_number)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        if is_valid:
            return True, "SUCCESS"
        else:
            return False, "Phone number of country code is not valid."
    except phonenumbers.NumberParseException:
        return False, "Invalid characters in phone number or country code."
