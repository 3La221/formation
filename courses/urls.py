from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    #authentication
    path('auth/<str:id>' , views.auth_view , name="login-etudiant"),
	path('auth/' , views.auth_view , name="login-etudiant"),
    path('logout/' , views.logout_view , name="logout-etudiant"),
    
    
    #admin
    path('add_formation/', views.create_formation , name="ajouter-formation") ,
    
    
    #formations
    path("formation/<str:id>/" ,views.formation_details , name="formation-detail"),
    
    
    path("",views.landing_page,name="landing-page"),
    path("submit/<str:id>",views.inscrire,name="inscription"),
    path("mes_formation/<int:id>",views.mes_formations, name="mes-formations")
    
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
