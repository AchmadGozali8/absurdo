# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Posts
from django.http import JsonResponse

def get_post(request):
	p = Posts()
	p.check()
	return JsonResponse({"status":"good job"},)
# Create your views here.
