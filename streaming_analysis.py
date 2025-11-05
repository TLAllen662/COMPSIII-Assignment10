# Import pandas
import pandas as pd

# Read the CSV file
df = pd.read_csv('streaming_data.csv')

# Add month and day ordering
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 

df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True) 
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True) 

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

# Calculate songs listened to by day
days = df['day'].value_counts().sort_index()

# Calculate songs listened to by month
month = df['month'].value_counts().sort_index()


