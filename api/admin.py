from django.contrib import admin
from models import NPC, Quote, Mission


class QuoteInline(admin.StackedInline):
    model = Quote
    extra = 0


class OptionNPC(admin.ModelAdmin):
    list_display = ('name', 'portrait_style', 'lat', 'lng')
    inlines = [QuoteInline]


admin.site.register(NPC, OptionNPC)
admin.site.register(Quote)
admin.site.register(Mission)