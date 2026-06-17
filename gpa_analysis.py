"""
Question: How does AI usage correlate with GPA change?
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Load the cleaned dataset

df = pd.read_csv("cleaned_data.csv")

# Step 1: Process and analyze

print("=" * 60)
print("Step 1: Processing and analysis")
print("=" * 60)

# Derived column: GPA change = GPA after AI - GPA before AI
df["gpa_change"] = df["Post_Semester_GPA"] - df["Pre_Semester_GPA"]
print("\nAdded column 'gpa_change' (Post_Semester_GPA - Pre_Semester_GPA).")

# Bucket Weekly_GenAI_Hours into usage tiers so we can group by them
df["ai_usage_tier"] = pd.cut(
    df["Weekly_GenAI_Hours"],
    bins=[0, 2, 6, 12, 40],
    labels=["low (0-2h)", "moderate (2-6h)", "high (6-12h)", "very high (12h+)"],
    include_lowest=True,
)
print("Added column 'ai_usage_tier' bucketing Weekly_GenAI_Hours into 4 groups.")

# Group by usage tier and get average GPA change per group
gpa_by_usage = (
    df.groupby("ai_usage_tier", observed=True)["gpa_change"]
    .mean()
    .reset_index()
    .rename(columns={"gpa_change": "avg_gpa_change"})
)

print("\nAverage GPA change by AI usage tier:")
print(gpa_by_usage.to_string(index=False))

# What percentage of students in each group actually improved?
df["gpa_improved"] = df["gpa_change"] > 0
improvement_rate = (
    df.groupby("ai_usage_tier", observed=True)["gpa_improved"]
    .mean()
    .reset_index()
    .rename(columns={"gpa_improved": "pct_improved"})
)
improvement_rate["pct_improved"] = improvement_rate["pct_improved"] * 100
print("\n% of students who improved GPA by AI usage tier:")
print(improvement_rate.to_string(index=False))


# Step 2: Visualizations

print("\n" + "-" * 60)
print("Step 2: Generating visualizations")
print("-" * 60)



# Chart 1: Average GPA change by AI usage frequency
fig, ax = plt.subplots(figsize=(9, 5))

colors = ["#4caf50" if v >= 0 else "#f44336" for v in gpa_by_usage["avg_gpa_change"]]
bars = ax.bar(
    gpa_by_usage["ai_usage_tier"],
    gpa_by_usage["avg_gpa_change"],
    color=colors,
    edgecolor="white",
    linewidth=0.8,
)

for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.001,
        f"{height:+.3f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )

ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_title("Average GPA Change by Weekly AI Usage", fontsize=13, fontweight="bold")
ax.set_xlabel("Weekly AI Usage (hours)", fontsize=11)
ax.set_ylabel("Average GPA Change", fontsize=11)
ax.tick_params(axis="x", rotation=15)
plt.tight_layout()
plt.savefig("chart1_avg_gpa_change_by_usage.png", dpi=150)
plt.show()
print("Saved: chart1_avg_gpa_change_by_usage.png")




# Chart 2: Distribution of GPA change across all students
fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(df["gpa_change"], bins=30, color="#5c85d6", edgecolor="white", linewidth=0.6)
ax.axvline(df["gpa_change"].mean(), color="red", linestyle="--", linewidth=1.5,
           label=f"Mean = {df['gpa_change'].mean():.3f}")

ax.set_title("Distribution of GPA Change Across All Students", fontsize=13, fontweight="bold")
ax.set_xlabel("GPA Change (After - Before)", fontsize=11)
ax.set_ylabel("Number of Students", fontsize=11)
ax.legend()
plt.tight_layout()
plt.savefig("chart2_gpa_change_distribution.png", dpi=150)
plt.show()
print("Saved: chart2_gpa_change_distribution.png")



# Chart 3: Percentage of students who improved GPA, by AI usage frequency
fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    improvement_rate["ai_usage_tier"],
    improvement_rate["pct_improved"],
    color="#9c6fd6",
    edgecolor="white",
    linewidth=0.8,
)

ax.axhline(50, color="gray", linestyle="--", linewidth=1, label="50% baseline")
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.set_title("% of Students Whose GPA Improved, by Weekly AI Usage",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Weekly AI Usage (hours)", fontsize=11)
ax.set_ylabel("% of students who improved GPA", fontsize=11)
ax.tick_params(axis="x", rotation=15)
ax.legend()
plt.tight_layout()
plt.savefig("chart3_pct_improved_by_usage.png", dpi=150)
plt.show()
print("Saved: chart3_pct_improved_by_usage.png")

print("\nDone. 3 charts saved as png files.")