from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils import decoder
from .models import User


@csrf_exempt
def get_user(request):
    if request.method == 'GET':
        return JsonResponse({'type': 'SUCCESS', 'answer': ''})
    else:
        return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        # try to decode request data
        decode_result, data = decoder.decode(request, ['name', 'last_name', 'phone', 'password'])
        # decoding success
        if decode_result:
            # try to create new user
            user_creating_result, user_creating_message = User.manager.create_user(name=data.get('name', None),
                                                                                   last_name=data.get('last_name', None),
                                                                                   phone=data.get('phone', None),
                                                                                   password=data.get('password', None),
                                                                                   email=data.get('email', None))
            # user created
            if user_creating_result:
                return JsonResponse({'type': 'SUCCESS', 'answer': user_creating_message})
            # user creating failure
            else:
                return JsonResponse({'type': 'ERROR', 'answer': user_creating_message})
        # decoding failure
        else:
            return JsonResponse({'type': 'ERROR', 'answer': data})
    # wrong request method
    else:
        return JsonResponse({'type': 'ERROR', 'answer': 'Method not allowed.'})