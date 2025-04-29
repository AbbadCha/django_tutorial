from django.shortcuts import render

def home(request):
    context = {'page': 'home'}
    return render(request, 'base/home.html', context)

def room(request, pk):
    context = {'page': 'room', 'room_id': pk}
    return render(request, 'base/room.html', context)
