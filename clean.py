"""
Outputs: cleaned_data.csv
"""

import pandas as pd



# Step 1: Load the dataset
df = pd.read_csv("ai_student_impact_dataset (1).csv")

print("=" * 60)
print("Step 1: Raw data overview")
print("=" * 60)

print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics (numeric columns):")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())

print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Step 2: Check for issues, only fix what's actually there

print("\n" + "=" * 60)
print("Step 2: Checking for issues")
print("=" * 60)

issues_found = False

# Check for missing values
missing_total = df.isnull().sum().sum()
if missing_total > 0:
    print(f"Found {missing_total} missing values. Dropping rows with missing data.")
    before = len(df)
    df = df.dropna()
    print(f"Dropped {before - len(df)} rows.")
    issues_found = True
else:
    print("No missing values found.")

# Check for duplicates
dupe_count = df.duplicated().sum()
if dupe_count > 0:
    print(f"Found {dupe_count} duplicate rows. Removing them.")
    df = df.drop_duplicates()
    issues_found = True
else:
    print("No duplicate rows found.")

# Check for inconsistent casing/whitespace in string columns
string_cols = df.select_dtypes(include="str").columns
messy_cols = []
for col in string_cols:
    if df[col].str.strip().ne(df[col]).any() or (df[col] != df[col].str.lower()).any():
        messy_cols.append(col)

if messy_cols:
    print(f"Found inconsistent casing or whitespace in: {messy_cols}. Standardizing.")
    for col in messy_cols:
        df[col] = df[col].str.strip().str.lower()
    issues_found = True
else:
    print("No casing or whitespace issues found in string columns.")

if not issues_found:
    print("\nDataset came in clean - no fixes were needed.")

print(f"\nFinal dataset shape: {df.shape[0]} rows x {df.shape[1]} columns")

# Step 3: Save cleaned data for everyone to use

df.to_csv("cleaned_data.csv", index=False)
print("\nSaved to cleaned_data.csv")