from django.urls import path

from . import views
from .views import TenderListView

urlpatterns = [
    path('', views.first_page, name='home'),
    path('tenders/', TenderListView.as_view(), name='tender_list_view'),

]