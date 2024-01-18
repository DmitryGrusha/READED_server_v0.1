import json


def utils_decode(request, keys_array):
    try:
        data = json.loads(request.body.decode('utf-8'))

        for key in keys_array:
            if key not in data:
                return False, 'Missing fields'

        return True, data
    except json.JSONDecodeError:
        return False, 'Invalid JSON format.'
