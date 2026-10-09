import os
import django
import sys

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from api.models import Course

courses = [
    {
        "slug": "masters-in-cyber-security--cloud-computing",
        "title": "Masters in Networking Cloud & Cybersecurity",
        "description": "Learn ethical hacking, penetration testing, security analysis, and comprehensive threat prevention techniques.",
        "duration": "12 months",
        "level": "Intermediate",
        "rating": 4.9,
        "image": "/cybersecurity.jpg",
        "category": "Security",
        "highlights": [
            "Ethical Hacking",
            "Penetration Testing",
            "Security Tools",
            "CEH Preparation",
        ],
        "overview": "Comprehensive cybersecurity training covering ethical hacking, penetration testing, and security analysis. Prepare for industry certifications while gaining hands-on experience with security tools.",
        "outcomes": [
            "Perform ethical hacking and penetration testing",
            "Identify and mitigate security vulnerabilities",
            "Use industry-standard security tools",
            "Prepare for CEH certification",
            "Implement security best practices",
        ],
        "syllabus": [
            {
                "module": "Topic 1: A+",
                "duration": " week 1",
                "topics": [
                    "Introduction & Hardware Basics",
                    "Storage, Peripherals & Operating Systems",
                    "Networking Basics",
                    "Security Fundamentals",
                ]
            },
            {
                "module": "Topic 2: N+",
                "duration": " week 2",
                "topics": [
                    "Introduction to Networking",
                    "Network Types",
                    "Network Devices & Cabling",
                ]
            }
        ]
    },
    {
        "slug": "masters-in-data-science-with-ai--ml",
        "title": "Masters in Data Science with AI & ML",
        "description": "Become an expert in AI & Data Science — build intelligent systems, chatbots,and deploy them professionally.",
        "duration": "6 months",
        "level": "Beginner to Advanced",
        "rating": 4.8,
        "image": "/ml.jpg",
        "category": "Programming",
        "highlights": [
            "Supervised & Unsupervised ML",
            "Deep Learning with TensorFlow & Keras",
            "NLP & Generative AI",
            "Model Deployment & Cloud",
        ],
        "overview": "Hands-on ML & AI program covering algorithms, neural networks, NLP, computer vision, and real-world projects.",
        "outcomes": [
            "Build predictive ML models for real-world datasets",
            "Apply clustering, dimensionality reduction, and ensemble learning",
            "Develop deep learning models for vision and NLP tasks",
        ],
        "syllabus": [
            {
                "module": "Python Programming Foundations",
                "duration": "Month 1",
                "topics": [
                    "Programming Concepts",
                    "Python Installation & Environment Setup",
                    "Variables, Data Types, Operators",
                ]
            }
        ]
    },
    {
        "slug": "master-in-python-full-stack-with-react--ai",
        "title": "Master's in Python Full Stack AI & Security",
        "description": "Complete Python programming course covering fundamentals, web development, Web Hosting, web Security & Ai Integration",
        "duration": "6 Months",
        "level": "Beginner to Advanced",
        "rating": 4.8,
        "image": "/django.jpg",
        "category": "Programming",
        "highlights": [
            "Web Development",
            "Security",
            "Api intergration",
            "Deployment",
        ],
        "overview": "Comprehensive Python programming course from basics to advanced topics. Learn web development with Django, React and Work with Real projects",
        "outcomes": [
            "Master Python programming fundamentals",
            "Build web applications with Django",
            "Api Intergrations",
            "Develop complete software projects",
        ],
        "syllabus": [
            {
                "module": "Module 1 – Python Programming Fundamentals",
                "duration": "week 1",
                "topics": [
                    "Introduction to Computer Hardware,software",
                    "Types of Languages",
                    "Algorithm,Flowchart",
                ]
            }
        ]
    }
]

for c in courses:
    Course.objects.update_or_create(
        slug=c['slug'],
        defaults=c
    )

print("Courses successfully seeded to database!")
