#!/usr/bin/env python

from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from functools import wraps

def allowed_method(*permitted_methods):
    def decorator(view):
        @wraps(view)
        def caller(request, *args, **kwargs):
            if request.method in permitted_methods:
                return view(request, *args, **kwargs)
            return HttpResponseNotAllowed(permitted_methods)
        return caller
    return decorator

def ajax_call_only():
    def decorator(view):
        @wraps(view)
        def caller(request, *args, **kwargs):
            if request.is_ajax():
                return view(request, *args, **kwargs)
            return HttpResponseForbidden("Ajax call only.")
        return caller
    return decorator