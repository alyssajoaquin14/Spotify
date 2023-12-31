import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.header("Spotify Top Streamed Songs 2023")
data = pd.read_csv("spotify-2023.csv", encoding='ISO-8859-1')
data.info()
st.dataframe(data, use_container_width=True)
# top artists with most songs
top_artists = data['artist(s)_name'].value_counts().head(10)

fig = plt.figure(figsize=(12, 6))
sns.barplot(x = top_artists.values, y = top_artists.index, palette = "viridis")
plt.xlabel('Number of Songs')
plt.ylabel('Artist(s) Name')
plt.title('Top 10 Artists with Most Songs')
st.pyplot(fig)

#top 10 songs with most streams
top_spotify_streams = data[['track_name', 'artist(s)_name', 'streams']].sort_values(by='streams', ascending=False).head(10)
fig2 = plt.figure(figsize=(12, 6))
sns.barplot(x = top_spotify_streams['streams'], y = top_spotify_streams['track_name'], palette= 'viridis')
plt.xlabel('Streams (in billions)')
plt.ylabel('Song Name')
plt.title('Top 10 Songs with Most Streams on Spotify')
st.pyplot(fig2)
