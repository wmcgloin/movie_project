import pandas as pd

# Load the CSV file into a DataFrame
file_path = './data/clean_data/movie_level_data.csv'  # Adjust path as necessary
data = pd.read_csv(file_path)

# Extract relevant columns and simplify genres to the primary genre
data['primaryGenre'] = data['genres'].str.split(',').str[0]  # Select the first genre listed

# Group by year and primary genre, then calculate the average rating
yearly_genre_ratings = data.groupby(['startYear', 'primaryGenre']).agg(AverageRating=('averageRating', 'mean')).reset_index()

# Convert years and ratings to the appropriate formats
yearly_genre_ratings['startYear'] = yearly_genre_ratings['startYear'].astype(int)
yearly_genre_ratings['AverageRating'] = yearly_genre_ratings['AverageRating'].round(1)

# Format data as a list of dictionaries to match the desired JSON structure
result_json = yearly_genre_ratings.rename(columns={'startYear': 'Year', 'primaryGenre': 'Genre'}).to_dict(orient='records')

# Save the data to a JSON file
json_file_path = 'movies_by_year_and_genre.json'
# Correction: Convert DataFrame to JSON string first then write to file
with open(json_file_path, 'w') as f:
    pd.DataFrame(result_json).to_json(f, orient='records', lines=False)

json_file_path
