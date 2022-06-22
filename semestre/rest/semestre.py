from telnetlib import STATUS
from semestre.models import Semestre
from django.http import JsonResponse 
from semestre.rest.serialilzers.semestre_serializer import SemestreSerializer 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login")
def semestre_list(request):
    semestres = Semestre.objects.all()
    serializer = SemestreSerializer(semestres , many=True)
    return JsonResponse({'semestres':serializer.data} , safe=False)


@login_required(login_url="/login")
def semestre_by_id(request , id):
    try:
        semestre  = Semestre.objects.get(pk=id)
    except Semestre.DoesNotExist :
        return JsonResponse({} , safe=False)

    serializer = SemestreSerializer(semestre , many=False)
    return JsonResponse(serializer.data , safe= False )


@login_required(login_url="/login")
def semestre_by_libelle(request , libelle):
    try:
         semestre  = Semestre.objects.get(libelle_semestre=libelle)
    except Semestre.DoesNotExist :
        return JsonResponse({} , safe=False)
    
    serializer = SemestreSerializer(semestre , many=False)
    return JsonResponse(serializer.data , safe= False )


@login_required(login_url="/login")
def semestre_by_id_niveau(request , niveau):
    try:
         semestres  = Semestre.objects.filter(niveau=niveau)
    except Semestre.DoesNotExist :
        return JsonResponse({} , safe=False)
    serializer = SemestreSerializer( semestres ,many=True)
    return JsonResponse({'semestres':serializer.data} , safe= False )

