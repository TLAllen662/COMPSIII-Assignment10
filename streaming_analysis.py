# Import pandas
import pandas as pd
import matplotlib.pyplot as plt
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
total_time = df['duration_seconds'].sum()

# Convert to minutes and hours for easier reading
total_minutes = total_time / 60
total_hours = total_time / 3600

# Get top 5 most listened to artists
top_artists = df['artist'].value_counts().head(5)

# Get top 5 most listened to songs
top_songs = df['song'].value_counts().head(5)

# Get top 5 most listened to genres
top_genres = df['genre'].value_counts().head(5)

# Calculate songs listened to by day
days = df['day_of_week'].value_counts().sort_index()

# Calculate songs listened to by month
month = df['month'].value_counts().sort_index()

# Print Year in Music Summary
print("Your Year in Music Summary:")
print(f"Average Completion Rate: {completion_rate:.4f}")
print(f"Total Listening Time (seconds): {total_time}")
print(f"Total Listening Time (minutes): {total_minutes:.2f}")
print(f"Total Listening Time (hours): {total_hours:.2f}")
print()

print("Top Artists:")
print(top_artists)
print()

print("Top Songs:")
print(top_songs)
print()

print("Top Genres:")
print(top_genres)
print()

print("Songs by Day of Week:")
print(days)
print()

print("Songs by Month:")
print(month)
print()

# Create visualizations

# 1. Bar chart of songs listened by day of the week
plt.figure(figsize=(10, 6))
plt.bar(days.index, days.values)
plt.title('Songs Listened to by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Songs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('songs_by_day.png')
plt.show()

# 2. Line chart of songs listened by month
plt.figure(figsize=(12, 6))
plt.plot(month.index, month.values, marker='o', linewidth=2, markersize=6)
plt.title('Songs Listened to by Month')
plt.xlabel('Month')
plt.ylabel('Number of Songs')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('songs_by_month.png')
plt.show()

# 3. Histogram of duration_seconds
plt.figure(figsize=(10, 6))
plt.hist(df['duration_seconds'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribution of Song Duration')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('duration_histogram.png')
plt.show()


