from django.urls import path,include
from semestre.rest import niveau 

urlpatterns = [
    path('list/',niveau.niveau_list,name='niveau_list_api') ,
    path('id/<int:id>/', niveau.niveau_by_id,name='niveau_by_id'), 
    path('nom/<str:nom>/', niveau.niveau_by_name,name='niveau_by_name'), 
    path('filliere/<str:filliere>/', niveau.niveau_by_id_filliere,name='niveau_by_id_filliere'), 
]