from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from student_system.api_views import StudentViewSet, CourseViewSet, EnrollmentViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

app_name = 'api'

urlpatterns = [
    path('token/', obtain_auth_token, name='api-token-auth'),
    path('', include(router.urls)),
]
