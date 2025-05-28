# covid_globaltrack

📝 COVID-19 Global Data Tracker
Project Description
This project involves building a data analysis and reporting notebook (or app) that tracks global COVID-19 trends. You'll analyze cases, deaths, recoveries, and vaccinations across countries and time periods. The project covers:

Cleaning and processing real-world COVID-19 data

Performing exploratory data analysis (EDA)

Generating insights through statistical analysis

Visualizing trends using Python data tools

The final deliverable will be a comprehensive data analysis report with visualizations and narrative insights, suitable for presentation or publishing.

🚩 Objectives
Import and clean COVID-19 global data

Analyze time trends (cases, deaths, vaccinations)

Compare metrics across countries/regions

Visualize trends with charts and maps

Communicate findings in a Jupyter Notebook or PDF report

🗂️ Project Steps
1️⃣ Data Collection
Goal: Obtain reliable COVID-19 datasets

Recommended Data Sources:

Our World in Data COVID-19 Dataset (CSV & API)

Johns Hopkins University GitHub Repository

Action Items:

Download owid-covid-data.csv from Our World in Data

Save the file in your project working directory

Note: Our World in Data CSV is recommended for beginners

2️⃣ Data Loading & Exploration
Goal: Load the dataset and understand its structure

Tasks:

python
# Load data
import pandas as pd
df = pd.read_csv('owid-covid-data.csv')

# Explore data
df.columns
df.head()
df.isnull().sum()
Key Columns to Note:

date, location, total_cases, total_deaths

new_cases, new_deaths, total_vaccinations

3️⃣ Data Cleaning
Goal: Prepare data for analysis

Tasks:

Filter countries of interest (e.g., Kenya, USA, India)

Drop rows with missing dates/critical values

Convert date column to datetime: pd.to_datetime()

Handle missing numeric values with fillna() or interpolate()

4️⃣ Exploratory Data Analysis (EDA)
Goal: Generate descriptive statistics and explore trends

Analysis Tasks:

Plot total cases over time for selected countries

Plot total deaths over time

Compare daily new cases between countries

Calculate death rate: total_deaths / total_cases

Visualizations:

Line charts (cases & deaths over time)

Bar charts (top countries by total cases)

Heatmaps (optional for correlation analysis)

Tools:

matplotlib

seaborn

5️⃣ Visualizing Vaccination Progress
Goal: Analyze vaccination rollouts

Tasks:

Plot cumulative vaccinations over time

Compare % vaccinated population across countries

Visualizations:

Line charts

Optional pie charts for vaccinated vs. unvaccinated

6️⃣ Optional: Choropleth Map
Goal: Visualize cases/vaccination rates geographically

Tasks:

Prepare dataframe with iso_code and total_cases for latest date

Plot choropleth showing case density or vaccination rates

Tools:

Plotly Express

geopandas (advanced)

7️⃣ Insights & Reporting
Goal: Summarize findings and create final report

Tasks:

Write 3-5 key insights from the data

Highlight anomalies or interesting patterns

Use Markdown cells in Jupyter Notebook for narrative

Final Deliverables:

Well-documented Jupyter Notebook containing:

Code

Visualizations

Narrative explanations

Optional exports:

Notebook → PDF

PowerPoint with screenshots

Required Tools/Packages
Python 3.x

pandas

matplotlib

seaborn

(Optional) plotly, geopandas

