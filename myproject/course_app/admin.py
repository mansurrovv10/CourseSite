from django.contrib import admin
from .models import (
    UserProfile, Category, SubCategory, Course, Lesson,
    Assignment, Exam, Question, Option, Certificate, Review
)
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin



class SubCategoryInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [SubCategoryInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',)}




@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',)}



class OptionInline(admin.TabularInline,TranslationInlineModelAdmin):
    model = Option
    extra = 1


@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    inlines = [OptionInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',)}



class QuestionInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Question
    extra = 1
    show_change_link = True


@admin.register(Exam)
class ExamAdmin(TranslationAdmin):
    inlines = [QuestionInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',)}


@admin.register(Lesson)
class LessonAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',)}

@admin.register(Assignment)
class AssignmentAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',)}



admin.site.register(UserProfile)
admin.site.register(Certificate)
admin.site.register(Review)
