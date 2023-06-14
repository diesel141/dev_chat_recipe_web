from django.urls import path

from . import views

urlpatterns = [path("test", views.RequestChatGPTView.as_view())]
