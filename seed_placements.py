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

from api.models import PlacedStudent

# Define the source and destination paths for images
src_placements_dir = BASE_DIR.parent / 'frontend' / 'public' / 'placements'
dest_placements_dir = BASE_DIR / 'media' / 'placements'

# Copy images to backend media folder
print("Copying student photos from public/placements to backend/media/placements...")
if src_placements_dir.exists():
    os.makedirs(dest_placements_dir, exist_ok=True)
    for file_name in os.listdir(src_placements_dir):
        src_file = src_placements_dir / file_name
        dest_file = dest_placements_dir / file_name
        if src_file.is_file() and not dest_file.exists():
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {file_name}")
else:
    print(f"Warning: Source folder {src_placements_dir} not found!")

# Data to seed
students_data = [
    {
        "name": "Abhirami G",
        "course": "Networking",
        "position": "Network Support Engineer",
        "image": "placements/WhatsApp Image 2026-04-21 at 3.53.40 PM.jpeg",
    },
    {
        "name": "Mahitha Mahesh",
        "course": "Networking",
        "position": "Network Service Engineer",
        "image": "placements/WhatsApp Image 2026-04-05 at 1.34.50 PM (1).jpeg",
    },
    {
        "name": "Rugma D",
        "course": "Networking",
        "position": "IT Support Engineer",
        "image": "placements/WhatsApp Image 2026-04-05 at 1.34.49 PM.jpeg",
    },
    {
        "name": "Rose Dhaleena Sajeev",
        "course": "Networking",
        "position": "Technical Support Engineer",
        "image": "placements/WhatsApp Image 2026-04-05 at 1.34.49 PM (2).jpeg",
    },
    {
        "name": "Steev Joseph",
        "course": "Networking",
        "position": "System Administrator",
        "image": "placements/WhatsApp Image 2026-04-21 at 3.53.41 PM.jpeg",
    },
    {
        "name": "SHIBIN M",
        "course": "Networking",
        "position": "Technical Support Engineer",
        "image": "placements/WhatsApp Image 2026-04-05 at 1.34.49 PM (1).jpeg",
    },
    {
        "name": "Mussamil Sainu",
        "course": "Networking",
        "position": "L1 Network Support",
        "image": "placements/Screenshot 2026-03-01 190642.png",
    },
    {
        "name": "Harikrishna Manoj",
        "course": "Python",
        "position": "Python Developer",
        "image": "placements/python.jpeg",
    },
    {
        "name": "Ashik Basheer",
        "course": "Networking",
        "position": "Network Support Engineer",
        "image": "placements/Screenshot 2026-02-06 110607.png",
    },
    {
        "name": "Ashwin K",
        "course": "Networking",
        "position": "Technical support engineer",
        "image": "placements/Screenshot 2026-02-06 110627.png",
    },
    {
        "name": "Arya Sree",
        "course": "Networking",
        "position": "Technical support engineer",
        "image": "placements/Screenshot 2026-02-06 110705.png",
    },
    {
        "name": "jinil job",
        "course": "Networking",
        "position": "Technical support engineer",
        "image": "placements/Screenshot 2026-02-06 110923.png",
    },
    {
        "name": "Megha Suku",
        "course": "Networking",
        "position": "Network Engineer",
        "image": "placements/Screenshot 2025-09-16 151450.png",
    },
    {
        "name": "Ribin A.K",
        "course": "Networking",
        "position": "L1 Network Engineer",
        "image": "placements/Screenshot 2025-09-16 151423.png",
    },
    {
        "name": "Adheena V.C",
        "course": "Networking",
        "position": "Network Associate",
        "image": "placements/Screenshot 2025-09-16 151508.png",
    },
    {
        "name": "Muhammed Farhan T",
        "course": "Networking",
        "position": "Technical Support",
        "image": "placements/Screenshot 2025-09-16 151439.png",
    },
    {
        "name": "Thazkiya Sherin",
        "course": "Networking",
        "position": "Technical Executive",
        "image": "placements/IMG-20250820-WA0015.jpg",
    },
    {
        "name": "Akhil Raj",
        "course": "Networking",
        "position": "Network Engineer",
        "image": "placements/IMG-20250820-WA0016.jpg",
    },
    {
        "name": "Antony Joby",
        "course": "Networking",
        "position": "Network Support Engineer",
        "image": "placements/IMG-20250820-WA0017.jpg",
    },
    {
        "name": "Akshay K",
        "course": "Networking",
        "position": "L1 Engineer",
        "image": "placements/IMG-20250820-WA0018.jpg",
    },
    {
        "name": "Vishnu E",
        "course": "Networking",
        "position": "Network Engineer",
        "image": "placements/IMG-20250820-WA0019.jpg",
    },
    {
        "name": "Amal Shibu",
        "course": "Networking",
        "position": "L1 Network Engineer",
        "image": "placements/IMG-20250820-WA0020.jpg",
    },
    {
        "name": "Nithin Joy",
        "course": "Networking",
        "position": "Network Support Engineer",
        "image": "placements/Screenshot 2025-09-22 155339.png",
    },
]

print("Seeding database with placed students...")
created_count = 0
for idx, data in enumerate(students_data, start=1):
    # Use update_or_create to avoid duplicate seeding
    student, created = PlacedStudent.objects.update_or_create(
        name=data["name"],
        defaults={
            "course": data["course"],
            "position": data["position"],
            "image": data["image"],
            "order": idx
        }
    )
    if created:
        created_count += 1

print(f"Done! Seeded {created_count} new student placements (total database records: {PlacedStudent.objects.count()}).")
