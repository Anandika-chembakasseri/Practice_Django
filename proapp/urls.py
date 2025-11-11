from django.urls import path
from.import views
urlpatterns = [
    path ('',views.new),
    path ('temp',views.new1)
]
