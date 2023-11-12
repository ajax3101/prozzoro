from django.contrib import admin
from zoda.models import Tender, Region, Agency


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    model = Tender

    list_display = (
        "t",
        "tl",
        "cpv",
        "v"	,
        "a"	,
        "s"	,
        "t_id",
        "cdb",
        "t_method",
    )
    list_per_page = 10
    list_max_show_all = 100
    
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'edrpou', 'region')
    list_filter = ('region',)

# @admin.register(Tender)
# class TenderAdmin(admin.ModelAdmin):
#     list_display = ('t', 'tl', 'cpv', 'edrpou_id')
#     list_filter = ('edrpou_id__region',)  # Фильтр по региону агентства