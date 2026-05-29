import os
import sys
import shutil
from pathlib import Path

# Set up Django environment
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from api.models import Course

# Define the source and destination paths for images
src_public_dir = BASE_DIR.parent / 'frontend' / 'public'
dest_courses_dir = BASE_DIR / 'media' / 'courses'

# List of course images to copy
course_images = [
    "cybersecurity.jpg",
    "ml.jpg",
    "network.jpg",
    "django.jpg",
    "digital.jpg",
    "business-analytics.jpg",
    "logi.jpg",
    "logi1.jpg",
    "ui.jpg",
]

print("Copying course cover photos from public to backend/media/courses...")
if src_public_dir.exists():
    os.makedirs(dest_courses_dir, exist_ok=True)
    for img_name in course_images:
        src_file = src_public_dir / img_name
        dest_file = dest_courses_dir / img_name
        if src_file.is_file() and not dest_file.exists():
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {img_name}")
        elif not src_file.is_file():
            print(f"Warning: Source file {src_file} does not exist.")
else:
    print(f"Warning: Public folder {src_public_dir} not found!")

# Data to seed
courses_data = [
    {
        "slug": "masters-in-cyber-security--cloud-computing",
        "title": "Master's in Cyber Security & Cloud Computing",
        "description": "Learn ethical hacking, penetration testing, cloud security, and modern threat prevention techniques.",
        "duration": "12 Months",
        "level": "Most Placed",
        "rating": 4.9,
        "image": "courses/cybersecurity.jpg",
        "category": "Security",
        "highlights": [
            "Ethical Hacking",
            "Penetration Testing",
            "Network & Cloud Security",
            "Certification Prep",
        ],
        "overview": "Comprehensive cybersecurity training covering ethical hacking, penetration testing, and security analysis. Prepare for industry certifications while gaining hands-on experience with security tools.",
        "prerequisites": [
            "Basic networking knowledge",
            "Linux/Windows administration",
            "Programming basics helpful"
        ],
        "outcomes": [
            "Perform ethical hacking and penetration testing",
            "Identify and mitigate security vulnerabilities",
            "Use industry-standard security tools",
            "Prepare for CEH certification",
            "Implement security best practices"
        ],
        "syllabus": [
            {
                "module": "Topic 1: A+",
                "duration": "week 1",
                "topics": [
                    "Introduction & Hardware Basics",
                    "Storage, Peripherals & Operating Systems",
                    "Networking Basics",
                    "Security Fundamentals"
                ]
            },
            {
                "module": "Topic 2: N+",
                "duration": "week 2",
                "topics": [
                    "Introduction to Networking",
                    "Network Types",
                    "Network Devices & Cabling, Devices",
                    "IP Addressing & Subnetting",
                    "Network Topologies & Cloud Computing",
                    "Network Types"
                ]
            },
            {
                "module": "Topic 3: CCNA",
                "duration": "week 3-7",
                "topics": [
                    "Static Routing",
                    "Dynamic Routing Protocols",
                    "Switching Concepts",
                    "IP Services",
                    "Network Security",
                    "Network Troubleshooting"
                ]
            },
            {
                "module": "Topic 4: MCSE 2025 - Microsoft Certified Solutions Expert",
                "duration": "week 8-14",
                "topics": [
                    "Windows Server 2019,2022,2025 Fundamentals",
                    "Storage Configuration and Management",
                    "Understanding File Systems",
                    "Storage Configuration",
                    "iSCSI setup",
                    "LOCAL DISK",
                    "Active Directory Domain Services (AD DS)",
                    "Networking Services",
                    "Server Security & Protection",
                    "Server Virtualization with Hyper-V",
                    "Maintenance and Performance Monitoring",
                    "IP Address Management (IPAM)",
                    "Advanced Active Directory Topics",
                    "High Availability Solutions",
                    "Advanced Active Directory Topics",
                    "Installations"
                ]
            },
            {
                "module": "Topic 5: RHCE LINUX",
                "duration": "week 15-20",
                "topics": [
                    "Introduction to Red Hat Enterprise Linux",
                    "Working with the Linux Command Line",
                    "File and Directory Management",
                    "Working with Text Files",
                    "User and Group Administration",
                    "File Permissions and Access Control",
                    "perform site-to-site recovery by using Azure Site Recovery",
                    "Services and Daemon Management",
                    "SSH and Remote Access"
                ]
            },
            {
                "module": "Topic 6: VMWARE",
                "duration": "week 20",
                "topics": [
                    "Introduction to vmware and virtualization",
                    "Installing and configuring VMware vSphere",
                    "Virtual Machine Managment",
                    "Resource Managment and Monitoring"
                ]
            },
            {
                "module": "Topic 7: RMT",
                "duration": "week 21",
                "topics": [
                    "Introduction To RMT Tools",
                    "Types of RMT Tools"
                ]
            },
            {
                "module": "Topic 8: AZURE",
                "duration": "week 22",
                "topics": [
                    "Manage Azure AD objects",
                    "Manage role-based access control",
                    "Manage subscriptions and governance",
                    "configure Azure policies",
                    "Implement and manage storage",
                    "Configure name resolution",
                    "perform site-to-site recovery by using Azure Site Recovery"
                ]
            },
            {
                "module": "Topic 9: AWS",
                "duration": "week 23",
                "topics": [
                    "Introduction to Cloud Computing and AWS",
                    "AWS Core Services",
                    "Networking and Content Delivery",
                    "Identity, Access, and Security",
                    "Monitoring, Management, and Automation",
                    "Deployment and Infrastructure as Code (IaC)",
                    "Cost Management and Billing",
                    "AWS Security & Compliance",
                    "Real-Time Projects / Capstone"
                ]
            },
            {
                "module": "Topic 10: GCP(Google Cloud Platform)",
                "duration": "week 24",
                "topics": [
                    "Introduction to Cloud Technology",
                    "Gcp Overview",
                    "Compute Engine",
                    "Cloud Engine",
                    "Networking",
                    "Tools and Operations"
                ]
            },
            {
                "module": "Topic 11: Cyber Security",
                "duration": "week 25-40",
                "topics": [
                    "Introduction to Ethical Hacking",
                    "Footprinting and Reconnaissance",
                    "Scanning Networks",
                    "Enumeration",
                    "Vulnerability Analysis",
                    "System Hacking",
                    "Malware Threats",
                    "Sniffing",
                    "Social Engineering",
                    "Denial-of-Service",
                    "Session Hijacking",
                    "Evading IDS, Firewalls, and Honeypots",
                    "Hacking Web Servers",
                    "SQL Injection",
                    "Wi-Fi Hacking",
                    "Hacking Mobile Platforms",
                    "IoT Hacking",
                    "Cloud Computing",
                    "Cryptography",
                    "Introduction to Cyber Forensics",
                    "Artificial Intelligence in Cyber Security"
                ]
            }
        ],
        "instructors": [
            {"name": "Antony Bright", "title": "Cybersecurity Analyst", "experience": "2+ years"},
            {"name": "Arjun Sabu", "title": "System Administrator", "experience": "4+ years"},
            {"name": "Noel George", "title": "Network Engineer", "experience": "1+ years"}
        ],
        "schedule": {
            "weekdays": "Mon-Sat- 7:15 AM to 05:30 PM",
            "weekends": "Sunday Closed",
            "duration": "40 Weeks"
        }
    },
    {
        "slug": "masters-in-data-science-with-ai--ml",
        "title": "Masters in Data Science with AI & ML",
        "description": "Master deep learning, neural networks, NLP, machine learning models, and real-world AI projects.",
        "duration": "6 Months",
        "level": "Most Valuable",
        "rating": 4.8,
        "image": "courses/ml.jpg",
        "category": "Programming",
        "highlights": [
            "Deep Learning",
            "Neural Networks",
            "Natural Language Processing",
            "AI Projects",
        ],
        "overview": "Hands-on ML & AI program covering algorithms, neural networks, NLP, computer vision, and real-world projects. Learn to build and deploy intelligent systems and prepare for AI engineering careers.",
        "prerequisites": [
            "Proficiency in Python programming",
            "Basic knowledge of statistics and mathematics",
            "Understanding of fundamental ML concepts (preferred, not mandatory)"
        ],
        "outcomes": [
            "Build predictive ML models for real-world datasets",
            "Apply clustering, dimensionality reduction, and ensemble learning",
            "Develop deep learning models for vision and NLP tasks",
            "Work with Hugging Face and Generative AI APIs",
            "Deploy ML/AI models to cloud platforms",
            "Complete an end-to-end AI project"
        ],
        "syllabus": [
            {
                "module": "Python Programming Foundations",
                "duration": "Month 1",
                "topics": [
                    "Programming Concepts",
                    "Introduction to Programming",
                    "Python Installation & Environment Setup",
                    "Variables, Data Types, Operators",
                    "Input / Output Operations",
                    "Control Structures",
                    "Conditional Statements",
                    "Loops (for, while)",
                    "break, continue, pass",
                    "User-defined & Built-in Functions",
                    "Lists, Tuples, Sets",
                    "Dictionaries",
                    "Iteration Techniques",
                    "Modules & Packages",
                    "File Handling (CSV, TXT)",
                    "Exception Handling",
                    "Object-Oriented Programming (OOP)",
                    "Mini Project: simple calculator"
                ]
            },
            {
                "module": "Data Analysis, Excel, Statistics & Visualization",
                "duration": "Month 2",
                "topics": [
                    "Types of Data (Qualitative, Quantitative)",
                    "Mean, Median, Mode",
                    "Variance, Standard Deviation",
                    "Probability & Correlation",
                    "Linear Algebra Basics: Arrays & Matrix Operations",
                    "Indexing & Slicing",
                    "Mathematical Functions",
                    "Series & DataFrames",
                    "Data Cleaning & Wrangling",
                    "Formulas & Functions",
                    "Pivot Tables",
                    "Charts & Dashboards",
                    "Tableau: Connecting to Data Sources",
                    "Visual Analytics",
                    "Dashboards & Storytelling",
                    "Matplotlib (Bar, Line, Histogram, Pie)",
                    "Seaborn (Heatmaps, Boxplots)",
                    "GroupBy & Aggregation",
                    "Missing Value Handling",
                    "Mini Project: Exploratory Data Analysis on Real-World Dataset"
                ]
            },
            {
                "module": "Machine Learning",
                "duration": "Month 3",
                "topics": [
                    "ML Workflow",
                    "Types of Learning (Supervised, Unsupervised, Reinforcement)",
                    "Feature Selection",
                    "Train-Test Split",
                    "Model Evaluation Metrics",
                    "Linear Regression",
                    "Logistic Regression",
                    "K-Nearest Neighbors (KNN)",
                    "Decision Trees",
                    "Random Forest",
                    "Support Vector Machines (SVM)",
                    "Hyperparameter Tuning",
                    "K-Means Clustering",
                    "Hierarchical Clustering",
                    "Principal Component Analysis (PCA)",
                    "Mini Project:Customer Segmentation System"
                ]
            },
            {
                "module": "Deep Learning, NLP & Computer Vision",
                "duration": "Month 4",
                "topics": [
                    "Neural Networks",
                    "Activation & Loss Functions",
                    "Backpropagation",
                    "Model Building & Training",
                    "Artificial Neural Networks (ANN)",
                    "Convolutional Neural Networks (CNN)",
                    "Recurrent Neural Networks (RNN)",
                    "Transfer Learning",
                    "Text Preprocessing",
                    "TF-IDF & Word Embeddings",
                    "Sentiment Analysis",
                    "Image Processing",
                    "Face Detection",
                    "Object Detection Basics",
                    "Mini Project:Face Recognition System"
                ]
            },
            {
                "module": "Advanced AI & Generative Models",
                "duration": "Month 5",
                "topics": [
                    "Transformer Architecture",
                    "Pre-trained Models",
                    "Text Classification & Question Answering (QA)",
                    "YOLO Architecture",
                    "Custom Dataset Training",
                    "Real-Time Object Detection",
                    "LLaMA Overview",
                    "Prompt Engineering",
                    "LangChain (Chains, Agents, Memory)",
                    "OpenAI API",
                    "Gemini API",
                    "AI Chatbot Development",
                    "Mini Project: AI Chatbot using LangChain"
                ]
            },
            {
                "module": "R, SQL, Capstone & Career Preparation",
                "duration": "Month 6",
                "topics": [
                    "Data Manipulation with dplyr",
                    "Data Visualization with ggplot2",
                    "DBMS & RDBMS Concepts",
                    "MySQL / PostgreSQL",
                    "CRUD Operations",
                    "Joins & Subqueries",
                    "Mini Project:Sales Management Database"
                ]
            }
        ],
        "instructors": [
            {"name": "Anexa Thomas", "title": "Data Science Trainer", "experience": "3+ years"},
            {"name": "Robin Shiji", "title": "Python Trainer", "experience": "1.5+ years"}
        ],
        "schedule": {
            "weekdays": "Mon - Sat 07:00 AM to 05:00 PM",
            "weekends": "Sunday Closed",
            "duration": "24 weeks"
        }
    },
    {
        "slug": "masters-in-cloud-and-network-engineering",
        "title": "Master's in Cloud and Network Engineering",
        "description": "Master networking, switching, routing, cloud fundamentals, and hands-on infrastructure labs.",
        "duration": "8 Months",
        "level": "Most Placed",
        "rating": 4.8,
        "image": "courses/network.jpg",
        "category": "Networking",
        "highlights": [
            "CCNA Prep",
            "Hands-On Labs",
            "Industry Projects",
            "Placement"
        ],
        "overview": "This comprehensive networking course covers everything from basic network concepts to advanced routing and switching. You'll gain practical experience with Cisco equipment and prepare for industry certifications.",
        "prerequisites": [
            "Basic computer knowledge",
            "Understanding of operating systems"
        ],
        "outcomes": [
            "Configure and troubleshoot network devices",
            "Implement routing and switching protocols",
            "Design network topologies",
            "Prepare for CCNA certification",
            "Secure network infrastructure"
        ],
        "syllabus": [
            {
                "module": "Topic 1: A+",
                "duration": "week 1",
                "topics": [
                    "Introduction & Hardware Basics",
                    "Storage, Peripherals & Operating Systems",
                    "Networking Basics",
                    "Security Fundamentals"
                ]
            },
            {
                "module": "Topic 2: N+",
                "duration": "week 2",
                "topics": [
                    "Introduction to Networking",
                    "Network Types",
                    "Network Devices & Cabling, Devices",
                    "IP Addressing & Subnetting",
                    "Network Topologies & Cloud Computing",
                    "Network Types"
                ]
            },
            {
                "module": "Topic 3: CCNA",
                "duration": "week 3-7",
                "topics": [
                    "Static Routing",
                    "Dynamic Routing Protocols",
                    "Switching Concepts",
                    "IP Services",
                    "Network Security",
                    "Network Troubleshooting"
                ]
            },
            {
                "module": "Topic 4: MCSE 2025 - Microsoft Certified Solutions Expert",
                "duration": "week 8-14",
                "topics": [
                    "Windows Server 2019,2022,2025 Fundamentals",
                    "Storage Configuration and Management",
                    "Understanding File Systems",
                    "Storage Configuration",
                    "iSCSI setup",
                    "LOCAL DISK",
                    "Active Directory Domain Services (AD DS)",
                    "Networking Services",
                    "Server Security & Protection",
                    "Server Virtualization with Hyper-V",
                    "Maintenance and Performance Monitoring",
                    "IP Address Management (IPAM)",
                    "Advanced Active Directory Topics",
                    "High Availability Solutions",
                    "Advanced Active Directory Topics",
                    "Installations"
                ]
            },
            {
                "module": "Topic 5: RHCE LINUX",
                "duration": "week 15-20",
                "topics": [
                    "Introduction to Red Hat Enterprise Linux",
                    "Working with the Linux Command Line",
                    "File and Directory Management",
                    "Working with Text Files",
                    "User and Group Administration",
                    "File Permissions and Access Control",
                    "perform site-to-site recovery by using Azure Site Recovery",
                    "Services and Daemon Management",
                    "SSH and Remote Access"
                ]
            },
            {
                "module": "Topic 6: VMWARE",
                "duration": "week 20",
                "topics": [
                    "Introduction to vmware and virtualization",
                    "Installing and configuring VMware vSphere",
                    "Virtual Machine Managment",
                    "Resource Managment and Monitoring"
                ]
            },
            {
                "module": "Topic 7: RMT",
                "duration": "week 21",
                "topics": [
                    "Introduction To RMT Tools",
                    "Types of RMT Tools"
                ]
            },
            {
                "module": "Topic 8: AZURE",
                "duration": "week 22",
                "topics": [
                    "Manage Azure AD objects",
                    "Manage role-based access control",
                    "Manage subscriptions and governance",
                    "configure Azure policies",
                    "Implement and manage storage",
                    "Configure name resolution",
                    "perform site-to-site recovery by using Azure Site Recovery"
                ]
            },
            {
                "module": "Topic 9: AWS",
                "duration": "week 23",
                "topics": [
                    "Introduction to Cloud Computing and AWS",
                    "AWS Core Services",
                    "Networking and Content Delivery",
                    "Identity, Access, and Security",
                    "Monitoring, Management, and Automation",
                    "Deployment and Infrastructure as Code (IaC)",
                    "Cost Management and Billing",
                    "AWS Security & Compliance",
                    "Real-Time Projects / Capstone"
                ]
            },
            {
                "module": "Topic 10: GCP(Google Cloud Platform)",
                "duration": "week 24",
                "topics": [
                    "Introduction to Cloud Technology",
                    "Gcp Overview",
                    "Compute Engine",
                    "Cloud Engine",
                    "Networking",
                    "Tools and Operations"
                ]
            }
        ],
        "instructors": [
            {"name": "Sandip", "title": "Network Engineer", "experience": "5+ years"},
            {"name": "Noel George", "title": "Network Engineer", "experience": "2+ years"}
        ],
        "schedule": {
            "weekdays": "Mon-sat - 7:15 AM to 5:00 PM",
            "weekends": "Sunday Closed",
            "duration": "24 weeks"
        }
    },
    {
        "slug": "master-in-python-full-stack-with-react--ai",
        "title": "Master's in Python Full Stack with AI & Security",
        "description": "Learn backend + frontend with Python, Django, REST APIs, React.js, and AI integrations.",
        "duration": "6 Months",
        "level": "Recommended",
        "rating": 4.8,
        "image": "courses/django.jpg",
        "category": "Programming",
        "highlights": [
            "Django",
            "React.js",
            "API Integration",
            "Deployment"
        ],
        "overview": "Comprehensive Python programming course from basics to advanced topics. Learn web development with Django, React and Work with Real projects.",
        "prerequisites": [
            "Basic computer knowledge",
            "No prior programming experience required"
        ],
        "outcomes": [
            "Master Python programming fundamentals",
            "Build web applications with Django",
            "Api Intergrations",
            "Develop complete software projects"
        ],
        "syllabus": [
            {
                "module": "Module 1 - Python Programming Fundamentals",
                "duration": "week 1",
                "topics": [
                    "Introduction to Computer Hardware,software",
                    "Types of Languages",
                    "Algorithm,Flowchart",
                    "What is Python?",
                    "Data types and variables",
                    "Conditional Statements",
                    "For loop,While Loop",
                    "Array Collections",
                    "Function and Modules",
                    "Python Modules & Packages",
                    "File Handling",
                    "Exception Handling"
                ]
            },
            {
                "module": "Module 2: Advanced Python & AI Basics",
                "duration": "week 4",
                "topics": [
                    "Object Oriented Programming (OOPS)",
                    "Access modifiers",
                    "Abstract Class",
                    "Mysql Module Connector Installation",
                    "INTRODUCTION TO AI",
                    "ChatGPT & GitHub Copilot Usage",
                    "Prompt Engineering Basics",
                    "AI TOOLS FOR DEVELOPERS",
                    "Introduction to Artificial Intelligence",
                    "AI in Software Development",
                    "ChatGPT for Developers",
                    "GitHub Copilot",
                    "Google Gemini",
                    "Claude AI",
                    "Cursor AI"
                ]
            },
            {
                "module": "Module 3: Database programming",
                "duration": "Week 8",
                "topics": [
                    "Introduction to DBMS",
                    "MySQL Query Execution",
                    "CRUD operations",
                    "Database Integration"
                ]
            },
            {
                "module": "Module 4: Html",
                "duration": "week 10",
                "topics": [
                    "Introduction to HTML",
                    "Html tags"
                ]
            },
            {
                "module": "Module 5: Css",
                "duration": "week 12",
                "topics": [
                    "Introduction to Css",
                    "Css properties",
                    "Display properties",
                    "Css FlexBox",
                    "Position properties",
                    "Css Animations",
                    "Media Queries"
                ]
            },
            {
                "module": "Module 6: Bootstrap",
                "duration": "week 14",
                "topics": [
                    "How to add bootstrap",
                    "Bootstrap classes",
                    "Containers",
                    "Grid properties"
                ]
            },
            {
                "module": "Module 7: Javascript",
                "duration": "week 16",
                "topics": [
                    "How to add js",
                    "Js Events",
                    "Form Validation Using Js",
                    "Dom Manipulation",
                    "Fetch API",
                    "Jquery & Ajax"
                ]
            },
            {
                "module": "Module 8: React Js",
                "duration": "Week 18",
                "topics": [
                    "Introduction",
                    "Installation",
                    "Architecture",
                    "React Features",
                    "ReactJS - Creating a React application",
                    "Simple application using CDN",
                    "Complex application using React Create App CLI",
                    "Complex application using customised method",
                    "JSX",
                    "Components",
                    "Class Component",
                    "Function Component",
                    "ECMAScript 6",
                    "Arrow Functions",
                    "Variables (let, const, var)",
                    "Array methods (map)",
                    "Spread Operator (...)",
                    "Styling",
                    "Properties",
                    "Events",
                    "Conditionals",
                    "Lists",
                    "Forms",
                    "Form Validation Using JS",
                    "Grid properties",
                    "Router",
                    "React Hooks",
                    "useState",
                    "useEffect",
                    "useContext",
                    "REST APIs in React",
                    "Fetch API",
                    "Axios",
                    "Environment variables"
                ]
            },
            {
                "module": "Module 9: Web Programming with Django",
                "duration": "Week 18 - 22",
                "topics": [
                    "Introduction to Web Programming",
                    "Web Server",
                    "Web Client",
                    "Network Protocols",
                    "CGI Programming",
                    "Django Framework",
                    "Installation",
                    "Configuration",
                    "Model-View-Template (MVT) Architecture",
                    "Template Inheritance",
                    "URL Routing",
                    "Form Processing",
                    "Model Forms",
                    "User Registration and Authentication",
                    "Django Admin Panel",
                    "Email Integration",
                    "Introduction to REST Framework",
                    "REST API",
                    "JSON Module",
                    "Serialization",
                    "Enviornment variables"
                ]
            },
            {
                "module": "Module 10: Git",
                "duration": "Week 23",
                "topics": [
                    "Introduction to Git",
                    "Creating and Initializing a Repository",
                    "Understanding Branches",
                    "Creating and Switching Branches",
                    "Merging Branches",
                    "Pushing Code to Remote Repository",
                    "Cloning and Pulling from Repository"
                ]
            },
            {
                "module": "Module 11: Deployment",
                "duration": "Week 24",
                "topics": [
                    "Introduction to Deployment",
                    "Deployment Workflow and Best Practices",
                    "Frontend Deployment with Vercel",
                    "Setting up a Vercel Account",
                    "Connecting GitHub Repository",
                    "Deploying React Applications",
                    "Environment Variables in Vercel",
                    "Continuous Deployment with Vercel",
                    "Backend Deployment with PythonAnywhere",
                    "Setting up a PythonAnywhere Account",
                    "Uploading Django Project",
                    "Database Configuration",
                    "Static & Media Files Setup",
                    "Environment Variables in PythonAnywhere",
                    "Testing and Running the Deployed Application",
                    "Connecting GitHub for CI/CD"
                ]
            },
            {
                "module": "Module 12: Cyber Security for Developers",
                "duration": "Week 25",
                "topics": [
                    "Introduction to Cyber Security",
                    "Basic Security Concepts",
                    "Security Principles",
                    "Common Web Vulnerabilities",
                    "Security Best Practices",
                    "OWASP Top 10",
                    "Authentication & Authorization",
                    "Introduction for Developers"
                ]
            }
        ],
        "instructors": [
            {"name": "Robin shiji", "title": "Software Developer & Project Incharge", "experience": "2+ years"}
        ],
        "schedule": {
            "weekdays": "Mon-sat 7:15 AM to 05:00 PM",
            "weekends": "Sunday Closed",
            "duration": "25 weeks"
        }
    },
    {
        "slug": "masters-in-digital-marketing-with-ai",
        "title": "Master's in Digital Marketing with AI",
        "description": "Master SEO, social media marketing, PPC ads, analytics, and modern AI marketing tools.",
        "duration": "6 Months",
        "level": "Recommended",
        "rating": 4.6,
        "image": "courses/digital.jpg",
        "category": "Marketing",
        "highlights": [
            "SEO",
            "Social Media",
            "Google Ads",
            "AI Tools"
        ],
        "overview": "Comprehensive digital marketing course covering all major channels and strategies. Learn to create, execute, and optimize digital marketing campaigns that drive real business results.",
        "prerequisites": [
            "Basic computer skills",
            "Understanding of social media platforms"
        ],
        "outcomes": [
            "Develop comprehensive digital marketing strategies",
            "Execute SEO and SEM campaigns",
            "Create engaging social media content",
            "Manage Google Ads and Facebook advertising",
            "Analyze and optimize campaign performance"
        ],
        "syllabus": [
            {
                "module": "Foundations of Digital Marketing",
                "duration": "Month 1",
                "topics": [
                    "Introduction to Digital Marketing concepts",
                    "Digital vs Traditional Marketing",
                    "Inbound & Outbound Marketing",
                    "Marketing Funnel & Lead Generation",
                    "Website basics: Domain, Hosting, UI/UX",
                    "Canva design & Landing page basics",
                    "Keyword Research & Competitor Analysis",
                    "SEO fundamentals: On-page, Off-page & Technical SEO"
                ]
            },
            {
                "module": "Performance Marketing & Advertising",
                "duration": "Month 2",
                "topics": [
                    "Google Ads setup & campaign management",
                    "Search ads, keyword bidding & ad copy",
                    "Conversion tracking with GA4",
                    "Social Media Marketing strategy",
                    "Facebook & Instagram marketing",
                    "Meta Ads Manager & paid campaigns",
                    "YouTube channel setup & video SEO",
                    "Google Business Profile & Local SEO"
                ]
            },
            {
                "module": "SEO, Analytics & Optimization",
                "duration": "Month 3",
                "topics": [
                    "Advanced on-page SEO & content optimization",
                    "Keyword mapping & internal linking",
                    "Technical SEO & website speed optimization",
                    "Backlink building & SEO audits",
                    "Google Analytics 4 setup",
                    "Traffic, user behaviour & conversion analysis",
                    "Conversion Rate Optimization (CRO)",
                    "A/B testing & funnel optimization"
                ]
            },
            {
                "module": "AI, Tools & Automation",
                "duration": "Month 4",
                "topics": [
                    "Introduction to AI in Digital Marketing",
                    "AI-based consumer behaviour analysis",
                    "AI tools for content, images & videos",
                    "AI tools for SEO, ads & analytics",
                    "Prompt engineering basics",
                    "Marketing automation & email funnels",
                    "CRM integration & workflow automation",
                    "WhatsApp marketing & chatbot automation"
                ]
            },
            {
                "module": "Growth, Psychology & Emerging Tech",
                "duration": "Month 5",
                "topics": [
                    "Growth marketing fundamentals",
                    "User acquisition & growth funnels",
                    "Data-driven marketing strategies",
                    "Campaign analysis & lifecycle marketing",
                    "Neuromarketing & consumer psychology",
                    "Emotional triggers & psychology-based copywriting",
                    "Blockchain basics & Web3 marketing",
                    "NFTs & brand engagement concepts"
                ]
            },
            {
                "module": "Career, Projects & Certification",
                "duration": "Month 6",
                "topics": [
                    "360-degree & omnichannel marketing",
                    "Live SEO & Google Ads projects",
                    "AI tools & WhatsApp automation projects",
                    "Campaign performance review",
                    "Freelancing platforms & client handling",
                    "Pricing, proposals & reporting",
                    "Industry case studies",
                    "Portfolio building & certification"
                ]
            }
        ],
        "instructors": [
            {"name": "John Kuriakos", "title": "Digital Marketing Professional", "experience": "3+ years"}
        ],
        "schedule": {
            "weekdays": "Mon - Sat 07:15 AM to 05:00 PM",
            "weekends": "Sunday Closed",
            "duration": "24 weeks"
        }
    },
    {
        "slug": "professional-data-analytics-engineer",
        "title": "Professional Data Analytics Engineer",
        "description": "Develop analytical skills for business using Python, visualization, and predictive modeling.",
        "duration": "4 Months",
        "level": "New",
        "rating": 4.8,
        "image": "courses/business-analytics.jpg",
        "category": "Programming",
        "highlights": [
            "Python Analytics",
            "Visualization",
            "Predictive Models",
            "Reporting"
        ],
        "overview": "Comprehensive 4-month business analytics program. Master Python, Excel, SQL, and visualization tools to solve real-world business problems and deliver actionable insights.",
        "prerequisites": [
            "Basic computer skills",
            "Familiarity with spreadsheets (preferred)",
            "No prior coding required (Python basics covered in course)"
        ],
        "outcomes": [
            "Perform business data analysis using Python & Excel",
            "Design interactive dashboards with Tableau/Power BI",
            "Apply SQL for querying and extracting business insights",
            "Build KPI-driven reports and visualizations",
            "Deliver an end-to-end business analytics capstone project"
        ],
        "syllabus": [
            {
                "module": "Python Programming",
                "duration": "Month 1",
                "topics": [
                    "What is Programming?",
                    "Applications of Python",
                    "Python Installation (Anaconda, VS Code, Jupyter)",
                    "Python Syntax & Indentation",
                    "Variables & Keywords",
                    "Data Types: int, float, string, boolean",
                    "Input & Output Functions",
                    "Conditional Statements (if, elif, else)",
                    "Loops (for, while)",
                    "break, continue, pass",
                    "Functions (User-defined & Built-in)",
                    "Arguments & Return Values",
                    "Lambda Functions",
                    "Hands-on Practice",
                    "Number Guessing Game",
                    "Pattern Printing Programs",
                    "Strings & String Methods",
                    "Lists, Tuples, Sets",
                    "Dictionaries",
                    "Indexing & Slicing",
                    "Iteration Techniques",
                    "Modules & Packages",
                    "File Handling (Text, CSV, Excel)",
                    "Exception Handling",
                    "OOP Concepts",
                    "Type Casting",
                    "Operators (Arithmetic, Relational, Logical, Assignment)",
                    "Hands-on: Simple Calculator",
                    "Basic Python Programs",
                    "Mini Project: Python Data Processing System"
                ]
            },
            {
                "module": "DATA ANALYSIS TOOLS & EDA",
                "duration": "Month 2",
                "topics": [
                    "NumPy Arrays",
                    "Array Creation Methods",
                    "Indexing & Slicing",
                    "Mathematical & Statistical Functions",
                    "Matrix Operations",
                    "Series & DataFrames",
                    "Reading CSV & Excel Files",
                    "Data Cleaning",
                    "Handling Missing Values",
                    "GroupBy & Aggregation",
                    "Merging & Joining",
                    "Hands-on: Sales Data Analysis",
                    "Matplotlib (Line, Bar, Histogram, Pie)",
                    "Seaborn (Boxplot, Heatmap, Countplot)",
                    "Plot Customization",
                    "Data Cleaning Techniques",
                    "Outlier Detection",
                    "Correlation Analysis",
                    "Feature Understanding",
                    "Mini Project:Complete EDA on real dataset"
                ]
            },
            {
                "module": "MACHINE LEARNING",
                "duration": "Month 3",
                "topics": [
                    "AI vs ML vs Deep Learning",
                    "Types of Machine Learning",
                    "Machine Learning Lifecycle",
                    "Data Preprocessing",
                    "Feature Scaling",
                    "Train-Test Split",
                    "Scikit-learn Basics",
                    "Linear Regression",
                    "Multiple Linear Regression",
                    "Logistic Regression",
                    "K-Nearest Neighbors (KNN)",
                    "Decision Tree",
                    "Random Forest",
                    "Bias-Variance Tradeoff",
                    "Accuracy, Precision, Recall",
                    "F1 Score",
                    "Confusion Matrix",
                    "R², MAE, MSE, RMSE",
                    "Feature Importance",
                    "Hyperparameter Tuning",
                    "Unsupervised Learning",
                    "K-Means Clustering",
                    "Mini Project:ML Prediction / Classification Model"
                ]
            },
            {
                "module": "Excel, SQL, NoSQL, R & BI Tools",
                "duration": "Month 4",
                "topics": [
                    "Excel Interface",
                    "Data Formatting",
                    "Formulas & Functions",
                    "IF, COUNTIF, SUMIF",
                    "VLOOKUP, HLOOKUP, XLOOKUP",
                    "Pivot Tables & Charts",
                    "DBMS & RDBMS Concepts",
                    "Creating Databases & Tables",
                    "CRUD Operations (SQL)",
                    "WHERE, ORDER BY, LIMIT",
                    "Aggregate Functions",
                    "JOINs (INNER, LEFT, RIGHT)",
                    "Subqueries",
                    "Views & Indexes",
                    "What is NoSQL?",
                    "SQL vs NoSQL",
                    "MongoDB Architecture",
                    "Documents & Collections",
                    "CRUD Operations (MongoDB)",
                    "Aggregation Pipeline",
                    "MongoDB with Python",
                    "R Programming Basics",
                    "R & RStudio",
                    "R Data Types & Structures",
                    "dplyr for Data Manipulation",
                    "ggplot2 for Visualization",
                    "Exploratory Data Analysis (EDA) using R",
                    "Power BI Overview",
                    "Power Query",
                    "Data Modeling",
                    "DAX Basics",
                    "Dashboard Creation (Power BI)",
                    "Tableau Overview",
                    "Charts & Dashboards (Tableau)",
                    "Filters, Parameters & Actions",
                    "What is Generative AI",
                    "Traditional AI vs Gen AI",
                    "Use cases of Gen AI",
                    "GPT, Gemini, Claude (overview)",
                    "Prompt engineering basics",
                    "Zero-shot & Few-shot prompting",
                    "Chat GPT for data analysis",
                    "AI-assisted coding",
                    "AI for Excel, SQL & Python",
                    "What is Lang Chain",
                    "Prompt templates",
                    "Simple LLM pipelines"
                ]
            },
            {
                "module": "FINAL CAPSTONE PROJECT",
                "duration": "",
                "topics": [
                    "Python",
                    "EDA",
                    "Machine Learning",
                    "SQL / NoSQL",
                    "R Programming",
                    "BI Dashboard",
                    "Generative AI support"
                ]
            }
        ],
        "instructors": [
            {"name": "Anexa Thomas", "title": "Technical Head - Software Dept", "experience": "3+ years"}
        ],
        "schedule": {
            "weekdays": "Mon - Sat 07:00 AM to 05:00 PM",
            "weekends": "Sunday Closed",
            "duration": "6 months"
        }
    },
    {
        "slug": "professional-diploma-in-logistics--supply-chain-management",
        "title": "Professional Diploma in Logistics & Supply Chain Management",
        "description": "To equip learners with practical and theoretical knowledge of logistics operations, supply chain management, inventory control, transportation, and global trade practices.",
        "duration": "6 Months",
        "level": "Highly Recommended",
        "rating": 4.9,
        "image": "courses/logi.jpg",
        "category": "Logistics",
        "highlights": [
            "FICS Certification(Uk Accredited)",
            "Warehouse Management System(WMS Certification)",
            "WMS Software",
            "KCDS (Govt of india recongnized certification)"
        ],
        "overview": "This 6-month Professional Diploma in Logistics & Supply Chain Management equips learners with practical and theoretical expertise in inventory planning, warehouse management, transportation, procurement, and international trade. Develop the skills required to manage efficient, cost-effective supply chain operations in today’s global business environment.",
        "prerequisites": [
            "Basic computer knowledge",
            "Basic understanding of business, commerce, or operations (preferred)",
            "Interest in logistics, supply chain, or warehouse management",
            "No prior experience required"
        ],
        "outcomes": [
            "Understand end-to-end supply chain operations and logistics processes",
            "Apply inventory control techniques to optimize stock levels",
            "Manage warehouse operations and distribution systems efficiently",
            "Plan and coordinate transportation and freight operations",
            "Handle procurement, vendor management, and global trade documentation",
            "Analyze supply chain performance and implement cost-reduction strategies"
        ],
        "syllabus": [
            {
                "module": "Supply Chain Management",
                "duration": "Month 1",
                "topics": [
                    "Fundamentals of Supply Chain Management",
                    "Supply Chain Network & Design",
                    "Value Chain and Supply Chain Framework",
                    "Supply Chain Planning & Coordination",
                    "Technology and Performance in SCM"
                ]
            },
            {
                "module": "Management in Logistics & Transport",
                "duration": "Month 2",
                "topics": [
                    "Introduction to Logistics Management",
                    "Strategic Integrated Logistics Management",
                    "Logistics Planning and Strategy",
                    "Demand Management and Logistics System Design",
                    "Logistics Network Design",
                    "Transport Management",
                    "Measuring Logistics Performance and Global Logistics"
                ]
            },
            {
                "module": "Multimodal Transport Operations",
                "duration": "Month 3",
                "topics": [
                    "Introduction to Multimodal Transport Operations",
                    "Transportation Systems in India",
                    "Air, Sea and Courier Transportation",
                    "Cargo, Rail and Containerized Transport",
                    "Regulatory Framework and Statutory Bodies",
                    "Public–Private Participation and Multimodal Growth"
                ]
            },
            {
                "module": "Warehouse Management",
                "duration": "Month 4",
                "topics": [
                    "Introduction to Warehousing",
                    "Warehouse Operations and Procedures",
                    "Warehouse Equipment and Cargo Handling",
                    "Warehouse Layout and Storage Systems",
                    "Inventory Management in Warehouses",
                    "Warehouse Management Systems (WMS)",
                    "Warehouse Workforce and Security Management",
                    "Safety, Performance and Cost Management"
                ]
            },
            {
                "module": "Inventory Management",
                "duration": "Month 5",
                "topics": [
                    "Introduction to Inventory",
                    "Inventory Management Concepts",
                    "Inventory Management Techniques",
                    "Stock Levels and Types of Inventory",
                    "Materials Management",
                    "Procurement Management",
                    "Procurement Documentation",
                    "Role of Inventory Manager"
                ]
            },
            {
                "module": "Network Integration Management",
                "duration": "Month 6",
                "topics": [
                    "Introduction to Network Integration",
                    "Supply Chain Drivers and Integration",
                    "Sales & Operations Planning (S&OP) and CPFR",
                    "Risk Management, Insurance and Dangerous Goods",
                    "Regulatory Framework and Taxation",
                    "Legal Aspects in Logistics and Courier Services",
                    "Network Analysis and Case Study"
                ]
            },
            {
                "module": "Business Communication & Organizational Behaviour",
                "duration": "Month 6",
                "topics": [
                    "Introduction to Business Communication",
                    "Business Communication Skills",
                    "Business Presentations and Meetings",
                    "Interpersonal Communication and Workplace Skills",
                    "Introduction to Organizational Behaviour",
                    "Individual Behaviour",
                    "Motivation and Group Behaviour",
                    "Organizational Structure and Work Environment"
                ]
            }
        ],
        "instructors": [
            {"name": "Franklin", "title": "Logistics Expert", "experience": "5+ years"}
        ],
        "schedule": {
            "weekdays": "Mon - Sat 07:00 AM to 05:00 PM",
            "weekends": "Sunday Closed",
            "duration": "6 months"
        }
    },
    {
        "slug": "masters-program-in-logistics--supply-chain-management-",
        "title": "Master's Program in Logistics & Supply Chain Management",
        "description": "To develop advanced managerial, analytical, and strategic competencies in Logistics and SupplyChain Management with strong industry orientation and internship exposure.",
        "duration": "Highly Recommended",
        "level": "New one",
        "rating": 4.9,
        "image": "courses/logi1.jpg",
        "category": "Logistics",
        "highlights": [
            "FICS Certification(Uk Accredited)",
            "Warehouse Management System(WMS Certification)",
            "WMS Software",
            "KCDS (Govt of india recongnized certification)"
        ],
        "overview": "This 12-month Masters in Logistics & Supply Chain Management equips learners with practical and theoretical expertise in inventory planning, warehouse management, transportation, procurement, and international trade. Develop the skills required to manage efficient, cost-effective supply chain operations in today’s global business environment.",
        "prerequisites": [
            "Basic computer knowledge",
            "Basic understanding of business, commerce, or operations (preferred)",
            "Interest in logistics, supply chain, or warehouse management",
            "No prior experience required"
        ],
        "outcomes": [
            "Understand end-to-end supply chain operations and logistics processes",
            "Apply inventory control techniques to optimize stock levels",
            "Manage warehouse operations and distribution systems efficiently",
            "Plan and coordinate transportation and freight operations",
            "Handle procurement, vendor management, and global trade documentation",
            "Analyze supply chain performance and implement cost-reduction strategies"
        ],
        "syllabus": [
            {
                "module": "Supply Chain Management",
                "duration": "Month 1",
                "topics": [
                    "Fundamentals of Supply Chain Management",
                    "Supply Chain Network & Design",
                    "Value Chain and Supply Chain Framework",
                    "Supply Chain Planning & Coordination",
                    "Technology and Performance in SCM"
                ]
            },
            {
                "module": "Management in Logistics & Transport",
                "duration": "Month 2",
                "topics": [
                    "Introduction to Logistics Management",
                    "Strategic Integrated Logistics Management",
                    "Logistics Planning and Strategy",
                    "Demand Management and Logistics System Design",
                    "Logistics Network Design",
                    "Transport Management",
                    "Measuring Logistics Performance and Global Logistics"
                ]
            },
            {
                "module": "Multimodal Transport Operations",
                "duration": "Month 3",
                "topics": [
                    "Role of Logistics and Integrated Logistics Systems",
                    "Need, Merits, and Modalities of Multimodal Transport",
                    "Indian Road Corridors",
                    "Indian Railway Administration and Railways Act, 1989",
                    "National Waterways and Sagarmala Projects",
                    "Air Transport: Private Players, UDAN, Ghost Airports, GAGAN",
                    "Courier Industry and Benefits of Transportation",
                    "Cargo Types and Catchment Areas",
                    "WRS, TOFC & COFC",
                    "WDRA and Its Functions",
                    "Statutory Bodies and DGS",
                    "PPP Concepts in Transport",
                    "Welfare Activities in Indian Transport System"
                ]
            },
            {
                "module": "Warehouse Management",
                "duration": "Month 4",
                "topics": [
                    "Warehousing Concepts and Types of Warehouses",
                    "Warehouse Operations and Procedures",
                    "Material Handling Equipment (MHE)",
                    "Types of Cargo Handling",
                    "Warehouse Principles and Management",
                    "Major and Minor Warehouse Activities",
                    "Warehouse Workforce Responsibilities",
                    "Warehouse Layouts and Storage Methods",
                    "Inventory Types and SKUs",
                    "Importance of Inventory Management in Warehouses",
                    "Types of WMS",
                    "Latest Warehouse Technologies",
                    "Warehouse SOPs and Safety Measures",
                    "Roles of Warehouse Security",
                    "Warehouse KPIs",
                    "Efficient Warehouse Strategies",
                    "Warehouse Costs and Functions"
                ]
            },
            {
                "module": "Inventory Management",
                "duration": "Month 5",
                "topics": [
                    "Introduction to Inventory",
                    "Inventory Management Concepts",
                    "Inventory Management Techniques",
                    "Stock Levels and Types of Inventory",
                    "Materials Management",
                    "Procurement Management",
                    "Procurement Documentation",
                    "Role of Inventory Manager"
                ]
            },
            {
                "module": "Network Integration Management",
                "duration": "Month 6",
                "topics": [
                    "Introduction to Network Integration",
                    "Supply Chain Drivers and Integration",
                    "Sales & Operations Planning (S&OP) and CPFR",
                    "Risk Management, Insurance and Dangerous Goods",
                    "Regulatory Framework and Taxation",
                    "Legal Aspects in Logistics and Courier Services",
                    "Network Analysis and Case Study"
                ]
            },
            {
                "module": "Business Communication & Organizational Behaviour",
                "duration": "Month 7",
                "topics": [
                    "Introduction to Business Communication",
                    "Communication Process and Skills",
                    "Listening Skills",
                    "Business Presentations and Meetings",
                    "Meetings and Conferences",
                    "interview skills",
                    "Resume making"
                ]
            },
            {
                "module": "Organizational Behaviour",
                "duration": "Month 8",
                "topics": [
                    "Scope and Importance of OB",
                    "Goals and Functions of OB",
                    "Personality and Determinants",
                    "Perception and Attitudes",
                    "Motivation",
                    "Group Behaviour and Cohesion",
                    "Organizationa structure",
                    "Conflict Managment",
                    "Stress and Burnout Managment"
                ]
            },
            {
                "module": "INTERNATIONAL TRADE, EXIM & SHIPPING M",
                "duration": "Month 9",
                "topics": [
                    "EXIM Documentation & Procedures",
                    "Commercial Shipping Management",
                    "International Business Environment",
                    "Commercial Shipping Management"
                ]
            },
            {
                "module": "ARTIFICIAL INTELLIGENCE & DIGITAL TRANSFORMATION IN LOGISTICSAND SCM",
                "duration": "Month 10",
                "topics": [
                    "AI Fundamentals for Logistics & SCM",
                    "Machine Learning Applications in Supply Chain",
                    "AI in Logistics Operations",
                    "AI for Risk, Compliance and Decision Support",
                    "Digital Supply Chain & Emerging Technologies",
                    "AI Tools, ERP Integration & Case Studies"
                ]
            },
            {
                "module": "Industry Internship",
                "duration": "Month 11-12",
                "topics": [
                    "Internship with approved logistics / SCM organizations",
                    "Live Project Work",
                    "Internship Report Submission",
                    "Final Viva Voce"
                ]
            }
        ],
        "instructors": [
            {"name": "Franklin", "title": "Logistics Director", "experience": "8+ years"}
        ],
        "schedule": {
            "weekdays": "Mon - Sat 07:00 AM to 05:00 PM",
            "weekends": "Sunday Closed",
            "duration": "12 months"
        }
    },
    {
        "slug": "ui-and-ux-designing-course",
        "title": "UI & UX Designing Course",
        "description": "Learn user interface and user experience design with wireframing, prototyping, design systems, Figma, and real-world UI/UX projects.",
        "duration": "3 Months",
        "level": "Most Valuable",
        "rating": 4.8,
        "image": "courses/ui.jpg",
        "category": "Designing",
        "highlights": [
            "UI Design",
            "UX Research",
            "Wireframing & Prototyping",
            "Figma Projects"
        ],
        "overview": "This comprehensive UI & UX Designing course equips learners with practical and creative skills in user interface design, user experience design, wireframing, prototyping, usability testing, and interactive design using industry-standard tools like Figma, Canva, and Adobe Photoshop. Students will build responsive and visually engaging digital experiences through real-world projects and portfolio development.",
        "prerequisites": [
            "Basic computer knowledge",
            "Creativity and interest in design",
            "Basic understanding of internet and mobile applications",
            "No prior coding or design experience required"
        ],
        "outcomes": [
            "Understand the complete UI & UX design process",
            "Design responsive user interfaces using Figma and Photoshop",
            "Create wireframes, prototypes, and interactive user flows",
            "Apply visual design principles, typography, and color psychology",
            "Conduct user research and usability testing",
            "Build professional UI/UX portfolio projects for career opportunities"
        ],
        "syllabus": [
            {
                "module": "Introduction to UI & UX Design",
                "topics": [
                    "Introduction to UI & UX",
                    "Why UI and UX is used?",
                    "Benefits and purpose of UI and UX",
                    "Difference between UI & UX",
                    "How do UI & UX process fit together",
                    "UCD Process and its phases"
                ]
            },
            {
                "module": "Adobe Photoshop",
                "topics": [
                    "Introduction to Adobe Photoshop",
                    "Overview of tools (Adobe, Canva, Figma)",
                    "Adobe Installation",
                    "Interface and Tools in Photoshop",
                    "Shortcut Keys in Photoshop"
                ]
            },
            {
                "module": "Basics of Visual Design",
                "topics": [
                    "Panels in Photoshop",
                    "Using Pen Tool",
                    "Photocollage",
                    "Working with layers in Photoshop",
                    "Colour theory and its application"
                ]
            },
            {
                "module": "Design with Photoshop",
                "topics": [
                    "Creating UI elements in Photoshop (Buttons, Icons)",
                    "Clipping and Layer Masking",
                    "Image Editing and Manipulation"
                ]
            },
            {
                "module": "Designing",
                "topics": [
                    "Poster Design",
                    "Instagram Post Design"
                ]
            },
            {
                "module": "Advanced Photoshop Techniques",
                "topics": [
                    "Layer Styles & Blending Modes",
                    "Using Brush Tool",
                    "How to remove background",
                    "Exporting assets for mobile"
                ]
            },
            {
                "module": "UI Kit in Photoshop",
                "topics": [
                    "Double Exposure",
                    "Dropdown Buttons",
                    "Radio Button",
                    "Check Button",
                    "Play Buttons"
                ]
            },
            {
                "module": "Animations in Photoshop",
                "topics": [
                    "Creating UI Design Kit",
                    "Types of Buttons in Photoshop",
                    "GIF Animations",
                    "Colour Splashes"
                ]
            },
            {
                "module": "Introduction to Figma",
                "topics": [
                    "Introduction to Figma",
                    "Figma Features",
                    "Setting up a Design Project in Figma",
                    "Interface and Tools in Figma",
                    "Boolean Operations in Figma"
                ]
            },
            {
                "module": "Figma Plugins and Integrations",
                "topics": [
                    "Figma Plugins",
                    "Advantages of Plugins",
                    "Types of Plugins",
                    "Iconify",
                    "iUnsplash",
                    "Storyset",
                    "Remove Background",
                    "Blobs",
                    "Lorem Ipsum",
                    "Roundall"
                ]
            },
            {
                "module": "Introduction to Canva",
                "topics": [
                    "Introduction to Canva",
                    "Creating Canva Account",
                    "Interface and Tools",
                    "Collaboration Features in Canva"
                ]
            },
            {
                "module": "Design with Canva",
                "topics": [
                    "Designing Posters",
                    "Designing Banners in Canva",
                    "Using Canva for Quick Prototyping",
                    "Creating Social Media Graphics in Canva"
                ]
            },
            {
                "module": "Designing a Logo",
                "topics": [
                    "Logo Designing",
                    "Colour Palettes",
                    "Uses of Colour Palettes",
                    "Importance of Colours"
                ]
            },
            {
                "module": "Design Process in UI & UX",
                "topics": [
                    "Design Thinking Process",
                    "Brand Strategies",
                    "Typography and Logo Types",
                    "Colours and Types",
                    "Colour Psychology"
                ]
            },
            {
                "module": "Designing Basic Components in Figma",
                "topics": [
                    "Ad Components in Figma",
                    "Variants",
                    "Grouping and Ungrouping",
                    "Adding Hover Effects for Components",
                    "Colour Pickers",
                    "Exporting Designs and Assets from Figma"
                ]
            },
            {
                "module": "UI/UX Case Study",
                "topics": [
                    "Understanding User Research",
                    "Conducting User Interviews and Surveys",
                    "Creating Personas",
                    "Competitive Analysis"
                ]
            },
            {
                "module": "Prototyping",
                "topics": [
                    "Working with Frames",
                    "Working with Layers",
                    "Prototyping in Figma",
                    "Creating Interactive Prototypes in Figma"
                ]
            },
            {
                "module": "Mapping in UI/UX",
                "topics": [
                    "Introduction to UX Design Principles",
                    "User Journey Mapping",
                    "Mind Mapping",
                    "Sketching"
                ]
            },
            {
                "module": "Flowcharts",
                "topics": [
                    "Information Architecture and Sitemap",
                    "Flowchart",
                    "Mermaid Code in draw.io"
                ]
            },
            {
                "module": "Wireframing",
                "topics": [
                    "Wireframing",
                    "Creating Wireframing in Figma",
                    "Types of Wireframing",
                    "Low Fidelity Wireframing"
                ]
            },
            {
                "module": "Wireframing & Prototyping",
                "topics": [
                    "Best Practices for Wireframing",
                    "From Wireframing to Prototyping",
                    "Case Study on Effective Wireframing"
                ]
            },
            {
                "module": "Design Systems",
                "topics": [
                    "Introduction to Prototyping in UI/UX Design",
                    "Tools in Prototyping",
                    "Advanced Techniques for Prototyping"
                ]
            },
            {
                "module": "High Fidelity Prototyping",
                "topics": [
                    "High Fidelity Prototyping in Figma",
                    "Designs in High Fidelity",
                    "Conducting Usability Testing"
                ]
            },
            {
                "module": "Microinteractions and Animations",
                "topics": [
                    "Importance of Animation",
                    "Tools for Creating Animation",
                    "Vertical Scrolling",
                    "Horizontal Scrolling"
                ]
            },
            {
                "module": "Usability Testing",
                "topics": [
                    "Usability Testing Methods and Best Practices",
                    "Feedback Loops",
                    "Analyzing User Test Results",
                    "Iterative Designs based on Feedback"
                ]
            },
            {
                "module": "Collaboration Technique in Figma",
                "topics": [
                    "Advanced Collaboration Techniques in Figma",
                    "Sharing and Presenting Designs",
                    "Design Handoff to Developers",
                    "Case Study on Effective Design Systems"
                ]
            },
            {
                "module": "Collaborate with Teams",
                "topics": [
                    "Collaboration in Figma",
                    "Working with Teams",
                    "Work with Community",
                    "FigJam"
                ]
            },
            {
                "module": "Real-world UI/UX Projects",
                "topics": [
                    "Planning a UI/UX Project",
                    "Defining Project Goals and Objectives",
                    "Design for Different Platforms",
                    "Start a Real-world Project in Figma"
                ]
            },
            {
                "module": "Coding in UI/UX",
                "topics": [
                    "Convert Design to Coding",
                    "Adobe XD",
                    "Difference between Adobe XD and Figma",
                    "Tips for Presenting Design Works"
                ]
            },
            {
                "module": "Final Project and Presentation",
                "topics": [
                    "Finalizing the UI/UX Project",
                    "Creating a Project Presentation",
                    "Practice Presentation and Feedback",
                    "Final Project Presentation",
                    "Interview Preparation",
                    "Final Assessment",
                    "Course Certification"
                ]
            }
        ],
        "instructors": [
            {"name": "Franklin", "title": "Trainer - UI/UX Design", "experience": "4+ years"}
        ],
        "schedule": {
            "weekdays": "Mon - Sat 07:15 AM to 05:30 PM",
            "weekends": "Sunday Closed",
            "duration": "3 months"
        }
    }
]

