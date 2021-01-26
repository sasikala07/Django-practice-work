from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

data = {
    "products": [
        {"pid": 111, "name": "micromax", "price": 30000,
         "features": ["5 MP Front Cam", "6 Inch display", "6 gb ram", "20 MP Cam"]},
        {"pid": 222, "name": "oppo", "price": 24000},
        {"pid": 333, "name": "vivo", "price": 34000},
        {"pid": 444, "name": "samsung", "price": 20000},
    ]
}



def display(request, pid):
    global pdata
    template = loader.get_template("productpage.html")
    for x in data['products']:
        if x['pid'] == pid:
            pdata = x
            # print(x)
    res = template.render(pdata, request)
    return HttpResponse(res)


def dispalyprodlist(req):
    template = loader.get_template("productlistpage.html")
    return HttpResponse(template.render(data, req))



def addtocart(req):

    # print(req.GET) ##it get as dictionary
    # print(req.GET['id'])
    # print(req.GET['qty'])

    # pid=req.GET['id']  ###by default is get
    # qtys=req.GET['qty']

    pid = req.POST['id']  ###change into post to secure
    qtys=req.POST['qty']

    cartitems={}
    if req.session.__contains__("cart"):
        cartitems=req.session['cart']
    cartitems[pid]=qtys
    req.session['cart']=cartitems
    print(req.session['cart'])

    return HttpResponse(' Item added to cart')
