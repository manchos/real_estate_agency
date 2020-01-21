from django.contrib import admin
from django.template.defaultfilters import escape
from .models import Flat, Complaint, Owner
from django.urls import reverse
from django.utils.html import format_html_join


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'phone_pure')
    raw_id_fields = ('flats',)
    list_display = ('full_name', 'phonenumber', 'phone_pure')


admin.site.register(Owner, OwnerAdmin)


class FlatAdmin(admin.ModelAdmin):
    def owners_phonenumbers_display(self, obj):
        return format_html_join(
            ', ', "<a href={}>{}: {}</a>",
            ((reverse('admin:property_owner_change', args=(owner.id,)),
              owner.full_name, owner.phone_pure) for owner in obj.owners.all())
        )
    list_select_related = True
    owners_phonenumbers_display.short_description = "Контакты обственников"
    owners_phonenumbers_display.allow_tags = True
    search_fields = ('town', 'address')
    readonly_fields = ['created_at', 'owners_phonenumbers_display']
    list_display = ('address', 'town', 'price', 'owners_phonenumbers_display',
                    'new_building', 'construction_year',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'сomplainant')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
