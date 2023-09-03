from django.contrib import admin
from .models import *

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_id','is_active','begeni_sayisi')

class LiveVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_id')

class KullaniciBegeniAdmin(admin.ModelAdmin):
    list_display = ('kullanici', 'ders')
    list_filter = ('kullanici', 'ders')
    search_fields = ('kullanici__username', 'ders__title')

admin.site.register(KullaniciBegeni, KullaniciBegeniAdmin)
admin.site.register(Dersler, LessonAdmin)
admin.site.register(CanliDersler, LiveVideoAdmin)
