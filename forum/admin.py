from django.contrib import admin
from forum.models import Theme, Comment
# Register your models here.

class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'count_answer', 'time_of_create']


admin.site.register(Theme ,ThemeAdmin)
admin.site.register(Comment)