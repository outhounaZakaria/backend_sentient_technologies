from telnetlib import STATUS
from semestre.models import Niveau
from django.http import JsonResponse 
from semestre.rest.serialilzers.niveau_seriallizer import NiveauSerializer 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login")
def niveau_list(request):
    niveaux = Niveau.objects.all()
    serializer = NiveauSerializer(niveaux , many=True)
    return JsonResponse({'niveaux':serializer.data} , safe=False)

   
@login_required(login_url="/login")
def niveau_by_id(request , id):
    try:
        niveau  = Niveau.objects.get(pk=id)
    except Niveau.DoesNotExist :
        return JsonResponse({} , safe=False)

    serializer = NiveauSerializer(niveau , many=False)
    return JsonResponse(serializer.data , safe= False )


@login_required(login_url="/login")
def niveau_by_name(request , nom):
    try:
         niveau  = Niveau.objects.get(nom_niveau=nom)
    except Niveau.DoesNotExist :
        return JsonResponse({} , safe=False)
    
    serializer = NiveauSerializer(niveau , many=False)
    return JsonResponse(serializer.data , safe= False )


@login_required(login_url="/login")
def niveau_by_id_filliere(request , filliere):
    try:
         niveaux  = Niveau.objects.filter(filiere=filliere)
    except Niveau.DoesNotExist :
        return JsonResponse({} , safe=False)
    serializer = NiveauSerializer( niveaux ,many=True)
    return JsonResponse({'niveaux':serializer.data} , safe= False )