from django.core.files import File

print("Seeding database with courses...")
created_count = 0
for idx, data in enumerate(courses_data, start=1):
    course, created = Course.objects.update_or_create(
        slug=data["slug"],
        defaults={
            "title": data["title"],
            "description": data["description"],
            "duration": data["duration"],
            "level": data["level"],
            "rating": data["rating"],
            "highlights": data["highlights"],
            "category": data["category"],
            "overview": data["overview"],
            "prerequisites": data["prerequisites"],
            "outcomes": data["outcomes"],
            "syllabus": data["syllabus"],
            "instructors": data["instructors"],
            "schedule": data["schedule"],
            "order": idx
        }
    )
    
    # Open local file and save via Django's File wrapper to trigger upload to active storage (e.g. Cloudinary)
    image_filename = os.path.basename(data["image"])
    local_image_path = dest_courses_dir / image_filename
    if local_image_path.exists():
        with open(local_image_path, 'rb') as f:
            course.image.save(image_filename, File(f), save=True)
        print(f"Saved image for course: {course.title}")
    else:
        course.image = data["image"]
        course.save()

    if created:
        created_count += 1
        print(f"Created Course: {course.title}")
    else:
        print(f"Updated Course: {course.title}")

print(f"Done! Seeded/Updated {len(courses_data)} courses in the database (created {created_count} new).")
