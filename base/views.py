from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# rooms= [
#     {'id':1, 'name':'Lets learn Physic!'},
#     {'id':2, 'name':'Lets learn Math!'},
#     {'id':3, 'name':'Lets learn English!'},
#     {'id':4, 'name':'Lets learn Python!'},
#     {'id':5, 'name':'Lets learn C++!'},
# ]

def home(request):
    rooms = Room.objects.all() #all rooms in the db
    context ={'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk) #needs to be unique or will throw errors
    #loop through the room values
    # for i in rooms:
    #     if i['id'] == int(pk):  #just to be safe pk might be string
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST' :
        form= RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'base/room_make.html', context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    # this form will be pre filled
    form = RoomForm(instance=room)

    if request.method == 'POST' :
        form= RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request,'base/room_make.html', context)