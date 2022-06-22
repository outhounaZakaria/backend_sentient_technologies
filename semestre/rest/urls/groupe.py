from django.urls import path,include
from semestre.rest import groupe 

urlpatterns = [
    path('list/',groupe.groupe_list,name='groupe_list_api') ,
    path('id/<int:id>/', groupe.groupe_by_id,name='groupe_by_id'), 
    path('nom/<str:nom>/', groupe.groupe_by_name,name='groupe_by_name'), 
    path('niveau/<int:niveau>/', groupe.groupe_by_id_niveau,name='groupe_by_id_niveau'), 
]