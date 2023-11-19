from django.http import Http404
from django.shortcuts import render
from .models import Event


# Return all avents
def list(request):
    return render(request, 'events/event_list.html', {'events' : Event.objects.all()})

# Return one event by private key pk
def detail(request, private_key):
    try:
        event = Event.objects.get(pk=private_key)
    except Event.DoesNotExist():
        raise Http404('Event ID : ' + private_key + 'does not exist. Please check.')
    return render(request, 'events/event_list.html', {'event' : Event.objects.get(pk=private_key)})
