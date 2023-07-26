from django.contrib import admin
from apps.guide.models import *
# Register your models here.
admin.site.register(Guide)
admin.site.register(Travel)
admin.site.register(InvoiceType)
admin.site.register(Unit)
admin.site.register(GuideContent)
admin.site.register(GuideContentDetail)
admin.site.register(GuideContentDetailTmp)