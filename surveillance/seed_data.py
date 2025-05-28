from django.utils import timezone
from surveillance.models import Grower, Plant, SurveillanceRecord

def seed_data():
    # Create Growers
    grower1 = Grower.objects.create(name="John Farmer", email="john@example.com", property_location="Darwin Farm")
    grower2 = Grower.objects.create(name="Jane Grower", email="jane@example.com", property_location="Katherine Orchard")

    # Create Plants
    plant1 = Plant.objects.create(grower=grower1, plant_type="Mango", location="Field A", planting_date="2024-01-15")
    plant2 = Plant.objects.create(grower=grower1, plant_type="Mango", location="Field B", planting_date="2024-02-10")
    plant3 = Plant.objects.create(grower=grower2, plant_type="Mango", location="Orchard 1", planting_date="2024-03-05")

    # Create Surveillance Records (10 records)
    records = [
        {"plant": plant1, "pest_or_disease": "Anthracnose", "plant_part": "leaves", "severity": "medium", "notes": "Spots on leaves"},
        {"plant": plant1, "pest_or_disease": "Fruit Fly", "plant_part": "fruit", "severity": "high", "notes": "Infestation detected"},
        {"plant": plant2, "pest_or_disease": "Powdery Mildew", "plant_part": "stem", "severity": "low", "notes": "Early stage"},
        {"plant": plant2, "pest_or_disease": "Aphids", "plant_part": "leaves", "severity": "medium", "notes": "Spraying required"},
        {"plant": plant3, "pest_or_disease": "Bacterial Canker", "plant_part": "stem", "severity": "high", "notes": "Urgent action needed"},
        {"plant": plant3, "pest_or_disease": "Mites", "plant_part": "leaves", "severity": "low", "notes": "Monitor closely"},
        {"plant": plant1, "pest_or_disease": "Fusarium Wilt", "plant_part": "roots", "severity": "medium", "notes": "Soil treatment needed"},
        {"plant": plant2, "pest_or_disease": "Scale Insects", "plant_part": "stem", "severity": "medium", "notes": "Insecticide needed"},
        {"plant": plant3, "pest_or_disease": "Sooty Mold", "plant_part": "leaves", "severity": "low", "notes": "Clean leaves"},
        {"plant": plant1, "pest_or_disease": "Whitefly", "plant_part": "leaves", "severity": "medium", "notes": "Sticky traps recommended"},
    ]

    # Insert Surveillance Records
    for record in records:
        SurveillanceRecord.objects.create(
            plant=record["plant"],
            surveillance_date=timezone.now(),
            pest_or_disease=record["pest_or_disease"],
            plant_part=record["plant_part"],
            severity=record["severity"],
            notes=record["notes"]
        )