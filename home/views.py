from django.shortcuts import render


def index(request):
    """A view to return the home page"""
    return render(request, 'home/index.html')

    
def puzzle_list(request):
    """A view to return the home page"""
    return render(request, 'home/puzzle_list.html')


