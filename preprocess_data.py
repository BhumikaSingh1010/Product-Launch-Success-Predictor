
import pandas as pd
from pathlib import Path

# Find the dataset relative to this Python file
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "social_media_viral_content_2000_sample.csv"

# Load the dataset
df = pd.read_csv(DATA_PATH)

# Inspect the dataset
print("Dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nTarget distribution:")
print(df["is_viral"].value_counts(dropna=False))
