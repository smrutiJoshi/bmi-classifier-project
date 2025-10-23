# BMI Calculator & Classifier - Machine Learning Project

A Python project to process height-weight data from Kaggle, calculate BMI, and classify individuals into health categories.

## 📋 Project Overview

This project:
1. Loads height and weight data from Kaggle dataset
2. Calculates BMI (Body Mass Index) for each record
3. Classifies individuals into BMI categories:
   - **Underweight**: BMI < 18.5
   - **Normal weight**: BMI 18.5 - 24.9
   - **Overweight**: BMI 25.0 - 29.9
   - **Obesity**: BMI ≥ 30.0

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download this project**
   ```bash
   mkdir bmi_classifier_project
   cd bmi_classifier_project
   ```

2. **Download the Kaggle dataset**
   
   **Option A: Using Kaggle CLI (Recommended)**
   ```bash
   # Install Kaggle CLI
   pip install kaggle
   
   # Setup Kaggle API credentials
   # 1. Go to https://www.kaggle.com/settings
   # 2. Click "Create New API Token" - this downloads kaggle.json
   # 3. Place kaggle.json in ~/.kaggle/ (Linux/Mac) or C:\Users\<YourUsername>\.kaggle\ (Windows)
   
   # Download the dataset
   kaggle datasets download -d virenbr11/height-weight-images
   
   # Unzip the dataset
   unzip height-weight-images.zip
   ```
   
   **Option B: Manual Download**
   - Go to https://www.kaggle.com/datasets/virenbr11/height-weight-images
   - Click the "Download" button
   - Extract the ZIP file to your project directory

3. **Install required Python packages**
   ```bash
   pip install pandas numpy
   ```

4. **Verify your setup**
   
   Make sure you have the CSV file from the dataset. It should be named something like:
   - `height_weight_data.csv` or
   - `data.csv` or similar
   
   Update the `INPUT_CSV` variable in `bmi_calculator.py` with your actual CSV filename.

## 📂 Project Structure

```
bmi_classifier_project/
│
├── bmi_calculator.py          # Main processing script
├── README.md                  # This file
├── requirements.txt           # Python dependencies
│
├── height_weight_data.csv     # Input CSV (from Kaggle)
├── height_weight_bmi_processed.csv  # Output CSV (generated)
│
└── images/                    # Image folder (from Kaggle dataset)
```

## ▶️ Running the Project

1. **Update the input filename** (if needed)
   
   Open `bmi_calculator.py` and update this line:
   ```python
   INPUT_CSV = "height_weight_data.csv"  # Change to your CSV filename
   ```

2. **Run the script**
   ```bash
   python bmi_calculator.py
   ```

3. **Check the output**
   
   The script will:
   - Display statistics about the dataset
   - Show BMI distribution
   - Show category distribution
   - Save the processed data to `height_weight_bmi_processed.csv`

## 📊 Output Format

The processed CSV will contain all original columns plus:
- **BMI**: Calculated Body Mass Index
- **Category**: BMI classification (Underweight, Normal weight, Overweight, Obesity)

## 🧮 BMI Calculation

The script uses the standard BMI formula for imperial units:

```
BMI = (weight in pounds / (height in inches)²) × 703
```

Height is converted from feet-inches format (e.g., "5'10\"") to total inches.

## 🔍 Example Output

```
BMI STATISTICS
==================================================
Total records: 500
Valid BMI calculations: 498

BMI Statistics:
count    498.000000
mean      24.567890
std        4.234567
min       15.200000
25%       21.450000
50%       24.100000
75%       27.800000
max       38.900000

CATEGORY DISTRIBUTION
==================================================
Normal weight    245
Overweight       156
Obesity           67
Underweight       30
```

## 🛠️ Troubleshooting

**Issue: "Input file not found"**
- Make sure you've downloaded and extracted the Kaggle dataset
- Verify the CSV filename matches the `INPUT_CSV` variable
- Check that the CSV is in the same directory as the script

**Issue: "Could not find height and weight columns"**
- The script automatically detects columns with "height" and "weight" in their names
- If detection fails, check your CSV column names and update the script accordingly

**Issue: "No BMI values calculated"**
- Check if the height/weight data format matches the expected format (e.g., "5'10\"" for height, "150 lbs" for weight)
- The script includes parsing functions that can be adjusted for different formats

## 📈 Future Enhancements

Potential improvements for this project:
- Add visualization (BMI distribution charts, category pie charts)
- Train a machine learning model to predict BMI from images
- Add gender-specific BMI categories
- Include age-adjusted BMI calculations
- Web interface for easy data upload and processing

## 📝 License

This is an educational project. The dataset is from Kaggle and follows its respective license.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!