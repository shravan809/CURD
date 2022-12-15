from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact',views.student),
    path('details/',views.details,name='add'),
    path('about',views.aboutus),
    path('delete/<int:id>/',views.delete_data, name="deletedata"),
    path('<int:id>/',views.update_data, name="updatedata")
]