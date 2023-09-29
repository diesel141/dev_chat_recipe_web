from django.urls import path

from . import views

urlpatterns = [path("chatgpt/prompt", views.RequestChatGPTView.as_view())]
