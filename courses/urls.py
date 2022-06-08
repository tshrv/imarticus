from django.urls import path
from .views import CourseDetailView

urlpatterns = [
    path('course/<int:pk>', view=CourseDetailView.as_view(), name='course-detail'),
]
