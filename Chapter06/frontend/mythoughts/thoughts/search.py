import requests
import math
from django.conf import settings
from django.shortcuts import render, redirect

from .thoughts import get_username_from_session


def load(request):
    # Create a slow call
    math.factorial(50000)
    return redirect('index')


# request by the customer gets transformed into API endpoints
# the result is decoded in JSON and rendered in the template 
def search(request):
    username = get_username_from_session(request)
    search_param = request.GET.get('search')

    url = settings.THOUGHTS_BACKEND + '/api/thoughts/'
    params = {
        'search': search_param,
    }
    result = requests.get(url, params=params)
    results = result.json()

    context = {
        'thoughts': results,
        'username': username,
    }
    return render(request, 'search.html', context)
