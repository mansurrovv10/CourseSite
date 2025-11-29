from .models import Category, SubCategory, Course, Assignment, Exam, Question, Option,Lesson
from modeltranslation.translator import TranslationOptions, register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('sub_category_name',)

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')



@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('question_name',)

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('option_name',)
