
from django.contrib import admin
from models import *


class DefinitionsAdmin(admin.ModelAdmin):
    """

    """

    list_display = ('name', 'definition')
    list_filter = ('domain', 'tbl_scope')
    fieldsets = (
        (None, {'fields':('name', 'definition')}),
        ('Link', {'fields': ('link',)}),
        ('TBL Scope', {'fields': ('tbl_scope',)}),
        ('Domain', {'fields': ('domain',)}),
        ('Remarks', {'fields': ('remarks',)}))

    search_fields = ('name','domain', 'tbl_scope')


class IndicatorsAdmin(admin.ModelAdmin):
    """

    """

    list_display = ('tbl_scope', 'type', 'indicator', 'tags',)
    list_filter = ('tbl_scope',)
    fieldsets = (
        (None, {'fields':('tbl_scope', 'type','indicator', 'tags')}),)

    search_fields = ('tags','indicators', 'type')


class MethodsAdmin(admin.ModelAdmin):
    """

    """

    list_display = ('name', 'problem', 'stage', )

    fieldsets = (
        (None, {'fields':('name', 'problem','tbl_scope', 'stage', 'lcp', 'activity', 'domain', 'time_scale',
                          'prerequisite', 'description', 'input', 'procedure', 'output', 'key_benefits',
                          'shortcomings', 'example', 'external_link', 'sources')}),)

    search_fields = ('name','problem', 'stage')


class ProceduresAdmin(admin.ModelAdmin):
    """

    """

    list_display = ('name',)
    fieldsets = (
        (None, {'fields':('name', 'steps',)}),)

    search_fields = ('name',)


admin.site.register(Definitions, DefinitionsAdmin)
admin.site.register(Indicators, IndicatorsAdmin)
admin.site.register(Procedures, ProceduresAdmin)
admin.site.register(Methods, MethodsAdmin)
admin.site.register(Domain)
admin.site.register(TBL_Scope)