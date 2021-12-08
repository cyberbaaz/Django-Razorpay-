from django.shortcuts import render
import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZOR_PUBLIC_KEY, settings.RAZOR_PRIVATE_KEY))


# Create your views here.
def index(request):
    DATA = {
        "amount": 99900,
        "currency": "INR",
        "receipt": "receipt#1"
        }
    order=client.order.create(data=DATA)
    order_id = order['id']
    context={
        'amount':999,
        'api_key':settings.RAZOR_PUBLIC_KEY,
        'order_id':order_id
    }
    return render(request,'pay.html',context)


