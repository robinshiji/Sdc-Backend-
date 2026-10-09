from rest_framework import serializers
from .models import ContactInquiry, CourseEnquiry, BrochureRequest, PlacedStudent, Trainer, Course, Career, JobApplication

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
    instructors = TrainerSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'slug', 'title', 'description', 'duration', 'level',
            'rating', 'image', 'highlights', 'category', 'overview',
            'outcomes', 'syllabus', 'brochure', 'instructors',
            'order', 'created_at'
        ]
        read_only_fields = ['created_at']


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        read_only_fields = ['created_at']


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['created_at']
