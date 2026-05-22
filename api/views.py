from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import ContactInquiry, CourseEnquiry, BrochureRequest, PlacedStudent, Trainer, Course
from .serializers import (
    ContactInquirySerializer,
    CourseEnquirySerializer,
    BrochureRequestSerializer,
    PlacedStudentSerializer,
    TrainerSerializer,
    CourseSerializer
)

class ContactInquiryCreateView(CreateAPIView):
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer


class CourseEnquiryCreateView(CreateAPIView):
    queryset = CourseEnquiry.objects.all()
    serializer_class = CourseEnquirySerializer


class BrochureRequestCreateView(CreateAPIView):
    queryset = BrochureRequest.objects.all()
    serializer_class = BrochureRequestSerializer


class PlacedStudentListView(ListAPIView):
    queryset = PlacedStudent.objects.all()
    serializer_class = PlacedStudentSerializer


class TrainerListView(ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class CourseViewSet(ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'

