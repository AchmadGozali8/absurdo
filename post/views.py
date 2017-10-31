# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework_swagger.views import get_swagger_view
from .models import Posts
from django.http import JsonResponse

# Create your views here.
schema_view = get_swagger_view(title="First REST API")