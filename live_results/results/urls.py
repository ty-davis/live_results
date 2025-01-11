from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('meets/<str:slug>/', views.meet_view),
    path('meets/', views.meet_view),
    path('meets/<str:meet_slug>/<str:event_slug>', views.event_view),
]
