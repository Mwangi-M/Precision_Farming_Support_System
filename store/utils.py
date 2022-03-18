import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
    # the try/except below: to handle error if a product is
    # deleted on the admin side
        try:
            cartItems += cart[i]["quantity"]

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
            # append(above) puts all items under in one page

            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems':cartItems, 'order':order, 'items':items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        # above- we are able to query child objects by setting the parent value.
        # it will get all order otems that have order as parent
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {'cartItems':cartItems, 'order':order, 'items':items}

def guestOrder(request, data):
    print('User is not logged in...')
    # print('Data:',request.body)
    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']
    cookieData = cookieCart(request)
    items = cookieData['items']
    # now, from below, we are focusing on the database side
    customer, created = Customer.objects.get_or_create(
        email=email,
        # if an anonymous user uses a specific email, the system is
        # going to look for this email, and if the email exists, the system will just
        # attach it to the customer, but they still dont have an account.. or just listed
        # as a customer
        # relevance is to see how many times a guest user has shopped with us
        # and if this user wants to create an account, their account doesn't need to be
        # reset, they can create an account, and all their previos orders can be attached
        # it helps to trace certain user behaviour
    )
    customer.name = name  # if the users wish to change their names, that's why I'm
    # creating this out of the created method
    customer.save()

    order = Order.objects.create(
        # complete is false until payment processing has actually went through
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
        # OrderItem is the model
        # on each iteration we are creating a new OrderItem

    return customer, order
