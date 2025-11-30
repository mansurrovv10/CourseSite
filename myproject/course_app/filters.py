from .models import Course
from django_filters import FilterSet


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'sub_category':['exact'],
            'price':['gt','lt'],
            'level':['exact'],
        }