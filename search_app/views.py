# # search_app/views.py
# from django.http import JsonResponse
# import json
# import os

# def search_users(request):
#     query = request.GET.get('q', '').lower()
#     json_path = os.path.join(os.path.dirname(__file__), 'user_list.json')

#     with open(json_path) as f:
#         users = json.load(f)

#     filtered_users = [
#         user for user in users
#         if query in user['first_name'].lower() or query in user['last_name'].lower()
#     ]

#     if filtered_users:
#         return JsonResponse({'results': filtered_users}, status=200)
#     else:
#         return JsonResponse({'message': 'No results found'}, status=404)

from django.http import JsonResponse
import json
import os

def search_users(request):
    query = request.GET.get('q', '').lower()
    json_path = os.path.join(os.path.dirname(__file__), 'user_list.json')

    with open(json_path) as f:
        users = json.load(f)

    filtered_users = [
        user for user in users
        if query in user['first_name'].lower() or query in user['last_name'].lower()
    ]

    if filtered_users:
        return JsonResponse({'results': filtered_users}, status=200)
    else:
        return JsonResponse({'message': 'No results found'}, status=404)

