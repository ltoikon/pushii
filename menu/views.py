from .models import MenuItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

@csrf_exempt
@require_POST
def add_item(request):
    givenname = request.POST.get("name")
    givenprice = request.POST.get("price")
    givenavailable = request.POST.get("available")

    if givenname and givenprice:  # Add validation checks for name and price
        item = MenuItem(name=givenname, price=givenprice, available=givenavailable)
        item.save()
        return JsonResponse({"message": "Item added to the menu"})
    else:
        return JsonResponse({"message": "Invalid request: name and price are required"})



@require_GET
def get_items(request):
    #fetch all items in the menu
    items = MenuItem.objects.all()
    data = []
    for item in items:
        data.append({"name": item.name, "price": item.price, "available": item.available})
    #items = MenuItem.objects.all().values("name", "price", "available")
    return JsonResponse(data, safe=False)