from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from users.models import User
from .models import Order

@csrf_exempt
@require_POST
def add_order(request):
    email = request.POST.get("email")
    items = request.POST.get("items")

    user = User.objects.get(email=email)
    order = Order(user=user, items=items, status="Added")
    order.save()

    return JsonResponse({"Message": "Order added!", "Order id": order.pk,})

@require_GET
def get_order(request, order_id):
    order = Order.objects.get(id=order_id)
    return JsonResponse({"order_id": order_id, "status": order.status, "items": order.items})

