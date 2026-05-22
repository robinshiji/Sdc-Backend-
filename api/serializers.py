from rest_framework import serializers
from .models import ContactInquiry, CourseEnquiry, BrochureRequest, PlacedStudent, Trainer, Course

class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = '__all__'
        read_only_fields = ['created_at']


class CourseEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnquiry
        fields = '__all__'
        read_only_fields = ['created_at']


class BrochureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrochureRequest
        fields = '__all__'
        read_only_fields = ['created_at']


class PlacedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacedStudent
        fields = '__all__'
        read_only_fields = ['created_at']


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'
        read_only_fields = ['created_at']


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='slug')

    class Meta:
        model = Course
        fields = [
            'id', 'slug', 'title', 'description', 'duration', 'level',
            'rating', 'image', 'highlights', 'category', 'overview',
            'prerequisites', 'outcomes', 'syllabus', 'instructors',
            'schedule', 'order', 'created_at'
        ]
        read_only_fields = ['created_at']

