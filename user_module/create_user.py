from sqlite3 import IntegrityError
from utils import validator
from user_module.models import User


class CreateUserManager:
    @staticmethod
    def create_user(username, name, last_name, phone_number, country_code, password, email):
        # checking required fields for empty value
        checking_result, checking_message = check_empty_required_fields(username=username,
                                                                        country_code=country_code,
                                                                        phone_number=phone_number,
                                                                        password=password)
        if checking_result is False:
            return False, checking_message

        # checking the username for matches in the database
        if is_username_already_exist(username=username):
            return False, "Username already exist."

        # checking the phone for matches in the database
        if is_phone_already_exist(phone_number=phone_number):
            return False, "Phone number already exist."
        else:
            # country_code and phone_number validation
            (phone_number_validation_result,
             phone_number_validation_message) = validator.utils_validate_phone_number(phone_number=phone_number,
                                                                                      country_code=country_code)
            if phone_number_validation_result is False:
                return False, phone_number_validation_message

        # checking the email for matches in the database
        if email is not None:
            if is_email_already_exist(email=email):
                return False, "Email already exist."
            else:
                # email validation
                email_validation_result, email_validation_message = validator.utils_validate_email(email=email)
                if email_validation_result is False:
                    return False, f"Email validation error - {email_validation_message}"

        # trying to save user into database
        save_user_result, save_user_message = save_user(username=username,
                                                        name=name,
                                                        last_name=last_name,
                                                        country_code=country_code,
                                                        phone_number=phone_number,
                                                        password=password,
                                                        email=email)
        # user created
        if save_user_result:
            return True, save_user_message
        # user creating error
        else:
            return False, save_user_message


def check_empty_required_fields(username, country_code, phone_number, password) -> (bool, str):
    if not username: return False, "No username value."
    if not country_code: return False, "No country code value."
    if not phone_number: return False, "No phone number value."
    if not password: return False, "No password value."

    return True, ""


def is_phone_already_exist(phone_number) -> bool:
    return User.objects.filter(phone_number=phone_number).exists()


def is_email_already_exist(email) -> bool:
    return User.objects.filter(email=email).exists()


def is_username_already_exist(username) -> bool:
    return User.objects.filter(username=username).exists()


def save_user(username, name, last_name, country_code, phone_number, password, email) -> (bool, str):
    try:
        user = User(username=username,
                    name=name,
                    last_name=last_name,
                    country_code=country_code,
                    phone_number=phone_number,
                    password=password,
                    email=email)
        user.save()
        return True, "User created."
    except IntegrityError:
        return False, "Creating user error."
