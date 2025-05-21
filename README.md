# Anime Recommendation System

## Project Overview
This machine learning project provides anime recommendations based on content similarity analysis of anime synopses. The system uses TF-IDF vectorization and cosine similarity to suggest similar titles from a dataset of over 16,000 anime entries.

## Features
- Content-based recommendation engine
- Streamlit web interface
- Dataset containing anime metadata and synopses
- Precomputed similarity matrix for fast recommendations

## Installation
```bash
pip install pandas numpy scikit-learn streamlit
```

## Usage
1. Start the web interface:
```bash
streamlit run app.py
```
2. Select an anime from the dropdown
3. View top 5 recommendations

## Dataset
- Source: anime_with_synopsis.csv
- Contains:
  - MAL_ID
  - Title
  - Genres
  - Synopsis

## Model Files
- `Anime_list.pkl`: Processed anime metadata
- `similarity.pkl`: Precomputed similarity matrix

## Algorithm
Uses TF-IDF vectorization on anime synopses combined with cosine similarity to find nearest neighbors. The model processes text using:
- Stemming
- Stopword removal
- TF-IDF weighting

## Dependencies
- Python 3.8+
- pandas
- numpy
- scikit-learn
- Streamlit

## Acknowledgments
Dataset sourced from MyAnimeList.net API
