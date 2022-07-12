from django.http import HttpResponse
import redis
import json
from requests import request

rds = redis.StrictRedis(port=6379,db=0)

class Red:
    def set(cache_key,data):
        data = json.dumps(data)
        rds.set(cache_key,data)
        return True

    def get(cache_key):
        cache_data = rds.get(cache_key)

        if not cache_data:
            return None
        
        cache_data = cache_data.decode("utf-8")
        cache_data = json.loads(cache_data)

        return cache_data

# Custom Throttle settings
from rest_framework.throttling import AnonRateThrottle

class AnonMinThrottle(AnonRateThrottle):
             scope = 'anon_min'

class AnonDayThrottle(AnonRateThrottle):
             scope = 'anon_day'


# Settings for Custom Error Handling Response for Throttle

from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled
from django.shortcuts import redirect, render

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, Throttled): 
        return redirect('limit')
        

    return response