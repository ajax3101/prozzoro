from django.contrib import admin
from zoda.models import Tender


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
    