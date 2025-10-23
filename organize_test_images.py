import os
import shutil
import pandas as pd

# Paths
SRC_IMG_DIR = r'height-weight-images/versions/1'
CSV_PATH = 'data/image_category.csv'
TEST_DIR = 'data/test'

# Read CSV
df = pd.read_csv(CSV_PATH)

# Create category folders if not exist
categories = df['Category'].unique()
for cat in categories:
    os.makedirs(os.path.join(TEST_DIR, cat), exist_ok=True)

# Copy images to category folders
for _, row in df.iterrows():
    fname = row['Filename']
    cat = row['Category']
    src_path = os.path.join(SRC_IMG_DIR, fname)
    dst_path = os.path.join(TEST_DIR, cat, fname)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
    else:
        print(f"Image not found: {src_path}")

print("Images copied to test folders by category.")
