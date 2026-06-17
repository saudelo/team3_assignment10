import pandas as pd

DATA_FILE = "data/cleaned_data.csv"
OUTPUT_FILE = "data/skill_retention_by_hours.csv"

border_80 = "="*80+"\n"
GPA_bins = [0, 1, 2, 3, 4]
GPA_labels = ["0-1", "1-2", "2-3", "3-4"]
hour_bins = [0, 5, 10, 15, 20, 25, 30, 35, 40]
hour_labels = ["0-5", "05-10", "10-15", "15-20", "20-25", "25-30", "30-35", "35-40"]
year_order = ["Freshman", "Sophomore", "Junior", "Senior", "Graduate"]

df = pd.read_csv(DATA_FILE)

print(df.info())
print(df.describe())

df["Weekly_hours_bracket"] = pd.cut(df["Weekly_GenAI_Hours"], bins=hour_bins, labels=hour_labels)
df["Pre_Semester_GPA_bracket"] = pd.cut(df["Pre_Semester_GPA"], bins=GPA_bins, labels=GPA_labels)
df["Post_Semester_GPA_bracket"] = pd.cut(df["Post_Semester_GPA"], bins=GPA_bins, labels=GPA_labels)
df["GPA_diff"] = df["Pre_Semester_GPA"] - df["Post_Semester_GPA"].shift(fill_value=0)

year_subset = df[["Year_of_Study", "Weekly_GenAI_Hours", "Skill_Retention_Score", "Weekly_hours_bracket"]]
pre_GPA_subset = df[["Pre_Semester_GPA", "Pre_Semester_GPA_bracket", "Weekly_GenAI_Hours", "Skill_Retention_Score", "Weekly_hours_bracket"]]
post_GPA_subset = df[["Post_Semester_GPA", "Post_Semester_GPA_bracket", "Weekly_GenAI_Hours", "Skill_Retention_Score", "Weekly_hours_bracket"]]
subset = df[["Post_Semester_GPA_bracket", "Pre_Semester_GPA_bracket", "Skill_Retention_Score", "Weekly_hours_bracket", "GPA_diff", "Year_of_Study"]]

# print(df["Post_Semester_GPA"].max())

print(df.info())
print(year_subset.info())

year_pivot = year_subset.pivot_table(
    values="Skill_Retention_Score",
    index="Weekly_hours_bracket",
    columns="Year_of_Study",
    aggfunc="mean",
    fill_value=0,
    margins=True,
    margins_name="Average Total"
)

pre_GPA_pivot = pre_GPA_subset.pivot_table(
    values="Skill_Retention_Score",
    index="Weekly_hours_bracket",
    columns="Pre_Semester_GPA_bracket",
    aggfunc="mean",
    fill_value=0,
    margins=True,
    margins_name="Average Total"
)

post_GPA_pivot = post_GPA_subset.pivot_table(
    values="Skill_Retention_Score",
    index="Weekly_hours_bracket",
    columns="Post_Semester_GPA_bracket",
    aggfunc="mean",
    fill_value=0,
    margins=True,
    margins_name="Average Total"
)

year_pivot = year_pivot.reindex(year_order, axis=1, fill_value=0.0).round(2)
pre_GPA_pivot = pre_GPA_pivot.reindex(GPA_labels, axis=1, fill_value=0.0).round(2)
post_GPA_pivot = post_GPA_pivot.reindex(GPA_labels, axis=1, fill_value=0.0).round(2)

print(year_pivot)
print(pre_GPA_pivot)
print(post_GPA_pivot)

subset.to_csv(OUTPUT_FILE)