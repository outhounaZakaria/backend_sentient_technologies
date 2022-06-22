from telnetlib import STATUS
from semestre.models import Groupe
from django.http import JsonResponse 
from semestre.rest.serialilzers.groupe_serializer import GroupeSerializer 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def groupe_list(request):
    groupes = Groupe.objects.all()
    serializer = GroupeSerializer(groupes , many=True)
    return JsonResponse({'groupes':serializer.data} , safe=False)


@login_required(login_url="/login/")
def groupe_by_id(request , id):
    try:
        groupe  = Groupe.objects.get(pk=id)
    except Groupe.DoesNotExist :
        return JsonResponse({} , safe=False)

    serializer = GroupeSerializer(groupe , many=False)
    return JsonResponse(serializer.data , safe= False )


@login_required(login_url="/login/")
def groupe_by_name(request , nom):
    try:
         groupe  = Groupe.objects.get(nom_group=nom)
    except Groupe.DoesNotExist :
        return JsonResponse({} , safe=False)
    
    serializer = GroupeSerializer(groupe , many=False)
    return JsonResponse(serializer.data , safe= False )


@login_required(login_url="/login/")
def groupe_by_id_niveau(request , niveau):
    try:
         groupes  = Groupe.objects.filter(niveau=niveau)
    except Groupe.DoesNotExist :
        return JsonResponse({} , safe=False)
    serializer = GroupeSerializer( groupes ,many=True)
    return JsonResponse({'groupes':serializer.data} , safe= False )

