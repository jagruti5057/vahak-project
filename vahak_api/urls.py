from django.urls import path
from vahak_api import views

urlpatterns = [
        path('',views.index,name='index'),
        # path('Businesscard/', views.Businesscard.as_view()),
        path('businesscard/', views.BusinesscardAPI.as_view()),
        path('businesscard/<int:id>/', views.BusinessCardUpdateAPI.as_view()),
        path('Vehicalmodel/', views.VehicalmodelAPI.as_view()),
        path('vehicalmodel/<int:id>/', views.VehicalmodelUpdateAPI.as_view()),
        path('Attachnewlorry/', views.AttachnewlorryAPI.as_view()),
        path('Attachnewlorry/<int:id>/', views.AttachlorryUpdateAPI.as_view())
               
]
