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
        answer = json.loads(request.body).get("A") + json.loads(request.body).get("B")
        response = JsonResponse({'answer': answer})
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
        answer = json.loads(request.body).get("A") - json.loads(request.body).get("B")
        response = JsonResponse({'answer': answer})
    else:
        response = HttpResponseNotAllowed(permitted_methods=["GET", "POST"])

    return response


def multiply(request):
    return HttpResponse("Hello hi ")


def divide(request):
    return HttpResponse("Hello hi ")


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])
