from django.shortcuts import render

# will be replaced by a Model and DB information eventually 
finches = [
    {'name': 'Sky', 'breed': 'Zebra Finch', 'description': 'cheerful singer', 'age': 1},
    {'name': 'Sunny', 'breed': 'Gouldian Finch', 'description': 'vibrant plumage', 'age': 2},
    {'name': 'Pippin', 'breed': 'Java Sparrow', 'description': 'playful and social', 'age': 1},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })