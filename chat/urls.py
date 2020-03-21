from django.urls import path


from . import views

app_name = "chat"
urlpatterns = [
    path('', views.home),
    path('<slug:label>', views.chat_room),

]
