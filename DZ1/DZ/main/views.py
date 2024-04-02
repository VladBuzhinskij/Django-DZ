from django.shortcuts import render
from django.http import HttpResponse
import logging

logger=logging.getLogger(__name__)
# Create your views here.
def index (request):
    logger.info('index page accessed')
    return render(request,'main/index.html')
def about (request):
    logger.info('about page accessed')
    return render(request,'main/about.html')