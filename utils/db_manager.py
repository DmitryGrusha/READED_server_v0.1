from user_module.models import User


def get_user_from_db(user_id):
    try:
        user = User.objects.get(pk=user_id)
        serialized_user = {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'last_name': user.last_name,
            'country_code': user.country_code,
            'phone_number': user.phone_number,
            'email': user.email
        }
        return True, serialized_user
    except:
        return False, "Serialization error."
