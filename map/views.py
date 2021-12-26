from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .forms import PointForm
from .models import Point, Category
from django.contrib.auth.decorators import login_required
from user.models import CustomUser
from django.forms.models import model_to_dict
import json
# Create your views here.
def index(request):
    return render(request,"index.html",{})

@login_required(login_url="/user/login")
def add_point(request):
    if(request.method == "POST"):
        user = CustomUser.objects.get(email = request.user)
        form = PointForm(json.loads(request.body.decode("UTF-8")))
        category = json.loads(request.body.decode("UTF-8")).get("category")
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.user = user
            instance.category = Category.objects.get(pk=category)
            instance.save()
    return redirect("/")

def get_points(request):
    points = Point.objects.all()
    return_data = []
    if points is not None:
        for point in points:
            return_data.append({"point":model_to_dict(point),"category":model_to_dict(Category.objects.get(pk=point.category.pk))})
    return JsonResponse(list(return_data),safe=False)

@login_required(login_url="/user/login")
def get_my_locations(request):
    points = Point.objects.filter(user = request.user)
    return_data = []
    for point in points:
        return_data.append(model_to_dict(point))
    return JsonResponse(return_data,safe=False)

@login_required(login_url="/user/login")
def delete_point(request,id):
    point = Point.objects.get(pk=id)
    if(point == None):
        return redirect("/")
    if(point.user.email != request.user.email):
        return redirect("/")
    point.delete()
    return redirect("/user/dashboard?dest=myLocations")