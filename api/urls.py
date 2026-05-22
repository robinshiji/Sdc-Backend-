from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactInquiryCreateView,
    CourseEnquiryCreateView,
    BrochureRequestCreateView,
    PlacedStudentListView,
    TrainerListView,
    CourseViewSet
)

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactInquiryCreateView.as_view(), name='contact-inquiry'),
    path('enquiry/', CourseEnquiryCreateView.as_view(), name='course-enquiry'),
    path('brochure/', BrochureRequestCreateView.as_view(), name='brochure-request'),
    path('placements/', PlacedStudentListView.as_view(), name='placed-students-list'),
    path('trainers/', TrainerListView.as_view(), name='trainers-list'),
]

