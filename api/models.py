from django.db import models

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
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='placements/')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Placed Student"
        verbose_name_plural = "Placed Students"
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.name} - {self.position} ({self.course})"


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
    prerequisites = models.JSONField(default=list, blank=True)
    outcomes = models.JSONField(default=list, blank=True)
    syllabus = models.JSONField(default=list, blank=True)
    instructors = models.JSONField(default=list, blank=True)
    schedule = models.JSONField(default=dict, blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

