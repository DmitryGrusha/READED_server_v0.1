from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .serializers import *

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                user = User.objects.get(username=serializer.data.get('username', None))
            except ObjectDoesNotExist:
                return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
            full_serializer = UserGetSerializer(user)
            return Response(full_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserById(APIView):
    def post(self, request):
        user_id = request.data.get('id', None)
        if user_id is None:
            return Response({'message': 'Missing "id" property in the request body.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserGetSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



from utils import decoder
from user_module.create_user import CreateUserManager

#
# @csrf_exempt
# def register_user(request):
#     if request.method == 'POST':
#         # try to decode request data
#         decode_result, data = decoder.utils_decode(request, ['username',
#                                                              'country_code',
#                                                              'phone_number',
#                                                              'password'])
#         # decoding success
#         if decode_result:
#             # try to create new user
#             (user_creating_result,
#              user_creating_message,
#              user) = CreateUserManager.create_user(username=data.get('username', None),
#                                                    name=data.get('name', None),
#                                                    last_name=data.get('last_name', None),
#                                                    country_code=data.get('country_code', None),
#                                                    phone_number=data.get('phone_number', None),
#                                                    password=data.get('password', None),
#                                                    email=data.get('email', None))
#             # user created
#             if user_creating_result:
#                 return JsonResponse({'user': {
#                                          'id': user.id,
#                                          'username': user.username,
#                                          'name': user.name,
#                                          'last_name': user.last_name,
#                                          'country_code': user.country_code,
#                                          'phone_number': user.phone_number,
#                                          'email': user.email}}, status=200)
#             # user creating failure
#             else:
#                 return JsonResponse({'message': user_creating_message}, status=400)
#         # decoding failure
#         else:
#             return JsonResponse({'message': data}, status=400)
#     # wrong request method
#     else:
#         return JsonResponse({'message': 'Method not allowed.'}, status=400)
#
# @csrf_exempt
# def get_user(request):
#     if request.method == 'POST':
#         decode_result, decode_message_or_data = decoder.utils_decode(request, [])
#         if decode_result:
#             result, serializable_user = db_manager.get_user_from_db(decode_message_or_data.get('id', None))
#             if result:
#                 return JsonResponse({'user': serializable_user}, status=200)
#             else:
#                 error_msg = serializable_user
#                 return JsonResponse({'message': error_msg}, status=400)
#         else:
#             return JsonResponse({'message': decode_message_or_data}, status=400)
#     else:
#         return JsonResponse({'message': 'Method not allowed.'}, status=400)