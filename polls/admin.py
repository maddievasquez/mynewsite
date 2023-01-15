# We can find all models that handle the superuser settings.
# In order to make the admin modifiable we need to we need to tell the admin
# that Question objects have an admin interface. This will allow us to change/add new
# questions through the admin interface
# from django.contrib import admin
# from .models import Choice, Question
#
#
# # from .models import Question
#
#
# # This makes the question come first than the publication date
#
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3
#
#
# admin.site.register(Choice)
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
#
# admin.site.register(Question, QuestionAdmin)

from django.contrib import admin

from .models import Choice, Question


# The choices are displayed in a more compact way
class ChoiceInline(admin.TabularInline):
    # Uncomment the line of code below, and comment the line above to see the changes.
    # class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


# The choices for the question can be added at the same time as the question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
