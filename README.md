

# 🎬 JustWatch Scraper Analytics 📊

This project involves scraping data from JustWatch, cleaning and processing it, and then analyzing various aspects of movies and TV shows. The data includes information such as titles, release years, IMDb ratings, streaming service availability, and more.

## 📂 Project Structure

The project is organized into two main directories:

- **TV_shows_data**: Contains files related to scraping, cleaning, and analyzing TV show data.
  - 📝 `Data_filtering_analysis.ipynb`: Jupyter Notebook containing data filtering and analysis for TV shows.
  - 📄 `Tvshows_data.csv`: Original dataset scraped from JustWatch for TV shows.
  - 🐍 `Web_scrapping_tvshow.py`: Python script for web scraping TV show data from JustWatch.
  - 🧹 `cleaned_tvshow_data.csv`: Cleaned dataset for TV shows after data processing.

- **movies_data**: Contains files related to scraping, cleaning, and analyzing movie data.
  - 📝 `Data_filtering_analysis.ipynb`: Jupyter Notebook containing data filtering and analysis for movies.
  - 🐍 `Web_scrapping_movies.py`: Python script for web scraping movie data from JustWatch.
  - 🧹 `cleaned_movie_data.csv`: Cleaned dataset for movies after data processing.
  - 📄 `movie_data.csv`: Original dataset scraped from JustWatch for movies.

## 📊 Data Overview

- **TV Shows Data**: The dataset contains 135 entries of TV shows scraped from JustWatch. Data cleaning addressed missing IMDb ratings (12) and streaming service values (60), along with 15 duplicate rows.
- **Movies Data**: The dataset includes 970 entries of movies scraped from JustWatch. Data cleaning resolved missing IMDb ratings (32) and streaming service values (151), with no duplicate rows found.

## 🔍 Data Filtering

- Included only TV shows and movies released in the last two years with IMDb ratings of 7 or higher.

## 📈 Data Analysis

- **TV Shows Analysis**: Calculated the average IMDb rating for TV shows (6.9) and identified the top 5 TV shows with the highest IMDb ratings.
- **Movies Analysis**: Calculated the average IMDb rating for movies (7.5) and identified the top 5 movies with the highest IMDb ratings. Determined the streaming service with the most significant number of offerings and explored the distribution of movie releases over the years.

## 💡 Insights

- The analysis provides insights into TV show and movie ratings, streaming services, and release trends, which can be valuable for stakeholders in the entertainment industry.

