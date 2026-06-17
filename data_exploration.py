import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os
# Color pallete used to standardize color for all visualizations
PALETTE = [
    "#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
    "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC",
    "#86BCB6", "#D4A6C8",
]
# Accent color
ACCENT = "#4E79A7"
# Background color
BG      = "#F8F9FA"
# Grid color
GRID    = "#E0E0E0"

try:
   #load file
    file_name = "ai_student_impact_dataset.csv"
    filepath = os.path.join(file_name)
    df = pd.read_csv(filepath)
    print("File loaded successfully!")
       


    #exploration
    rows_1,columns_1= df.shape  

    print(f"rows {rows_1}")  
    print(f"columns {columns_1}")  

    #clean_data
 
    #No rows with missing data
    clean_df = df.dropna()
    rows_2,columns_2= clean_df.shape  

    print(f"rows {rows_2}")  
    print(f"columns {columns_2}") 


    
    #All ids are unique
    clean_df.drop_duplicates(subset='Student_ID')
    rows_3,cols_3 = clean_df.shape
    print(f"rows {rows_3}")  
    print(f"columns {cols_3}") 

    #MORE EXPLORATION

    #In case it's relvant, data frames by Major
    #Major: STEM
    stem_mask = clean_df["Major_Category"].str.strip().str.upper() == "STEM"
    stem_df= clean_df[stem_mask]
    r,c = stem_df.shape
    print(f"rows {r}")  
    print(f"columns {c}") 

    #Major: Humanities
    stem_mask = clean_df["Major_Category"].str.strip() == "Humanities"
    stem_df= clean_df[stem_mask]
    r,c = stem_df.shape
    print(f"rows {r}")  
    print(f"columns {c}") 

    #Major: Medical
    med_mask = clean_df["Major_Category"].str.strip() == "Medical"
    med_df= clean_df[med_mask]
    r,c = med_df.shape
    print(f"rows {r}")  
    print(f"columns {c}") 

    #Major: Arts
    arts_mask = clean_df["Major_Category"].str.strip()== "Arts"
    arts_df= clean_df[arts_mask]
    r,c = arts_df.shape
    print(f"rows {r}")  
    print(f"columns {c}") 

    #Major: Business
    biz_mask = clean_df["Major_Category"].str.strip() == "Business"
    biz_df= clean_df[biz_mask]
    r,c = biz_df.shape
    print(f"rows {r}")  
    print(f"columns {c}") 



  
    to_filepath = os.path.join("clean_data.csv")
    #stem_df.to_csv(to_filepath, index = False)

except FileNotFoundError as e:
    print(e)
except Exception as exc:
    print(exc)






