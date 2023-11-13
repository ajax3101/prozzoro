from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Tender, Region, Agency
from .forms import TenderFilterForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .serializers import AgencySerializer

@require_GET
def get_agencies(request, region_id):
    agencies = Agency.objects.filter(region_id=region_id)
    serializer = AgencySerializer(agencies, many=True)
    return JsonResponse(serializer.data, safe=False)

def first_page(request):
    # Получаем все записи из модели Tender
    all_tenders = Tender.objects.all()
    
    # Фильтрация по региону и установе
    filter_form = TenderFilterForm(request.GET)
    if filter_form.is_valid():
        region = filter_form.cleaned_data.get('region')
        agency = filter_form.cleaned_data.get('agency')

        if region:
            all_tenders = all_tenders.filter(edr__region=region)

        if agency:
            all_tenders = all_tenders.filter(edr=agency)

    # # Добавляем возможность сортировки по полю 't' (заголовок тендера)
    # sort_by = request.GET.get('sort_by', '-t')
    # all_tenders = all_tenders.order_by(sort_by)

    # Используем Paginator для разбиения записей на страницы (по 10 записей на страницу)
    paginator = Paginator(all_tenders, 10)

    # Получаем номер текущей страницы из GET-параметра "page"
    page = request.GET.get('page')

    # Получаем записи для текущей страницы
    tenders = paginator.get_page(page)

    dict_obj = {
        'tenders': tenders,
        'filter_form': filter_form,
        #'sort_by': sort_by,
    }

    return render(request, 'zoda/index.html', dict_obj)


# class TenderListView(View):
#     template_name = 'zoda/tender_list_view.html'

#     def get(self, request, *args, **kwargs):
#         region_id = request.GET.get('region')
#         tenders = Tender.objects.all()

#         if region_id:
#             tenders = tenders.filter(edrpou_id__region_id=region_id)

#         regions = Region.objects.all()

#         return render(request, self.template_name, {'tenders': tenders, 'regions': regions})