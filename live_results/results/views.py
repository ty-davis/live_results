from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from .models import Meet, EventResult

# Create your views here.
def index_view(request):
    meets = Meet.objects.all()
    small_context = {
        "title": "Weber State Live Results",
        "meets": meets,
    }

    small_html = render_to_string('results/index.html', context=small_context, request=request)


    if request.headers.get('HX-Request'):
        return HttpResponse(small_html)
    else:
        context = {
            "main_content": small_html,
            "title": "Weber State Live Results",
        }
        return render(request, 'results/base-results.html', context=context)

def meet_view(request, slug=None):
    try:
        meet = Meet.objects.get(slug=slug)
        events = EventResult.objects.filter(meet_id=meet.id)
    except Meet.DoesNotExist:
        meet = None
        events = None

    meets = Meet.objects.all()
    small_context = {
        "title": "Weber State Live Results",
        "meet": meet,
        "events": events,
        "meets": meets,
    }

    small_html = render_to_string('results/meet.html', context=small_context, request=request)

    if request.headers.get('HX-Request'):
        return HttpResponse(small_html)
    else:
        context = {
            "main_content": small_html,
            "title": "Weber State Live Results",
        }
        return render(request, 'results/base-results.html', context=context)



def event_view(request, meet_slug, event_slug):
    event = None
    try:
        meet = Meet.objects.get(slug=meet_slug)
        try:
            events = EventResult.objects.filter(meet_id=meet.id)
        except:
            events = None
            event = None
        try:
            event = [event for event in events if event.slug == event_slug][0]
        except:
            event = None
    except Meet.DoesNotExist:
        meet = None
        event = None
        events = None

    small_context = {
        "meet": meet,
        "meet_slug": meet_slug,
        "event_slug": event_slug,
        "event": event,
        "events": events,
    }
    small_html = render_to_string('results/event.html', context=small_context, request=request)

    if request.headers.get('HX-Request'):
        return HttpResponse(small_html)
    else:
        context = {
            "main_content": small_html,
            "title": "Weber State Live Results",
        }
        return render(request, 'results/base-results.html', context=context)
