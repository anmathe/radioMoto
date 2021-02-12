from django.contrib import admin
from .models import Articles, Categories, sous_Categories, Emissions, LesEditions, AproposdeNous_laRadio, AproposdeNous_NousContacter, AproposdeNous_NotreEquipe, AproposdeNous_ProjetdAvenir

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


class LesEditionsAdmin(admin.ModelAdmin):
    list_display = ('deskEditions', 'dateEditions ')
    list_filter = ('deskEditions', 'dateEditions')
    search_fields = ('deskEditions', 'dateEditions')
    date_hierarchy = 'dateEditions'
    ordering = ('dateEditions')

admin.site.register(Categories )
admin.site.register(Articles, ArticlesAdmin )
admin.site.register(sous_Categories)
admin.site.register(AproposdeNous_laRadio, laRadioAdmin)
admin.site.register(AproposdeNous_NotreEquipe)
admin.site.register(AproposdeNous_ProjetdAvenir)
admin.site.register(Emissions, EmissionsAdmin)
admin.site.register(LesEditions)
admin.site.register(AproposdeNous_NousContacter)
