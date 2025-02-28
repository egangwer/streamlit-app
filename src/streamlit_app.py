import streamlit as st
import pandas as pd
import random
from joblib import load

museum_dat = load("path/to/museum_dat_with_extra.joblib")
kmeans_model = load("path/to/kmeans.joblib") 

st.title('Museum Artwork Topic Modeling')

def recommend_artworks(title, df, kmeans_model):
    artwork = df[df['Title'].str.lower() == title.lower()]
    if artwork.empty:
        return "Artwork not found. Try again."
    cluster_label = artwork['Cluster'].values[0] 
    similar_artworks = df[df['Cluster'] == cluster_label] 
    similar_artworks['Artist_Clean'] = similar_artworks['Artist_Clean'].str.title()
    return similar_artworks[['Title', 'Artist_Clean', 'Year', 'Medium', 'Link', 'Museum', 'Artwork_Text']].sample(1)

def find_artist(artist, df):
    artist = df[df['Artist_Clean'].str.lower() == artist.lower()]
    if artist.empty:
        return "Artist not found. Try again."
    artist_df = df[df['Artist_Clean'] == artist['Artist_Clean'].values[0]]
    artist_df['Artist_Clean'] = artist_df['Artist_Clean'].str.title()
    return artist_df[['Artist_Clean', 'Title', 'Year', 'Medium', 'Link']].drop_duplicates()

search_type = st.selectbox("I want to...", ["Find Similar Artworks", "Find an Artist"])

if search_type == "Find Similar Artworks":
    user_input = st.text_input('Enter an artwork here:')
    if st.button("Recommend similar artworks"):
        results = recommend_artworks(user_input, museum_dat, kmeans_model)
        if isinstance(results, str):
            st.warning(results)
        else:
            st.subheader(f"Artwork similar to '{user_input}':")
            row = results.iloc[0]  
            if pd.notna(row["Link"]):
                st.image(row["Link"], width=300)  
                st.markdown(f" **{row['Title']}** by {row['Artist_Clean']} is currently in the **{row['Museum']} Museum Collection**.")
                st.caption(f"{row['Artwork_Text']}")
            else: 
                st.warning("Image not found. Refresh for new picks")
                st.write(f"**{row['Title']}** by **{row['Artist_Clean']}** was created in {row['Year']} and is made of {row['Medium']}. Currently is in the **{row['Museum']} Museum Collection**.")
                st.caption(f"'{row['Artwork_Text']}'")
else: 
    user_input = st.text_input('Enter an artist here:')
    if st.button("Find artist"):
        results = find_artist(user_input, museum_dat)
        if isinstance(results, str):
            st.warning(results)
        else:
            st.subheader("Artist Information:")
            st.dataframe(results)

st.subheader("Random Artworks:")
random_artworks = museum_dat.sample(4, random_state=random.randint(1, 12000))  
cols = st.columns(4)

for idx, (col, row) in enumerate(zip(cols, random_artworks.iterrows())):
    with col:
        if pd.notna(row[1]["Link"]):
            st.image(row[1]["Link"], width=120) 
            st.caption(f"**{row[1]['Title']}**\n_{row[1]['Artist']}, {row[1]['Year']}_")
        else: 
            st.warning("Image not found. Refresh for new picks!")

if st.button("Refresh Artworks"):
    st.rerun()

st.write("Data is from the Cleveland Art Museum, Museum of Modern Art in New York, Art Institute of Chicago, and the Harvard Art Museum artwork collections.")
st.write("The data was accessed through API's and web scraping.")