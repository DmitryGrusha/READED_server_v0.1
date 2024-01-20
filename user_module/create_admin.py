def create_admin_in_db():
    from user_module.create_user import save_user
    if is_admin_already_exist() is False:
        save_user(username='Admin',
                  name='Admin',
                  last_name='Adminovich',
                  country_code='380',
                  phone_number='999999999',
                  password='password',
                  email=None)

def is_admin_already_exist() -> bool:
    from user_module.models import User
    return User.objects.filter(id=1).exists()