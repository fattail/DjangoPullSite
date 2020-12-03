from django.contrib import admin

from .models import Question,Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('问题正文内容',{'fields':['question_text']}),
        ('发布日期信息',{'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
