from sqlite3 import IntegrityError
from utils import validator
from user_module.models import User
from user_module.create_admin import create_admin_in_db


class CreateUserManager:
    @staticmethod
    def create_user(username, name, last_name, phone_number, country_code, password, email) -> (bool, str, User):
        # create admin
        create_admin_in_db()

        # checking required fields for empty value
        checking_result, checking_message = check_empty_required_fields(username=username,
                                                                        country_code=country_code,
                                                                        phone_number=phone_number,
                                                                        password=password)
        if checking_result is False:
            return False, checking_message, None

        # checking the username for matches in the database
        if is_username_already_exist(username=username):
            return False, "Username already exist.", None

        # checking the phone for matches in the database
        if is_phone_already_exist(phone_number=phone_number):
            return False, "Phone number already exist.", None
        else:
            # country_code and phone_number validation
            (phone_number_validation_result,
             phone_number_validation_message) = validator.utils_validate_phone_number(phone_number=phone_number,
                                                                                      country_code=country_code)
            if phone_number_validation_result is False:
                return False, phone_number_validation_message, None

        # checking the email for matches in the database
        if email is not None:
            if is_email_already_exist(email=email):
                return False, "Email already exist.", None
            else:
                # email validation
                email_validation_result, email_validation_message = validator.utils_validate_email(email=email)
                if email_validation_result is False:
                    return False, f"Email validation error - {email_validation_message}", None

        # trying to save user into database
        save_user_result, user = save_user(username=username,
                                           name=name,
                                           last_name=last_name,
                                           country_code=country_code,
                                           phone_number=phone_number,
                                           password=password,
                                           email=email)
        # user created
        if save_user_result:
            return True, "User created.", user
        # user creating error
        else:
            return False, "Creating user error.", None


def check_empty_required_fields(username, country_code, phone_number, password) -> (bool, str):
    if not username: return False, "No username value."
    if not country_code: return False, "No country code value."
    if not phone_number: return False, "No phone number value."
    if not password: return False, "No password value."

    return True, None


def is_phone_already_exist(phone_number) -> bool:
    return User.objects.filter(phone_number=phone_number).exists()


def is_email_already_exist(email) -> bool:
    return User.objects.filter(email=email).exists()


def is_username_already_exist(username) -> bool:
    return User.objects.filter(username=username).exists()


def save_user(username, name, last_name, country_code, phone_number, password, email) -> (bool, User):
    try:
        user = User(username=username,
                    name=name,
                    last_name=last_name,
                    country_code=country_code,
                    phone_number=phone_number,
                    password=password,
                    email=email)
        user.save()
        return True, user
    except IntegrityError:
        return False, None
