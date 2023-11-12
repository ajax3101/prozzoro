from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Tender, Region



def first_page(request):
    tenders = Tender.objects.all()
    dict_obj = {
                'tenders': tenders,
                }
    return render(request, 'zoda/index.html', dict_obj)

class TenderListView(View):
    template_name = 'zoda/tender_list_view.html'

    def get(self, request, *args, **kwargs):
        region_id = request.GET.get('region')
        tenders = Tender.objects.all()

        if region_id:
            tenders = tenders.filter(edrpou_id__region_id=region_id)

        regions = Region.objects.all()

        return render(request, self.template_name, {'tenders': tenders, 'regions': regions})