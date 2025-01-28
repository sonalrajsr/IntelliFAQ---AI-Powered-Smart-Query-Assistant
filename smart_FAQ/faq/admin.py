from django.contrib import admin
from .models import FAQ, InteractionLog

@admin.register(FAQ)
class FAQ(admin.ModelAdmin):
    list_display = ['question', 'answer']
    search_fields = ['question']


@admin.register(InteractionLog)
class InteractionLog(admin.ModelAdmin):
    list_display = ['user_query', 'response', 'timestamp']
    search_fields = ['user_query', 'timestamp']
