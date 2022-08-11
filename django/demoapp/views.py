import re
from urllib import response
from django.shortcuts import render
"""
cache for Vary header
from django.views.decorators.vary import vary_on_headers
from django.utils.cache import patch_vary_headers

@vary_on_headers('Accept_Language')
def homepage(request):
    response = render(request, "page1.html", context)
    patch_vary_headers(response, ['User-Agent'])
    return response
"""


from django.views.decorators.cache import cache_control

#another one example for cache control
@cache_control(private=True)
def homepage(request):
    return render(request, "page1.html")