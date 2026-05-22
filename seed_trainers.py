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

from api.models import Trainer

# Define the source and destination paths for images
src_trainers_dir = BASE_DIR.parent / 'frontend' / 'public' / 'Trainers'
dest_trainers_dir = BASE_DIR / 'media' / 'Trainers'

# Copy images to backend media folder
print("Copying trainer photos from public/Trainers to backend/media/Trainers...")
if src_trainers_dir.exists():
    os.makedirs(dest_trainers_dir, exist_ok=True)
    # List files case-insensitively or exactly as they are in the directory
    for file_name in os.listdir(src_trainers_dir):
        src_file = src_trainers_dir / file_name
        dest_file = dest_trainers_dir / file_name
        if src_file.is_file() and not dest_file.exists():
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {file_name}")
else:
    print(f"Warning: Source folder {src_trainers_dir} not found!")

# Data to seed
trainers_data = [
    {
        "name": "Liji Basil",
        "course": "Technical Head",
        "image": "Trainers/Liji.jpg",
    },
    {
        "name": "Antony Bright",
        "course": "Cyber Security Analyst",
        "image": "Trainers/antony.jpeg",
    },
    {
        "name": "Arjun Sabu",
        "course": "System Administrator",
        "image": "Trainers/Arjun Sabu.jpg",
    },
    {
        "name": "Noel George",
        "course": "Network Engineer - Cisco",
        "image": "Trainers/noel.jpg",
    },
    {
        "name": "Abhijith A",
        "course": "VAPT Analyst",
        "image": "Trainers/abhijith.jpg",
    },
    {
        "name": "John Kuriakose",
        "course": "Digital Marketing Manager",
        "image": "Trainers/johns.jpg",
    },
    {
        "name": "Robin Shiji",
        "course": "Software Developer-Python",
        "image": "Trainers/robin.jpg",
    },
    {
        "name": "Sudheesh .S",
        "course": "Junior System Administrator",
        "image": "Trainers/sudheesh.jpg",
    },
    {
        "name": "Vimal S",
        "course": "Junior System Administrator",
        "image": "Trainers/vimal.jpg",
    },
    {
        "name": "Akshay P R",
        "course": "Junior System Administrator",
        "image": "Trainers/akshay.jpg",
    },
    {
        "name": "Anexa Thomas",
        "course": "Data Science",
        "image": "Trainers/anexa.jpg",
    },
    {
        "name": "Theresa Thomas",
        "course": "System Administrator",
        "image": "Trainers/theresa.png",
    },
    {
        "name": "Aleena Paul",
        "course": "Junior System Administrator",
        "image": "Trainers/aleena.jpg",
    },
    {
        "name": "Sreeja Rajendran",
        "course": "Placement Manager/Head-Logistics",
        "image": "Trainers/sreeja.jpg",
    },
]

print("Seeding database with trainers...")
created_count = 0
for idx, data in enumerate(trainers_data, start=1):
    trainer, created = Trainer.objects.update_or_create(
        name=data["name"],
        defaults={
            "course": data["course"],
            "image": data["image"],
            "order": idx
        }
    )
    if created:
        created_count += 1

print(f"Done! Seeded {created_count} new trainers (total database records: {Trainer.objects.count()}).")
