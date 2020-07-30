from django.contrib import admin
from .models import questions,choice

class ChoiceInline(admin.TabularInline):
    model=choice
    extra=3

# Register your models here.
class questionAdmin(admin.ModelAdmin):
    fieldsets =[
        (None,{'fields':['question_text']}),
        ("Date Information", {'fields': ['pub_date']}),
    ]
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date','was_published_recently')
    list_filter=["pub_date"]
    search_fields=['question_text']
admin.site.register(questions,questionAdmin)
admin.site.register(choice)
