from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index(request):
    return HttpResponse('Scraper')