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
    file_name = "data/cleaned_data.csv"
    filepath = os.path.join(file_name)
    clean_df = pd.read_csv(filepath)
    print("File loaded successfully!")
       

    #Ai usage in correlation to self-reported anxiety

    #plot  Anxiety level during exams and institutional_Policy with amount of AI use

    #Burnout risk    Burnout_Risk_Level Anxiety_Level_During_Exams  Post_Semester_GPA Institutional_Policy
    #Weekly_GenAI_Hours Traditional_Study_Hours Perceived_AI_Dependency
    rows_1,columns_1= clean_df.shape  

    print(f"rows {rows_1}")  
    print(f"columns {columns_1}")  

    anx_df =clean_df[["Weekly_GenAI_Hours","Traditional_Study_Hours", "Perceived_AI_Dependency","Burnout_Risk_Level","Anxiety_Level_During_Exams","Institutional_Policy"]].copy()
    anx_df = anx_df.sort_values(by="Anxiety_Level_During_Exams", ascending=False) #More exploring
  

    print(anx_df[[
    "Traditional_Study_Hours",
    "Weekly_GenAI_Hours",
    "Anxiety_Level_During_Exams"
    ]].corr(numeric_only=True))


    
    print(anx_df[[
    "Perceived_AI_Dependency",
    "Weekly_GenAI_Hours",
    "Anxiety_Level_During_Exams"
    ]].corr(numeric_only=True))


    
    #"Weekly_GenAI_Hours"    #"Anxiety_Level_During_Exams"
    fig,ax = plt.subplots()
    m, c = np.polyfit(anx_df["Weekly_GenAI_Hours"], anx_df["Anxiety_Level_During_Exams"], deg=1)
    x_line = np.linspace(anx_df["Weekly_GenAI_Hours"].min(), anx_df["Weekly_GenAI_Hours"].max(), 100)
    ax.plot(x_line, m * x_line + c, color="red", linestyle="--", label="Trend")
    ax.scatter(anx_df["Weekly_GenAI_Hours"], anx_df["Anxiety_Level_During_Exams"])
    ax.set_title("AI Study Hours Effect on Anxiety Level During Exams")
    ax.set_xlabel("Weekly_GenAI_Hours")
    ax.set_ylabel("Anxiety_Level_During_Exams")
    plot_filepath1 = os.path.join("graphs/anxiety_data_ai_hours.png")
    plt.savefig(plot_filepath1, dpi=150, bbox_inches="tight")
    plt.show()

    #"Institutional_Policy", ""Anxiety_Level_During_Exams"
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(anx_df["Institutional_Policy"], bins=7, edgecolor="white")
    ax.set_title("Sum of Anxiety_Level by Institutional Policy (Histogram)")
    ax.set_xlabel("Institutional Policy")
    ax.set_ylabel("Sum of Anxiety_Levels")
    plt.tight_layout()
    plot_filepath2 = os.path.join("graphs/anxiety_institutional_policy.png")
    plt.savefig(plot_filepath2, dpi=150, bbox_inches="tight")
    plt.show()
    
    to_filepath = os.path.join("data/anxiety_data.csv")
    anx_df.to_csv(to_filepath, index = False)

    plt.close()

except FileNotFoundError as e:
    print(e)
except Exception as exc:
    print(exc)






