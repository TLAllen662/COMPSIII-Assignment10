# Import pandas
import pandas as pd

# Read the CSV file
df = pd.read_csv('streaming_data.csv')

# Add completion rate calculation
completion_rate = df['completion_rate'].mean()

# Calculate total listening time in seconds
total_time = df['listening_time'].sum()

# Convert to minutes and hours for easier reading
total_minutes = total_time / 60
total_hours = total_time / 3600

# Get top 5 most listened to artists
top_artists = df['artist'].value_counts().head(5)

# Get top 5 most listened to songs
top_songs = df['song_title'].value_counts().head(5)

# Get top 5 most listened to genres
top_genres = df['genre'].value_counts().head(5)
