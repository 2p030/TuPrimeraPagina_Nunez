from django.urls import path
from .views import inbox, sent_messages, message_detail, send_message

urlpatterns = [
    path('', inbox, name='inbox'),
    path('sent/', sent_messages, name='sent_messages'),
    path('send/', send_message, name='send_message'),
    path('<int:pk>/', message_detail, name='message_detail'),
]