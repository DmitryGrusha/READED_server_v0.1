from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils import decoder, db_manager
from user_module.create_user import CreateUserManager


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        # try to decode request data
        decode_result, data = decoder.utils_decode(request, ['username',
                                                             'country_code',
                                                             'phone_number',
                                                             'password'])
        # decoding success
        if decode_result:
            # try to create new user
            (user_creating_result,
             user_creating_message,
             user) = CreateUserManager.create_user(username=data.get('username', None),
                                                   name=data.get('name', None),
                                                   last_name=data.get('last_name', None),
                                                   country_code=data.get('country_code', None),
                                                   phone_number=data.get('phone_number', None),
                                                   password=data.get('password', None),
                                                   email=data.get('email', None))
            # user created
            if user_creating_result:
                return JsonResponse({'type': 'SUCCESS', 'answer': user_creating_message,
                                     'user': {
                                         'id': user.id,
                                         'username': user.username,
                                         'name': user.name,
                                         'last_name': user.last_name,
                                         'country_code': user.country_code,
                                         'phone_number': user.phone_number,
                                         'email': user.email}})
            # user creating failure
            else:
                return JsonResponse({'type': 'ERROR', 'answer': user_creating_message})
        # decoding failure
        else:
            return JsonResponse({'type': 'ERROR', 'answer': data})
    # wrong request method
    else:
        return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})


@csrf_exempt
def get_user(request):
    if request.method == 'POST':
        decode_result, decode_message_or_data = decoder.utils_decode(request, [])
        if decode_result:
            result, serializable_user = db_manager.get_user_from_db(decode_message_or_data.get('id', None))
            if result:
                return JsonResponse({'type': 'SUCCESS', 'answer': '',
                                     'user': serializable_user})
            else:
                error_msg = serializable_user
                return JsonResponse({'type': 'ERROR', 'answer': error_msg})
        else:
            return JsonResponse({'type': 'ERROR', 'answer': decode_message_or_data})
    else:
        return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})
