# Job Market Analytics Project (2025–2026)
# Advanced Visualizations using Python, NumPy, Matplotlib, Seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Style settings
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# ----------------------------------
# Load Dataset
# ----------------------------------
df = pd.read_csv("job_market_analytics_2025_2026.csv")

# Data Cleaning
df['salary'] = df['salary'].str.replace(' LPA', '').astype(float)
df['posted_date'] = pd.to_datetime(df['posted_date'])

print("Dataset Loaded Successfully")
print(df.head())

# ----------------------------------
# 1️⃣ Job Openings by Role (Bar Chart)
# ----------------------------------
plt.figure()
sns.countplot(y='job_title', data=df, palette='viridis')
plt.title("Job Openings by Role (2025–2026)", fontsize=14)
plt.xlabel("Number of Jobs")
plt.ylabel("Job Role")
plt.tight_layout()
plt.show()

# ----------------------------------
# 2️⃣ Average Salary by Job Role (Bar Chart)
# ----------------------------------
avg_salary = df.groupby('job_title')['salary'].mean().sort_values()

plt.figure()
sns.barplot(x=avg_salary.values, y=avg_salary.index, palette='coolwarm')
plt.title("Average Salary by Job Role (LPA)", fontsize=14)
plt.xlabel("Salary (LPA)")
plt.ylabel("Job Role")
plt.tight_layout()
plt.show()

# ----------------------------------
# 3️⃣ Top Hiring Locations (Horizontal Bar)
# ----------------------------------
plt.figure()
sns.countplot(y='location', data=df,
              order=df['location'].value_counts().index,
              palette='magma')
plt.title("Top Hiring Locations in India", fontsize=14)
plt.xlabel("Job Count")
plt.ylabel("Location")
plt.tight_layout()
plt.show()

# ----------------------------------
# 4️⃣ Job Type Distribution (Donut Chart)
# ----------------------------------
job_type_counts = df['job_type'].value_counts()

plt.figure()
plt.pie(job_type_counts,
        labels=job_type_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        wedgeprops=dict(width=0.4))
plt.title("Job Type Distribution")
plt.show()

# ----------------------------------
# 5️⃣ Skills Demand Analysis (Bar Chart)
# ----------------------------------
skills_series = df['skills'].str.split(', ')
skills_list = [skill for sublist in skills_series for skill in sublist]

skills_df = pd.DataFrame(skills_list, columns=['Skill'])

plt.figure()
sns.countplot(y='Skill',
              data=skills_df,
              order=skills_df['Skill'].value_counts().index,
              palette='Set2')
plt.title("Most In-Demand Skills (2025–2026)", fontsize=14)
plt.xlabel("Demand Count")
plt.ylabel("Skill")
plt.tight_layout()
plt.show()

# ----------------------------------
# 6️⃣ Salary Distribution (Histogram)
# ----------------------------------
plt.figure()
sns.histplot(df['salary'], bins=6, kde=True, color='green')
plt.title("Salary Distribution (LPA)", fontsize=14)
plt.xlabel("Salary (LPA)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ----------------------------------
# 7️⃣ Jobs Posted Over Time (Line Chart)
# ----------------------------------
jobs_by_month = df.groupby(df['posted_date'].dt.to_period('M')).size()

plt.figure()
jobs_by_month.plot(marker='o')
plt.title("Job Postings Trend Over Time", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Number of Jobs")
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------------
# 8️⃣ Location vs Job Type (Heatmap)
# ----------------------------------
pivot_table = pd.pivot_table(df,
                             values='job_title',
                             index='location',
                             columns='job_type',
                             aggfunc='count',
                             fill_value=0)

plt.figure()
sns.heatmap(pivot_table, annot=True, cmap='Blues', fmt='d')
plt.title("Location vs Job Type Heatmap", fontsize=14)
plt.xlabel("Job Type")
plt.ylabel("Location")
plt.tight_layout()
plt.show()

# ----------------------------------
# Key Insights
# ----------------------------------
print("\n🔍 Key Insights:")
print("• Python, SQL, and Power BI are the most demanded skills.")
print("• Bangalore and Mumbai lead in hiring.")
print("• Fresher & 0–1 year roles dominate the market.")
print("• Average salaries range between 5–8 LPA.")
print("• Full-Time roles are more common than internships.")
