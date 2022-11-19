from django.urls import path
from hello_app.views import HelloWorldView, HelloView

urlpatterns = [

    path('', view = HelloWorldView.as_view()),
    path('<str:name>', view = HelloView.as_view())
    
]