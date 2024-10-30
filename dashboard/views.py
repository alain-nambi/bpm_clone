from django.shortcuts import render

# Create your views here.
def index_view(request):
    """BPM global dashboard view"""
    context = {}

    return render(request, "index.html", context=context)