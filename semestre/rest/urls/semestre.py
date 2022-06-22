from django.urls import path,include
from semestre.rest import semestre 

urlpatterns = [
    path('list/',semestre.semestre_list,name='semestre_list_api') ,
    path('id/<int:id>/', semestre.semestre_by_id,name='semestre_by_id'), 
    path('libelle/<str:libelle>/', semestre.semestre_by_libelle,name='semestre_by_libelle'), 
    path('niveau/<int:niveau>/', semestre.semestre_by_id_niveau,name='semestre_by_id_niveau'), 
]