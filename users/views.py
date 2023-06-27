from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

#NEED better authentication, password hashing etc

#User registration
@csrf_exempt
@require_POST
def register_user (request):
    name = request.POST.get("name")
    #client should create hash of password before sending
    password = request.POST.get("password") 
    email = request.POST.get("email")
    phonenumber = request.POST.get("phonenumber")

    user = User(name=name, password=password, email=email, phonenumber=phonenumber)
    user.save()
    return JsonResponse({"message": "Registration completed"})

@csrf_exempt
@require_POST
def login_user (request):
    #email will work as username
    #later phonenumber could be added to work as username
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = User.objects.get(email=email, password=password)
    return JsonResponse({"name": user.name}) #need to add id? should it be in User class

