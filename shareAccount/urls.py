from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='shareAccounts'),
    path('add-shareAccount/',views.add_accounShare,name='add-shareAccount')
]
