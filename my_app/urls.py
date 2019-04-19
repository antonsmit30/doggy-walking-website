from django.urls import path
from my_app import views
from django.conf.urls.static import static, settings

app_name = "my_app"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('shelters/', views.ShelterListView.as_view(), name='shelters'),
    path('dogs/', views.DogListView.as_view(), name='dogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

