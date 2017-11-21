from django.http import HttpResponse,HttpResponseRedirect
from .models import MacroSensor,Plant,MicroSensor
from UserLogin.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def index(request):
    mydate = datetime.datetime.now()
    template = 'sensors/index.html'
    microsensor = MicroSensor.objects.filter(plant__user__user=request.user)
    plants = Plant.objects.filter(user__user=request.user)
    return render(request,template,{'username':request.user,'microsensor':microsensor,'plants':plants,'Currdate':mydate.strftime("%B %d, %Y")})

@login_required
def macroSensorView(request):
    macrosensors=MacroSensor.objects.all()
    template = 'sensors/macro.html'
    context={
        'macrosensors':macrosensors,
        'user':request.user,
    }
    return render(request,template,context)

@login_required
def microSensorView(request):
    mydate = datetime.datetime.now()
    plants=Plant.objects.filter(user__user=request.user)
    microsensors={}
    for plant in plants:
        plant_id = plant.plant_id
        for microObj in MicroSensor.objects.filter(plant__user__user=request.user):
            plant_test_id=microObj.plant.plant_id
            if(plant_test_id == plant_id):
                microsensors.setdefault(str(plant_id),[])
                microsensors[str(plant_id)].append(microObj)

    template = 'sensors/micro.html'
    context = {
        'plants': plants,
        'user':request.user,
        'microsensors':microsensors,
        'Currdate':mydate.strftime("%B %d, %Y")
    }
    return render(request,template,context)

@login_required
@csrf_exempt
def addPlants(request):
    template = 'sensors/addplant.html'
    if(request.method == 'POST'):
        user = UserProfile.objects.get(user = request.user)
        plant = Plant()
        plant.user = user
        plant.Latitude = float(request.POST.get('lat'))
        plant.Longitude = float(request.POST.get('long'))
        plant.name = request.POST.get('name')
        plant.save()
        microsensor = MicroSensor()
        microsensor.plant = plant
        microsensor.save()

        return HttpResponseRedirect(reverse('sensors:index'))
    else:
        return render(request,template)

@csrf_exempt
def add_reading_macro(request):
    if request.POST.get('temp') :
        new_reading = MacroSensor()
        new_reading.Temperature = request.POST.get('temp')
        new_reading.Humidity = request.POST.get('hum')
        new_reading.WaterLevel = request.POST.get('watL')
        new_reading.Rain = request.POST.get('rainG')
        new_reading.save()

        return HttpResponse(status=200)
    return  HttpResponse(status=400)


@csrf_exempt
def add_reading_micro(request,plant_id):

    if request.POST.get('soilM'):
        plant = get_object_or_404(Plant,pk=plant_id)
        new_reading= MicroSensor()
        new_reading.plant = plant
        new_reading.SoilMoisture = request.POST.get('soilM')
        new_reading.save()

        return HttpResponse(status=200)
    return  HttpResponse(status=400)

@csrf_exempt
def userprofile(request):
    template = 'sensors/userprofile.html'
    plants = Plant.objects.filter(user__user=request.user)
    context = {
        'plants': plants,
        'user': request.user,
    }
    if(request.method == 'POST'):
        name1 = request.POST.get('name')
        plants = Plant.objects.filter(user__user=request.user)
        for plant in plants:
            if(plant.name == request.POST.get('name')):
                plant.delete()
                break
            if(plant.name == request.POST.get('name1')):
                plant.Latitude = float(request.POST.get('lat1'))
                plant.Longitude = float(request.POST.get('long1'))
                plant.save()

        return HttpResponseRedirect(reverse('sensors:index'))
    else:
        return render(request, template, context)


