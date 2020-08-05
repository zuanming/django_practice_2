from django.test import TestCase

# Create your tests here.
def index(request):
    return HttpResponse("Books app")