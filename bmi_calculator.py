import pandas as pd
import numpy as np
import os
import re

def parse_height_to_inches(height_str):
    """Parse height string like 5' 10" into total inches"""
    try:
        match = re.match(r"(\d+)'\s*(\d+)", str(height_str).strip())
        if match:
            feet = int(match.group(1))
            inches = int(match.group(2))
            return feet * 12 + inches
        return None
    except:
        return None

def parse_weight_to_lbs(weight_str):
    """Extract numeric weight value in lbs"""
    try:
        weight = re.findall(r'\d+', str(weight_str))
        if weight:
            return float(weight[0])
        return None
    except:
        return None

def calculate_bmi(height_inches, weight_lbs):
    """Calculate BMI from height (inches) and weight (lbs)"""
    if height_inches and weight_lbs and height_inches > 0:
        bmi = (weight_lbs / (height_inches ** 2)) * 703
        return round(bmi, 2)
    return None

def categorize_bmi(bmi):
    """Categorize BMI into standard categories"""
    if bmi is None:
        return "Unknown"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obesity"

def process_dataset(input_csv, output_csv):
    print("Loading dataset...")
    df = pd.read_csv(input_csv)
    print(f"Original dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}\n")

    # ✅ Split combined Height & Weight column
    if 'Height & Weight' not in df.columns:
        print("Error: 'Height & Weight' column not found in dataset.")
        return

    df[['Height', 'Weight']] = df['Height & Weight'].str.extract(r"(\d+'\s*\d+\")\s*(\d+\s*lbs\.?)")

    # ✅ Parse numeric values
    df['height_inches'] = df['Height'].apply(parse_height_to_inches)
    df['weight_lbs'] = df['Weight'].apply(parse_weight_to_lbs)

    # ✅ Calculate BMI & Category
    df['BMI'] = df.apply(lambda row: calculate_bmi(row['height_inches'], row['weight_lbs']), axis=1)
    df['Category'] = df['BMI'].apply(categorize_bmi)

    # ✅ Ensure output directory exists
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    # ✅ Save output
    df.to_csv(output_csv, index=False)
    print(f"\nSaved processed dataset to: {output_csv}")

    # ✅ Show sample output
    print("\nSample results:")
    print(df[['Height', 'Weight', 'BMI', 'Category']].head())

    return df


if __name__ == "__main__":
    INPUT_CSV = os.path.join("height-weight-images", "versions", "1", "Output_data.csv")
    OUTPUT_CSV = os.path.join("data", "height_weight_bmi_processed.csv")

    if not os.path.exists(INPUT_CSV):
        print(f"Error: Input file '{INPUT_CSV}' not found!")
    else:
        df = process_dataset(INPUT_CSV, OUTPUT_CSV)
        print("\nProcessing complete!")
