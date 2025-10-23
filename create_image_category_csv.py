import pandas as pd

# Load the processed CSV
df = pd.read_csv('data/height_weight_bmi_processed.csv')

# Select only the required columns
df_new = df[['Filename', 'Category']]

# Save to a new CSV
df_new.to_csv('data/image_category.csv', index=False)

print("CSV with Filename and Category created at data/image_category.csv")