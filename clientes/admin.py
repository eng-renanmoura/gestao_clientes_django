from django.contrib import admin
from .models import Person, Documento

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'photo')
        })
    )
    #fields = (('doc', 'first_name'), 'last_name', 'age', 'salary', 'bio', 'photo')
    #exclude = ('bio',)
    list_filter = ('age', 'salary')
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto', 'doc')
    search_fields = ('id', 'first_name')

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'
    tem_foto.short_description = 'Possui foto'




admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)

