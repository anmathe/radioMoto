from django.contrib import admin
from .models import Articles, Categories, sous_Categories

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'Categories')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'corps_du_texte')
    def apercu_contenu(self, Articles):
        text = Articles.corps_du_texte[:25]
        if len(Articles.corps_du_texte) > 25:
            return '{}...'.format(text)
        else:
                return text
    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Categories )
admin.site.register(Articles, ArticlesAdmin )
admin.site.register(sous_Categories)

