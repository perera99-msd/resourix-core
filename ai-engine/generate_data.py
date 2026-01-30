import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Configuration
NUM_SAMPLES = 1000
OUTPUT_FILE = "data/synthetic_waste_data.csv"

# Real Sri Lankan Industrial Zones (for Contextual Realism)
LOCATIONS = [
    "Katunayake Export Processing Zone", 
    "Biyagama Export Processing Zone",
    "Koggala Export Processing Zone",
    "Seethawaka Export Processing Zone",
    "Horana Export Processing Zone",
    "Colombo Industrial Zone",
    "Ekala Industrial Estate",
    "Paliyagoda"
]

# Waste Categories with realistic price ranges (LKR per kg)
CATEGORIES = {
    "Textile Offcuts - Cotton": (50, 150),
    "Textile Offcuts - Polyester": (30, 90),
    "Textile Offcuts - Mixed": (20, 60),
    "Plastic - PET Bottles": (80, 130),
    "Plastic - HDPE Containers": (90, 140),
    "Plastic - LDPE Wrap": (70, 120),
    "Paper - Cardboard": (30, 60),
    "Paper - Mixed": (15, 40),
    "Metal - Steel Scraps": (150, 250),
    "Metal - Aluminum Cans": (300, 450),
    "Chemical - Empty Drums (Plastic)": (500, 800), # Per Unit
    "Organic - Food Waste": (5, 15)
}

def generate_waste_data(num_samples):
    data = []
    print(f"🏭 Generating {num_samples} industrial waste records...")
    
    for _ in range(num_samples):
        # 1. Pick a random category
        full_category = random.choice(list(CATEGORIES.keys()))
        category, sub_category = full_category.split(" - ")
        min_price, max_price = CATEGORIES[full_category]
        
        # 2. Generate realistic attributes
        weight_kg = round(random.uniform(50, 2000), 2)  # Between 50kg and 2 tons
        location = random.choice(LOCATIONS)
        
        # 3. Simulate "Market Demand" (Hidden AI Feature)
        # Random demand index: 0.8 (Low) to 1.2 (High)
        demand_index = random.uniform(0.8, 1.2) 
        
        # 4. Calculate "Fair Market Price" (Target Variable for AI)
        base_price = random.uniform(min_price, max_price)
        final_price_per_unit = round(base_price * demand_index, 2)
        total_value = round(final_price_per_unit * weight_kg, 2)
        
        # 5. Generate a "Vague" Description (For NLP Matching)
        # Factory owners write bad descriptions. We simulate that.
        adjectives = ["Mixed", "Clean", "Dirty", "Sorted", "Unsorted", "Baled", "Loose", "Leftover"]
        desc = f"{random.choice(adjectives)} {sub_category} available at {location.split(' ')[0]} factory."

        item = {
            "waste_id": fake.uuid4(),
            "date_listed": fake.date_between(start_date='-6m', end_date='today'),
            "category": category,
            "sub_category": sub_category,
            "description": desc,
            "location": location,
            "quantity_kg": weight_kg,
            "unit": "kg" if "Drums" not in sub_category else "units",
            "demand_index": round(demand_index, 2), # Feature for training
            "price_per_unit_lkr": final_price_per_unit, # Label for training
            "total_value_lkr": total_value,
            "status": random.choice(["Available", "Available", "Available", "Sold"]) # Mostly available
        }
        data.append(item)
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Ensure data folder exists
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df = generate_waste_data(NUM_SAMPLES)
    df.to_csv(OUTPUT_FILE, index=False)
    
    print(f"\n✅ SUCCESS! Generated {NUM_SAMPLES} rows.")
    print(f"📁 File saved to: {OUTPUT_FILE}")
    print("\n📊 First 5 rows:")
    print(df.head())
