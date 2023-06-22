from django.contrib import admin

# Register your models here.

from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date","question_text"]
    #exclude = []
    readonly_fields = ["pub_date"]
    list_display = ["question_text","pub_date","was_published_recently"]
    #list_editable = ["pub_date"]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
