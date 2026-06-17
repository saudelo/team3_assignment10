import matplotlib.pyplot as plt
import pandas as pd

INPUT_FILE = "skill_retention_by_hours.csv"

df = pd.read_csv(INPUT_FILE)

# freshman = df[df["Year_of_Study"] == "Freshman"]
# sophomore = df[df["Year_of_Study"] == "Sophomore"]
# junior = df[df["Year_of_Study"] == "Junior"]
# senior = df[df["Year_of_Study"] == "Senior"]
# graduate = df[df["Year_of_Study"] == "Graduate"]


# fresh = df[df["Year_of_Study"] == "Freshman"].groupby(df["Weekly_hours_bracket"])["Skill_Retention_Score"].mean()
# soph = df[df["Year_of_Study"] == "Sophomore"].groupby(df["Weekly_hours_bracket"])["Skill_Retention_Score"].mean()
# junior = df[df["Year_of_Study"] == "Junior"].groupby(df["Weekly_hours_bracket"])["Skill_Retention_Score"].mean()
# senior = df[df["Year_of_Study"] == "Senior"].groupby(df["Weekly_hours_bracket"])["Skill_Retention_Score"].mean()
# graduate = df[df["Year_of_Study"] == "Graduate"].groupby(df["Weekly_hours_bracket"])["Skill_Retention_Score"].mean()


year_pivot = df.pivot_table(
    values="Skill_Retention_Score",
    index="Weekly_hours_bracket",
    columns="Year_of_Study",
    aggfunc="mean",
    fill_value=0,
)

post_GPA_pivot = df.pivot_table(
    values="Skill_Retention_Score",
    index="Weekly_hours_bracket",
    columns="Post_Semester_GPA_bracket",
    aggfunc="mean",
    fill_value=0,
    margins=True,
    margins_name="Average Total"
)
fig, (ax1, ax2)= plt.subplots(2, 1, figsize=(10,8))
fig.suptitle("Skill Retention Score by Hours AI Used")


year_pivot.plot(kind="line", ax=ax1)
ax1.set_title("Year of Study")
ax1.set_xlabel("Weekly Hours of Use")
ax1.set_ylabel("Skill Retention Score")


post_GPA_pivot.plot(kind="line", ax=ax2)
ax2.set_title("GPA")
ax2.set_xlabel("Weekly Hours of Use")
ax2.set_ylabel("Skill Retention Score")

plt.tight_layout()
plt.show()