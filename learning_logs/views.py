from django.shortcuts import render


def index(request): 
    """A página inicial de leraning log"""
    return render(request, 'learning_logs/index.html')
