import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Spotify Dashboard", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stMetric {
        background-color: #1DB954;
        padding: 15px;
        border-radius: 10px;
        color: black;
        text-align: center;
    }
    h1, h2, h3 {
        color: #1DB954;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🎧 Spotify Data Dashboard")
st.markdown("### Analyze songs, artists, and streaming trends")


df = pd.read_csv("C:\\Users\\Suganya\\Desktop\\SEM II\\Python\\Unit_5\\spotify.csv")


st.sidebar.title("🎛 Filter Panel")
search = st.sidebar.text_input("🔍 Search Artist")

if search:
    df = df[df['Artist'].str.contains(search, case=False)]


col1, col2, col3 = st.columns(3)

col1.metric("🎵 Total Songs", len(df))
col2.metric("👀 Total Views", int(df['Views'].sum()))
col3.metric("▶️ Total Streams", int(df['Stream'].sum()))

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Top Artists by Views")
    top_artists = df.groupby('Artist')['Views'].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_artists)

with col2:
    st.subheader("🎵 Top Tracks by Streams")
    top_tracks = df.sort_values(by='Stream', ascending=False).head(10)
    st.bar_chart(top_tracks.set_index('Track')['Stream'])

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Views Distribution")
    fig, ax = plt.subplots()
    ax.hist(df['Views'], bins=20)
    st.pyplot(fig)

with col2:
    st.subheader("❤️ Likes vs Views")
    fig2, ax2 = plt.subplots()
    ax2.scatter(df['Views'], df['Likes'])
    ax2.set_xlabel("Views")
    ax2.set_ylabel("Likes")
    st.pyplot(fig2)

st.markdown("---")

st.subheader("🎤 Artist Details")

artist = st.selectbox("Select Artist", df['Artist'].unique())
artist_df = df[df['Artist'] == artist]

st.dataframe(artist_df[['Track', 'Views', 'Likes', 'Stream']])