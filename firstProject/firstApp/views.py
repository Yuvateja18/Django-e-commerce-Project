from django.shortcuts import render,redirect
from .models import Products,Category,Customer
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
def basic_view(request):

    products=Products.objects.all()
    categories=Category.objects.all()
    data={
        "Products":products,
        "Categories":categories
    }
    return render(request,"basic.html",data)
    

def basic_store(request):
    # products=Products.objects.all()
    categories=Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = Products.get_categoryid(category_id)
    else:
        products = Products.objects.all()
    data={
        "Products":products,
        "Categories":categories,
    }
    return render(request,"store.html",data)
    


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_no = request.POST["phone_no"]
        password = request.POST["password"]

        # Check if user already exists
        if Customer.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error": "Email already registered"})

        # Save new user
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_no=phone_no,
            password=make_password(password)
        )
        customer.save()
        return redirect("login")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            customer = Customer.objects.get(email=email)
            if check_password(password, customer.password):
                request.session["customer_id"] = customer.id
                request.session["customer_name"] = customer.first_name
                return render(request, "welcome.html", {"name": customer.first_name})
            else:
                return render(request, "login.html", {"error": "Invalid password"})
        except Customer.DoesNotExist:
            return render(request, "login.html", {"error": "User does not exist"})



def logout(request):
    request.session.clear()
    return redirect('login')


