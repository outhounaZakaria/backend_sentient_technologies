from django.urls import path,include


urlpatterns = [
    path('niveau/', include('semestre.rest.urls.niveau')),
    path('semestre/', include('semestre.rest.urls.semestre')),
    path('groupe/', include('semestre.rest.urls.groupe')),        
] 


