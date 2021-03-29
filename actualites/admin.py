from django.contrib import admin
from .models import Articles, Categories, sous_Categories, Emissions, LesEditions_Francaise, LesEditions_Kinande, LesEditions_swahili, AproposdeNous_laRadio, AproposdeNous_NousContacter, AproposdeNous_NotreEquipe, AproposdeNous_ProjetdAvenir

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'Categories')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'corps_du_texte')
    prepopulated_fields = {'slug': ('titre', ), }
    
    def apercu_contenu(self, Articles):
        text = Articles.corps_du_texte[:25]
        if len(Articles.corps_du_texte) > 25:
            return '{}...'.format(text)
        else:
                return text
    apercu_contenu.short_description = 'Aperçu du contenu'


class laRadioAdmin(admin.ModelAdmin):
    list_display = ( 'titreduMessage', )
    list_filter = ['titreduMessage']
    search_fields = ['titreduMessage']


class EmissionsAdmin(admin.ModelAdmin):
    list_display = ( 'titreEmission', )
    list_filter = ['titreEmission']
    search_fields = ['titreEmission']


class LesEditions_FrancaiseAdmin(admin.ModelAdmin):
    list_display = ('desk_francais', 'dateEditions ')
    list_filter = ('desk_francais', 'dateEditions')
    search_fields = ('desk_francais', 'dateEditions')
    date_hierarchy = 'dateEditions'
    ordering = 'dateEditions'

class LesEditions_swahiliAdmin(admin.ModelAdmin):
    list_display = ('desk_swahili', 'dateEditions ')
    list_filter = ('desk_swahili', 'dateEditions')
    search_fields = ('desk_swahili', 'dateEditions')
    date_hierarchy = 'dateEditions'
    ordering = 'dateEditions'

class LesEditions_KinandeAdmin(admin.ModelAdmin):
    list_display = ('desk_kinande', 'dateEditions ')
    list_filter = ('desk_kinande', 'dateEditions')
    search_fields = ('desk_kinande', 'dateEditions')
    date_hierarchy = 'dateEditions'
    ordering = 'dateEditions'

admin.site.register(Categories )
admin.site.register(Articles, ArticlesAdmin )
admin.site.register(sous_Categories)
admin.site.register(AproposdeNous_laRadio, laRadioAdmin)
admin.site.register(AproposdeNous_NotreEquipe)
admin.site.register(AproposdeNous_ProjetdAvenir)
admin.site.register(Emissions, EmissionsAdmin)
admin.site.register(LesEditions_Francaise)
admin.site.register(LesEditions_swahili)
admin.site.register(LesEditions_Kinande)
admin.site.register(AproposdeNous_NousContacter)
