from django.urls import path
from .consumers import DashboardConsumer

websocket_url = [
    path('ws/<str:dashboard_slug>', DashboardConsumer.as_asgi()),
]