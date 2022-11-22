from django.urls import path
from .views import Index, TableTeam, Result

urlpatterns = [
    path('', Index, name='index'),
    path('table_team', TableTeam, name='table=team'),
    path('result', Result, name='result'),

]