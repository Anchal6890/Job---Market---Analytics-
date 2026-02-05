## 📊 Job Market Insights & Analytics

## 🎯 Project Overview
This project provides a comprehensive analysis of the Data Analyst job market using Python. By scraping and processing job posting data, I’ve uncovered key trends regarding in-demand skills, top hiring companies, and geographic demand across India. This tool is designed to help freshers and analysts align their skill sets with current market requirements.

---

## 🛠️ The Technical Stack
* **Data Processing:** `Pandas`, `NumPy`
* **Visualization:** `Seaborn`, `Matplotlib`
* **Analysis Type:** Exploratory Data Analysis (EDA) & Time-Series Trend Analysis
* 

## 🚀 How to Use
1. **Clone the repo:** `git clone https://github.com/Anchal6890/Job-Market-Analytics.git`
2. **Install dependencies:** `pip install pandas seaborn matplotlib`
3. **Run the Notebook:** Open `Job market analysis.ipynb` in your preferred IDE.

---

## 🏗️ Core Engineering Highlights

### 🔹 Advanced Skill Extraction
Standard data cleaning wasn't enough for this dataset. The `skills` column contained nested strings. I implemented a parsing logic to **explode** these lists into individual data points, allowing for an accurate frequency count of technical requirements.
> **Result:** Identified SQL (126) and Tableau (117) as the primary market requirements.

### 🔹 Geographic Demand Mapping
By aggregating job counts by location, the analysis reveals a clear concentration of roles in Pune and Hyderabad, providing a roadmap for candidates targeting Tier-1 tech hubs.

### 🔹 Experience Level Normalization
To bridge the gap between categorical labels (like "Junior" or "0-1 Years") and numerical analysis, I utilized **Category Encoding**. This allowed for a more structured look at how companies gate-keep roles based on seniority.

---

## 📊 Business & Market Insights
* **Role Dominance:** Analytical roles (Reporting & Business Analytics) comprise over 40% of the current hiring volume.
* **Platform Efficiency:** Naukri (35.2%) and Indeed (33.2%) are the most effective sources for data-centric job hunting.
* **Hiring Giants:** Enterprise firms like **Cognizant, Accenture, and PwC** show a consistent hiring pattern for early-career professionals.

---

## 💻 Implementation Guide
To replicate this analysis:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Anchal6890/Job-Market-Analytics.git](https://github.com/Anchal6890/Job-Market-Analytics.git)
   
