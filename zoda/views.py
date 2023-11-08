from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tender


# def index(request):
#     tenders = Tender.objects.all()
    
#     context = {'tender': tenders, 't': 'Заголовок', }
#     return render(request, 'zoda/index.html', context)
def first_page(request):
    # slider_list = CMSSlider.objects.all()
    # pc_1 = PriceCard.objects.get(pk=1)
    # pc_2 = PriceCard.objects.get(pk=2)
    # pc_3 = PriceCard.objects.get(pk=3)
    tenders = Tender.objects.all()
    # form = OrderForm()
    dict_obj = {
                # 'slider_list': slider_list,
                # 'pc_1': pc_1,
                # 'pc_2': pc_2,
                # 'pc_3': pc_3,
                'tenders': tenders,
                # 'form': form
                }
    return render(request, 'zoda/index.html', dict_obj)

