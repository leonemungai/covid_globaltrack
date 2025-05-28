import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Set style for visualizations
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

## 2️⃣ Data Loading & Exploration
def load_and_explore_data(df = pd.read_csv('C:/Users/user/Desktop/plp docs/python/Week eight project/owid-covid-data.csv')):
    """Load and explore the dataset"""
    print("Loading and exploring data...")
    
    # Load data
    df = pd.read_csv('C:/Users/user/Desktop/plp docs/python/Week eight project/owid-covid-data.csv')
    
    # Basic exploration
    print("\n=== Dataset Info ===")
    print(f"Shape: {df.shape}")
    print("\nColumns:")
    print(df.columns)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nMissing values:")
    print(df.isnull().sum())
    
    return df

def clean_data(df, countries_of_interest):
    """Clean and prepare the data"""
    print("\nCleaning data...")
    
    # 1. First ensure proper datetime handling and sorting
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['location', 'date'])  # Critical for time-based operations
    
    # 2. Filter countries after sorting
    df = df[df['location'].isin(countries_of_interest)].copy()
    
    # 3. Drop rows with missing critical values
    critical_cols = ['date', 'location', 'total_cases', 'total_deaths']
    df = df.dropna(subset=critical_cols)
    
    # 4. Handle missing numeric values with proper time-aware interpolation
    numeric_cols = ['new_cases', 'new_deaths', 'total_vaccinations']
    for col in numeric_cols:
        if col in df.columns:
            # Create temporary DatetimeIndex for interpolation
            temp_df = df.set_index('date').groupby('location')[col]
            df[col] = temp_df.transform(
                lambda x: x.interpolate(method='time')).values
    
    print("\nAfter cleaning:")
    print(f"Shape: {df.shape}")
    print("Missing values in key columns:")
    print(df[critical_cols + numeric_cols].isnull().sum())
    
    return df

## 4️⃣ Exploratory Data Analysis (EDA)
def perform_eda(df):
    """Perform exploratory data analysis"""
    print("\nPerforming EDA...")
    
    # Calculate death rate
    df['death_rate'] = df['total_deaths'] / df['total_cases']
    
    # Plot total cases over time
    plt.figure()
    sns.lineplot(data=df, x='date', y='total_cases', hue='location')
    plt.title('Total COVID-19 Cases Over Time')
    plt.ylabel('Total Cases')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Plot total deaths over time
    plt.figure()
    sns.lineplot(data=df, x='date', y='total_deaths', hue='location')
    plt.title('Total COVID-19 Deaths Over Time')
    plt.ylabel('Total Deaths')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Plot daily new cases comparison
    plt.figure()
    sns.lineplot(data=df, x='date', y='new_cases', hue='location')
    plt.title('Daily New COVID-19 Cases')
    plt.ylabel('New Cases')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Plot death rate over time
    plt.figure()
    sns.lineplot(data=df, x='date', y='death_rate', hue='location')
    plt.title('COVID-19 Death Rate Over Time')
    plt.ylabel('Death Rate (Deaths/Cases)')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Bar chart of latest total cases by country
    latest_data = df.sort_values('date').groupby('location').last().reset_index()
    plt.figure()
    sns.barplot(data=latest_data, x='location', y='total_cases')
    plt.title('Latest Total COVID-19 Cases by Country')
    plt.ylabel('Total Cases')
    plt.xlabel('Country')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return df

## 5️⃣ Visualizing Vaccination Progress
def analyze_vaccinations(df):
    """Analyze vaccination progress"""
    print("\nAnalyzing vaccination progress...")
    
    if 'total_vaccinations' not in df.columns:
        print("Vaccination data not available in this dataset")
        return df
    
    # Plot cumulative vaccinations
    plt.figure()
    sns.lineplot(data=df, x='date', y='total_vaccinations', hue='location')
    plt.title('Total COVID-19 Vaccinations Over Time')
    plt.ylabel('Total Vaccinations')
    plt.xlabel('Date')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Calculate and plot vaccination rate per hundred
    if 'people_vaccinated_per_hundred' in df.columns:
        plt.figure()
        sns.lineplot(data=df, x='date', y='people_vaccinated_per_hundred', hue='location')
        plt.title('COVID-19 Vaccination Rate (per 100 people)')
        plt.ylabel('Vaccinated per 100 people')
        plt.xlabel('Date')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    return df

## 6️⃣ Optional: Build a Choropleth Map
def create_choropleth(df):
    """Create a choropleth map of cases or vaccinations"""
    print("\nCreating choropleth map...")
    
    # Get latest data for each country
    latest_data = df.sort_values('date').groupby('location').last().reset_index()
    
    # Check if ISO codes are available
    if 'iso_code' not in latest_data.columns:
        print("ISO codes not available - cannot create choropleth")
        return
    
    # Create choropleth for total cases
    fig = px.choropleth(latest_data,
                        locations="iso_code",
                        color="total_cases",
                        hover_name="location",
                        hover_data=["total_cases", "total_deaths"],
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="World Map of Total COVID-19 Cases")
    fig.show()
    
    # Create choropleth for vaccination if data exists
    if 'people_vaccinated_per_hundred' in latest_data.columns:
        fig = px.choropleth(latest_data,
                            locations="iso_code",
                            color="people_vaccinated_per_hundred",
                            hover_name="location",
                            hover_data=["total_vaccinations"],
                            color_continuous_scale=px.colors.sequential.Viridis,
                            title="World Map of COVID-19 Vaccination Rates (per 100 people)")
        fig.show()

## Main Execution
if __name__ == "__main__":
    # Configuration
    DATA_FILE = 'C:/Users/user/Desktop/plp docs/python/Week eight project/owid-covid-data.csv'
    COUNTRIES_OF_INTEREST = ['Kenya', 'United States', 'India']
    
    # Run pipeline
    df = load_and_explore_data(DATA_FILE)
    df = clean_data(df, COUNTRIES_OF_INTEREST)
    df = perform_eda(df)
    df = analyze_vaccinations(df)
    create_choropleth(df)