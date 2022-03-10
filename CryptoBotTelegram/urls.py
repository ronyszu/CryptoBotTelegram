from django.urls import path
from CryptoBotTelegram import views

urlpatterns = [
    path("", views.home, name="home"),
    path("CryptoBotTelegram/<name>", views.newsBot, name="news_bot"),
]