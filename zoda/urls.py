from django.urls import path

from . import views
from .views import get_agencies

#from .views import TenderListView

urlpatterns = [
    path('', views.first_page, name='home'),
    path('get_agencies/<int:region_id>/', get_agencies, name='get_agencies'),

 #   path('tenders/', TenderListView.as_view(), name='tender_list_view'),

]