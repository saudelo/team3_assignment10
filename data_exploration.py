import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ======LOAD DATA======
df = pd.read_csv('ai_student_impact_dataset.csv')


# ======INSPECT DATA======
print("Shape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())



# ======CLEAN DATA======

#Drop duplicates
df = df.drop_duplicates()

#Drop missing values
df = df.dropna()

#Clean presemester/post semester gpa (round 2 decmials)
df['Pre_Semester_GPA'] = df['Pre_Semester_GPA'].round(2)
df['Post_Semester_GPA'] = df['Post_Semester_GPA'].round(2)

#Clean names with underscores and replace with spaces
df.columns = df.columns.str.replace('_', ' ')
df['Institutional Policy'] = df['Institutional Policy'].str.replace('_', ' ')

print()
print(df.head())    
print()

# ======PROCESS DATA======

#GPA CHANGE
df['GPA Change'] = (
    df['Post Semester GPA']
    - df['Pre Semester GPA']
)
#YEAR OF STUDY
year_gpa = (
    df.groupby('Year of Study')['GPA Change']
      .mean()
      .sort_values(ascending=False)
)

print(year_gpa)
print()

#AI SKILL
ai_skill_gpa = (
    df.groupby('Prompt Engineering Skill')['GPA Change']
      .mean()
)


print(ai_skill_gpa)
print()

#YEAR OF STUDY AND AI SKILL
year_and_skill = (
    df.groupby(['Year of Study', 'Prompt Engineering Skill'])['GPA Change']
      .mean()
)

print(year_and_skill)
print()

#BURNOUT RISK
burnout_ai = (
    df.groupby('Burnout Risk Level')['Weekly GenAI Hours'].mean() 
)

print(burnout_ai)
print()



# ======VISUALIZATION DATA======

# FIGURE 1 - AI Usage vs GPA Change
plt.figure(figsize=(8, 5))

plt.scatter(
    df['Weekly GenAI Hours'],
    df['GPA Change'],
)

plt.axhline(
    y=0,
    color='red',
    linestyle='--',
    linewidth=2,
    label='No GPA Change'
)

plt.title('AI Usage vs GPA Change')
plt.xlabel('Weekly AI Hours')
plt.ylabel('GPA Change')
plt.tight_layout

plt.show()

# Figure 2 - AVG GPA Change by Major
plt.figure(figsize=(8, 5), )
year_gpa.plot(kind='bar', color=['red','blue', 'yellow', 'green', 'orange'])
plt.title('Average GPA Change by Year of Study')
plt.xlabel('Year of Study')
plt.ylabel('Average GPA Change')
plt.tight_layout()
plt.show()

# Figure 3 - AI Skill vs GPA Change
plt.figure(figsize=(8, 5))
ai_skill_gpa.plot(kind='bar', color=['blue', 'yellow', 'green'])
plt.title('Average GPA Change by AI Skill')
plt.xlabel('AI Skill')
plt.ylabel('Average GPA Change')
plt.tight_layout()
plt.show()

# Figure 4 - Year of Study vs AI Skill
plt.figure(figsize=(8, 5))
year_and_skill.plot(kind='bar', color=['red','yellow', 'blue'])
plt.title('Average GPA Change by Year of Study and AI Skill')
plt.xlabel('Year of Study')
plt.ylabel('Average GPA Change')
plt.tight_layout()
plt.show()

# Figure 5 - Burnout Risk vs AI Usage
plt.figure(figsize=(8, 5))
burnout_ai.plot(kind='bar', color=['red', 'orange', 'green'])
plt.title('Average GPA Change by Burnout Risk')
plt.xlabel('Burnout Risk')
plt.ylabel('AI Usage Weekly')
plt.tight_layout()
plt.show()

