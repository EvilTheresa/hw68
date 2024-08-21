import json
from json import JSONDecodeError

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
def add(request, *args, **kwargs):
    if request.method == 'GET':
        my_dict = {
            "A": int(5),
            "B": int(5),
        }
        response = JsonResponse(my_dict)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data.get("A")
            b = data.get("B")
            if isinstance(a, int) and isinstance(b, int):
                answer = a + b
                return JsonResponse({'answer': answer})
            else:
                return JsonResponse({'error': 'Numbers only!'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        response = HttpResponseNotAllowed(permitted_methods=["GET", "POST"])

    return response


def subtract(request):
    if request.method == 'GET':
        my_dict = {
            "A": int(5),
            "B": int(5),
        }
        response = JsonResponse(my_dict)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data.get("A")
            b = data.get("B")
            if isinstance(a, int) and isinstance(b, int):
                answer = a - b
                return JsonResponse({'answer': answer})
            else:
                return JsonResponse({'error': 'Numbers only!'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        response = HttpResponseNotAllowed(permitted_methods=["GET", "POST"])

    return response


def multiply(request):
    if request.method == 'GET':
        my_dict = {
            "A": int(5),
            "B": int(5),
        }
        response = JsonResponse(my_dict)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data.get("A")
            b = data.get("B")
            if isinstance(a, int) and isinstance(b, int):
                answer = a * b
                return JsonResponse({'answer': answer})
            else:
                return JsonResponse({'error': 'Numbers only!'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        response = HttpResponseNotAllowed(permitted_methods=["GET", "POST"])

    return response


def divide(request):
    if request.method == 'GET':
        my_dict = {
            "A": int(5),
            "B": int(5),
        }
        response = JsonResponse(my_dict)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = data.get("A")
            b = data.get("B")
            if isinstance(a, int) and isinstance(b, int):
                answer = a / b
                return JsonResponse({'answer': answer})
            else:
                return JsonResponse({'error': 'Numbers only!'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        response = HttpResponseNotAllowed(permitted_methods=["GET", "POST"])

    return response


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])
