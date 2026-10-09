from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile, UploadedFile
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import sys
import os

def get_raw_storage():
    if getattr(settings, 'CLOUDINARY_STORAGE', None):
        from cloudinary_storage.storage import RawMediaCloudinaryStorage
        return RawMediaCloudinaryStorage()
    return FileSystemStorage(location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)

def validate_file_size(value):
    if value.size > 10 * 1024 * 1024:
        raise ValidationError("File size exceeds 10MB limit. Please compress your file before uploading.")

def compress_image(image_field, max_width=1600):
    if not image_field:
        return image_field
    try:
        file_obj = getattr(image_field, 'file', None)
        # Only compress if it's a freshly uploaded file
        if not isinstance(file_obj, UploadedFile):
            return image_field
            
        Image.MAX_IMAGE_PIXELS = None # Allow huge files
        
        image_field.open()
        img = Image.open(image_field.file)
        
        if img.mode != 'RGB': img = img.convert('RGB')
        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int(float(img.height) * float(ratio))
            resample = getattr(Image, 'Resampling', Image).LANCZOS
            img = img.resize((max_width, new_height), resample)
            
        output = BytesIO()
        img.save(output, format='JPEG', quality=75, optimize=True)
        size = output.tell()
        output.seek(0)
        
        original_name = getattr(image_field, 'name', 'image.jpg')
        file_name = original_name.rsplit('.', 1)[0] + '.jpg' if '.' in original_name else original_name + '.jpg'
        
        return InMemoryUploadedFile(output, 'ImageField', file_name, 'image/jpeg', size, None)
    except Exception as e:
        print(f"Error compressing image: {e}")
        raise e

class ContactInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    course = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


class CourseEnquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Course Enquiry"
        verbose_name_plural = "Course Enquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.course} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


class BrochureRequest(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    college_or_place = models.CharField(max_length=255)
    course_slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Brochure Request"
        verbose_name_plural = "Brochure Requests"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.course_slug} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


class PlacedStudent(models.Model):
    image = models.ImageField(upload_to='placements/')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Placed Student"
        verbose_name_plural = "Placed Students"
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"Placed Student (ID: {self.id})"

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)


class Trainer(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)  # Represents designation / department
    image = models.ImageField(upload_to='Trainers/')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.course}"

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)


class Course(models.Model):
    slug = models.CharField(max_length=255, unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    rating = models.FloatField(default=5.0)
    image = models.ImageField(upload_to='courses/')
    highlights = models.JSONField(default=list)
    category = models.CharField(max_length=100)
    overview = models.TextField(blank=True, null=True)
    outcomes = models.JSONField(default=list, blank=True)
    syllabus = models.JSONField(default=list, blank=True)
    brochure = models.FileField(upload_to='brochures/', blank=True, null=True, validators=[validate_file_size], storage=get_raw_storage())
    instructors = models.ManyToManyField('Trainer', blank=True, related_name='courses_teaching')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)


class Career(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Career"
        verbose_name_plural = "Careers"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Career, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/', validators=[validate_file_size], storage=get_raw_storage())
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
        ordering = ['-created_at']

    def __str__(self):
        job_title = self.job.title if self.job else 'General Application'
        return f"{self.name} - {job_title}"
