from django.contrib import admin

from content_app.models import Comment, Content, Like, Playlist

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'is_public', 'upload_date')
    list_filter = ('content_type', 'is_public', 'upload_date')
    search_fields = ('title', 'description')
    fieldsets = (
    ('Informações Básicas', {'fields': ('title', 'description')}),
    ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
  )
    
# Register your models here.
admin.site.register(Content, ContentAdmin)


admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Playlist)
