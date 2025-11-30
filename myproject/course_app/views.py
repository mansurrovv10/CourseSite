from .models import (UserProfile,Category,SubCategory,Course,Lesson,
                     Assignment,Exam,Review)
from .serializers import (CategoryListSerializer, CategoryDetailSerializer,
                          SubCategoryListSerializer, SubCategoryDetailSerializer, LessonSerializer,
                          CourseListSerializer, CourseDetailSerializer, AssignmentListSerializer,
                          AssignmentDetailSerializer, ExamListSerializer, ExamDetailSerializer,
                          ExamCreateSerializer,UserProfileRegisterSerializer,UserProfileLoginSerializer,
                          CourseCreateSerializer,ReviewCreateSerializer,UserProfileListSerializer,
                          UserProfileDetailSerializer)
from rest_framework import viewsets,generics,status,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import CoursePagination
from .permissions import CreateCoursePermission,CreateExamPermission,CheckPermission



class RegisterCreateView(generics.CreateAPIView):
    serializer_class = UserProfileRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = UserProfileLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer
    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)



class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer
    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)




class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer



class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer



class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryDetailSerializer



class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer




class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['title']
    ordering_fields = ['price']
    pagination_class = CoursePagination


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class CourseCreateViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [CreateCoursePermission]

    def get_queryset(self):
        return Course.objects.filter(teacher=self.request.user)


class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer



class AssignmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer




class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer


class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer


class ExamCreateViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamCreateSerializer
    permission_classes = [CreateExamPermission]

    def get_queryset(self):
        return Course.objects.filter(teacher=self.request.user)



class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [CheckPermission]

    def get_queryset(self):
        return Course.objects.filter(student=self.request.user)


class ReviewEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [CheckPermission]


    def get_queryset(self):
        return Review.objects.filter(student=self.request.user.role)
