from django.urls import path
from app.views import index, projects, experience, contact

urlpatterns = [
    path('', index, name='index'),
    path('projects', projects, name='projects'),
    path('experience', experience, name='experience'),
    path('contact', contact, name='contact'),
]
