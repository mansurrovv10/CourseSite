from django.urls import path,include
from .views import ( LessonViewSet, AssignmentListAPIView,AssignmentDetailAPIView,ExamListAPIView,
                    ExamDetailAPIView, CategoryListAPIView,CategoryDetailAPIView,SubCategoryListAPIView,
                    SubCategoryDetailAPIView,CourseListAPIView,CourseDetailAPIView,ExamCreateViewSet,RegisterCreateView,
                    LoginView,LogoutView,CourseCreateViewSet,UserProfileListAPIView,UserProfileDetailAPIView,
                    ReviewEditAPIView,ReviewCreateAPIView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register(r'lesson',LessonViewSet)
router.register(r'course_create',CourseCreateViewSet)
router.register(r'exam_create',ExamCreateViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('userprofile/',UserProfileListAPIView.as_view(),name='userprofile-list'),
    path('userprofile/<int:pk>/',UserProfileDetailAPIView.as_view(),name='userprofile-detail'),
    path('category/',CategoryListAPIView.as_view(),name='category-list'),
    path('category/<int:pk>/',CategoryDetailAPIView.as_view(),name='category-detail'),
    path('subcategory/',SubCategoryListAPIView.as_view(),name='subcategory-list'),
    path('subcategory/<int:pk>/',SubCategoryDetailAPIView.as_view(),name='subcategory-detail'),
    path('course/',CourseListAPIView.as_view(),name='course-list'),
    path('course/<int:pk>/',CourseDetailAPIView.as_view(),name='course-detail'),
    path('assignment/',AssignmentListAPIView.as_view(),name='assignment-list'),
    path('assignment/<int:pk>/',AssignmentDetailAPIView.as_view(),name='assignment-detail'),
    path('exam/',ExamListAPIView.as_view(),name='exam-list'),
    path('exam/<int:pk>/',ExamDetailAPIView.as_view(),name='exam-detail'),
    path('review/',ReviewCreateAPIView.as_view(),name='review-create'),
    path('review/<int:pk>/',ReviewEditAPIView.as_view(),name='review-edit'),



    path('register/', RegisterCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
