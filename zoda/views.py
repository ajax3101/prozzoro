from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Tender, Region

def first_page(request):
    # Получаем все записи из модели Tender
    all_tenders = Tender.objects.all()

    # Используем Paginator для разбиения записей на страницы (по 10 записей на страницу)
    paginator = Paginator(all_tenders, 10)

    # Получаем номер текущей страницы из GET-параметра "page"
    page = request.GET.get('page')

    # Получаем записи для текущей страницы
    tenders = paginator.get_page(page)

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