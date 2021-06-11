from django.urls import path
from . import views
from django.urls import reverse 

urlpatterns =[
    # path("january",views.january),
    # path("february",views.february),
    path("",views.index,name='index'), # challenges -  it is like the home page
    path("<int:month>",views.monthly_challenge_by_number),      
    path("<str:month>",views.monthly_challenge,name='month-challenge'),
]