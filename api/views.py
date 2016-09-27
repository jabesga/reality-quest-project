from django.shortcuts import render, HttpResponse
from .models import NPC, Quote, Mission
from .forms import NPCForm, MissionForm
import json


def index(request):
    return render(request, 'api/index.html')


def npc(request):
    if request.method == 'POST':
        npc_form = NPCForm(data=request.POST)
        if npc_form.is_valid():
            name = request.POST['name']
            portrait = request.POST['portrait_style']
            lat = request.POST['lat']
            lng = request.POST['lng']
            quote_1 = request.POST['quote_1']
            quote_2 = request.POST['quote_2']
            quote_3 = request.POST['quote_3']
            quote_4 = request.POST['quote_4']
            _npc = NPC(name=name, portrait_style=portrait, lat=lat, lng=lng)
            _npc.save()

            Quote(npc=_npc, quote=quote_1).save()
            Quote(npc=_npc, quote=quote_2).save()
            Quote(npc=_npc, quote=quote_3).save()
            Quote(npc=_npc, quote=quote_4).save()

            return HttpResponse('NPC created succesfully (id: ' + str(_npc.id) + ')')
        else:
            return render(request, 'api/create-npc-with-form.html', {'form': npc_form})
    else:
        list_all_npc = NPC.objects.all()
        response_data = {'npc': []}

        for _npc in list_all_npc:
            quote_dict = {}
            i = 0
            list_all_npc_quote = _npc.quote_set.all()
            for _quote in list_all_npc_quote:
                i += 1
                quote_dict[i] = _quote.quote

            response_data['npc'].append({
                'id': _npc.id,
                'name': _npc.name,
                'portrait_style': _npc.portrait_style,
                'lat': _npc.lat,
                'lng': _npc.lng,
                'quotes': quote_dict
                })

        return HttpResponse(json.dumps(response_data), content_type='application/json')


def create_npc_with_form(request):
    form = NPCForm()
    return render(request, 'api/create-npc-with-form.html', {'form': form})


def find_npc_by_id(request, _id):
    try:
        _npc = NPC.objects.all().get(id=_id)
        response_data = {'name': _npc.name}
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    except NPC.DoesNotExist:
        return HttpResponse("No exist")


def find_missions_of_npc(request, _id):
    if request.method == 'GET':
        try:
            _npc = NPC.objects.all().get(id=_id)
            list_all_missions_of_npc = Mission.objects.all().filter(start_with=_npc)
            response_data = {'mission': []}
            for _mission in list_all_missions_of_npc:
                response_data['mission'].append({
                    'id': _mission.id,
                    'name': _mission.name,
                    'mission_briefing': _mission.mission_briefing,
                    'start_quote': _mission.start_quote,
                    'end_with': str(_mission.end_with),
                    'end_quote': _mission.end_quote,
                    })
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        except NPC.DoesNotExist:
            return HttpResponse("The NPC doesn't exist")


def create_mission_with_form(request):
    form = MissionForm()
    return render(request, 'api/create-mission-with-form.html', {'form': form})


def mission(request):
    mission_form = MissionForm()
    if request.method == 'POST':
        mission_form = MissionForm(data=request.POST)
        if mission_form.is_valid():
            _mission = mission_form.save()
            return HttpResponse('Mission created succesfully (id: ' + str(_mission.id) + ')')

    return render(request, 'api/create-mission-with-form.html', {'form': mission_form})
