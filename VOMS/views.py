# -*- coding:utf-8
from django.shortcuts import render


def index(request):
    return render(request, 'voms/index.html')


def dashborad(request):
    return render(request, 'voms/dashbord.html')
