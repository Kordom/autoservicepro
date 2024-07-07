from django.contrib import admin
from .models import *


# username:admin password:admin123456789

class UzsakymasEilutesInline(admin.TabularInline):
    model = UzsakymoEilutes
    extra = 2


@admin.register(AutomobilioModelis)
class AutomobilioModelisAdmin(admin.ModelAdmin):
    list_display = ('marke', 'modelis', 'metai', 'variklis')
    list_filter = ('marke', 'metai', 'variklis')


@admin.register(Automobilis)
class AutomobilisAdmin(admin.ModelAdmin):
    list_display = (
        'klientas',
        'marke',
        'modelis',
        'valstybinis_nr',
        'vin',
        'aprasymas')

    list_filter = ('klientas', 'automobilio_modelis__marke')
    search_fields = ('vin', 'valstybinis_nr')


@admin.register(Uzsakymas)
class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('data',
                    'marke',
                    'modelis',
                    'klientas',
                    'status',
                    'uzsakovas',
                    'grazinimo_terminas',
                    'suma')
    inlines = (UzsakymasEilutesInline,)
    list_filter = ('data', 'status')
    list_editable = ('status', 'uzsakovas',
                     'grazinimo_terminas')


@admin.register(UzsakymoEilutes)
class UzsakymoEilutesAdmin(admin.ModelAdmin):
    list_display = ('kiekis', 'kaina')
    list_filter = ('kiekis', )


@admin.register(Paslauga)
class PaslaugosAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')

# admin.site.register(AutomobilioModelis, AutomobilioModelisAdmin)
# admin.site.register(Automobilis, AutomobilisAdmin)
# admin.site.register(Uzsakymas, UzsakymasAdmin)
# admin.site.register(UzsakymoEilutes, UzsakymoEilutesAdmin)
# admin.site.register(Paslauga, PaslaugosAdmin)
admin.site.register(UzsakymasReview)
admin.site.register(Profile)