from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ContactInquiry, CourseEnquiry, BrochureRequest, PlacedStudent, Trainer, Course

class APIEndpointsTestCase(APITestCase):
    
    def test_contact_inquiry_creation(self):
        url = reverse('contact-inquiry')
        data = {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "1234567890",
            "course": "Data science",
            "message": "Hello, I am interested in data science."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactInquiry.objects.count(), 1)
        self.assertEqual(ContactInquiry.objects.get().name, "John Doe")

    def test_course_enquiry_creation(self):
        url = reverse('course-enquiry')
        data = {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "9876543210",
            "course": "Cyber Security & cloud computing",
            "message": "I would like to learn cybersecurity."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CourseEnquiry.objects.count(), 1)
        self.assertEqual(CourseEnquiry.objects.get().name, "Jane Smith")

    def test_brochure_request_creation(self):
        url = reverse('brochure-request')
        data = {
            "name": "Alice Johnson",
            "phone": "5555555555",
            "college_or_place": "ABC College",
            "course_slug": "data-science"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BrochureRequest.objects.count(), 1)
        self.assertEqual(BrochureRequest.objects.get().name, "Alice Johnson")

    def test_placed_students_list(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        # Create a small dummy image
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9'
            b'\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00'
            b'\x00\x02\x02\x4c\x01\x00\x3b'
        )
        uploaded_image = SimpleUploadedFile('test_student.gif', small_gif, content_type='image/gif')
        
        # Create a placed student
        student = PlacedStudent.objects.create(
            name="John Placed",
            course="Python",
            position="Junior Developer",
            image=uploaded_image
        )
        
        url = reverse('placed-students-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "John Placed")
        self.assertIn("image", response.data[0])
        # Clean up the test image file from disk
        student.image.delete(save=False)

    def test_trainers_list(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        # Create a small dummy image
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9'
            b'\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00'
            b'\x00\x02\x02\x4c\x01\x00\x3b'
        )
        uploaded_image = SimpleUploadedFile('test_trainer.gif', small_gif, content_type='image/gif')
        
        # Create a trainer
        trainer = Trainer.objects.create(
            name="Jane Trainer",
            course="Python Developer",
            image=uploaded_image,
            order=1
        )
        
        url = reverse('trainers-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Jane Trainer")
        self.assertIn("image", response.data[0])
        # Clean up the test image file from disk
        trainer.image.delete(save=False)

    def test_courses_list(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9'
            b'\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00'
            b'\x00\x02\x02\x4c\x01\x00\x3b'
        )
        uploaded_image = SimpleUploadedFile('test_course.gif', small_gif, content_type='image/gif')
        
        course = Course.objects.create(
            slug="test-course-slug",
            title="Test Course Title",
            description="Test Course Description",
            duration="3 Months",
            level="Beginner",
            rating=4.5,
            image=uploaded_image,
            category="Programming",
            highlights=["Highlight 1", "Highlight 2"],
            overview="Test Course Overview",
            prerequisites=["Prereq 1"],
            outcomes=["Outcome 1"],
            syllabus=[{"module": "Mod 1", "duration": "1 week", "topics": ["Topic 1"]}],
            instructors=[{"name": "Instructor 1", "title": "Trainer", "experience": "5 years"}],
            schedule={"weekdays": "Mon-Fri", "weekends": "Sat-Sun", "duration": "12 weeks"},
            order=1
        )
        
        url = reverse('course-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Course Title")
        self.assertEqual(response.data[0]['id'], "test-course-slug")
        self.assertIn("image", response.data[0])
        
        # Test course detail
        detail_url = reverse('course-detail', kwargs={'slug': 'test-course-slug'})
        detail_response = self.client.get(detail_url)
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data['title'], "Test Course Title")
        self.assertEqual(detail_response.data['id'], "test-course-slug")
        self.assertEqual(detail_response.data['highlights'], ["Highlight 1", "Highlight 2"])
        
        # Clean up the test image file from disk
        course.image.delete(save=False)


