import streamlit as st
import requests
import numpy as np
import pandas as pd

# Load Thrones API data
api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()

# Load pickle safely for new pandas versions
df = pd.read_pickle("data.pkl")

# Limit to first 25 rows
df = df.head(25).reset_index(drop=True)

# Replace character names (dictionary-based)
df['character'] = df['character'].replace({
    'Jaime': 'Jamie',
    'Lord Varys': 'Varys',
    'Bronn': 'Lord Bronn',
    'Sandor Clegane': 'The Hound',
    'Robb Stark': 'Rob Stark'
})

# Function to fetch image URL (robust matching)
def fetch_image(name, api_data):
    # Exact match first
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']
    # Partial match
    for item in api_data:
        if name.lower() in item['fullName'].lower():
            return item['imageUrl']
    return None

# Streamlit UI
st.title("Game Of Thrones Personality Matcher")

characters = df['character'].tolist()
selected_character = st.selectbox("Select a character", characters)

# Find closest character match
character_id = df.index[df['character'] == selected_character][0]
x = df[['x', 'y']].to_numpy()

distances = np.linalg.norm(x - x[character_id], axis=1)
recommended_id = np.argsort(distances)[1]
recommended_character = df.iloc[recommended_id]['character']

# Fetch images
image_url = fetch_image(selected_character, api_data)
recommended_character_image_url = fetch_image(recommended_character, api_data)

# Display results
col1, col2 = st.columns(2)

with col1:
    st.header(selected_character)
    if image_url:
        st.image(image_url)
    else:
        st.write("No image found")

with col2:
    st.header(recommended_character)
    if recommended_character_image_url:
        st.image(recommended_character_image_url)
    else:
        st.write("No image found")
