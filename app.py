
# import streamlit as st
# import pandas as pd
# import plotly.express as px


# # ==========================================
# # PAGE CONFIGURATION
# # ==========================================

# st.set_page_config(
#     page_title="Spotify Data Dashboard",
#     page_icon="🎧",
#     layout="wide"
# )


# # ==========================================
# # CUSTOM CSS
# # ==========================================

# st.markdown("""
# <style>

# .main {
#     background-color: #0E1117;
#     color: white;
# }

# .stMetric {
#     background-color: #1DB954;
#     padding: 15px;
#     border-radius: 10px;
#     color: black;
#     text-align: center;
# }

# h1, h2, h3 {
#     color: #1DB954;
# }

# /* ---- Sidebar quick-navigation buttons ---- */
# .nav-button {
#     display: block;
#     width: 100%;
#     padding: 10px 14px;
#     margin-bottom: 8px;
#     background-color: #1DB954;
#     color: black !important;
#     font-weight: 600;
#     text-align: left;
#     text-decoration: none !important;
#     border-radius: 8px;
#     transition: background-color 0.15s ease-in-out;
# }

# .nav-button:hover {
#     background-color: #17a34a;
# }

# </style>
# """, unsafe_allow_html=True)


# # ==========================================
# # TITLE
# # ==========================================

# st.title("🎧 Spotify Data Dashboard")

# st.markdown(
#     "### Analyze songs, artists, views, likes, and streaming trends"
# )


# # ==========================================
# # LOAD DATASET
# # ==========================================

# df = pd.read_csv("spotify.csv")


# # ==========================================
# # SIDEBAR FILTER
# # ==========================================

# st.sidebar.title("🎛 Filter Panel")

# search = st.sidebar.text_input(
#     "🔍 Search Artist"
# )


# # Artist Search Filter
# if search:

#     df = df[
#         df["Artist"].str.contains(
#             search,
#             case=False,
#             na=False
#         )
#     ]


# # ==========================================
# # SIDEBAR QUICK NAVIGATION
# # (click any button -> page scrolls to that section)
# # ==========================================

# st.sidebar.markdown("---")
# st.sidebar.markdown("### 📌 Quick Navigation")

# nav_items = {
#     "📊 Overview / KPIs": "overview",
#     "🔥 Top Artists by Views": "top-artists-views",
#     "🎵 Top Tracks by Streams": "top-tracks-streams",
#     "🎤 Top Artists by Song Count": "top-artists-songs",
#     "❤️ Likes vs Views": "likes-views",
#     "🎭 Mood Analysis": "mood-analysis",
#     "💎 Hidden Gems": "hidden-gems",
#     "🎚️ Audio Feature Correlation": "audio-features",
#     "💿 Album Type Comparison": "album-type",
#     "📱 Platform Split": "platform-split",
#     "🎤 Artist Details": "artist-details",
# }

# nav_html = ""
# for label, anchor in nav_items.items():
#     nav_html += f'<a class="nav-button" href="#{anchor}">{label}</a>'

# st.sidebar.markdown(nav_html, unsafe_allow_html=True)


# # ==========================================
# # KPI SECTION
# # ==========================================

# st.markdown("<div id='overview'></div>", unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)


# col1.metric(
#     "🎵 Total Songs",
#     len(df)
# )


# col2.metric(
#     "👀 Total Views",
#     f"{int(df['Views'].sum()):,}"
# )


# col3.metric(
#     "▶️ Total Streams",
#     f"{int(df['Stream'].sum()):,}"
# )


# st.markdown("---")


# # ==========================================
# # TOP ARTISTS BY VIEWS
# # ==========================================

# st.markdown("<div id='top-artists-views'></div>", unsafe_allow_html=True)

# col1, col2 = st.columns(2)

# with col1:

#     st.subheader("🔥 Top Artists by Views")

#     top_artists = (
#         df.groupby(
#             "Artist",
#             as_index=False
#         )["Views"]
#         .sum()
#         .sort_values(
#             "Views",
#             ascending=False
#         )
#         .head(10)
#         .reset_index(drop=True)
#     )

#     # Create bar position
#     top_artists["Rank"] = range(1, len(top_artists) + 1)

#     fig1 = px.bar(
#         top_artists,
#         x="Rank",
#         y="Views",
#         color="Artist",
#         hover_data={
#             "Artist": True,
#             "Views": ":,",
#             "Rank": False
#         },
#         title="Top 10 Artists by Views"
#     )

#     fig1.update_layout(
#         showlegend=False,
#         xaxis_title=None,
#         yaxis_title="Views",
#         xaxis=dict(
#             showticklabels=False
#         )
#     )

#     st.plotly_chart(
#         fig1,
#         use_container_width=True
#     )

# # ==========================================
# # TOP TRACKS BY STREAMS
# # ==========================================

# with col2:

#     st.markdown("<div id='top-tracks-streams'></div>", unsafe_allow_html=True)

#     st.subheader("🎵 Top Tracks by Streams")

#     top_tracks = (
#         df.groupby(
#             "Track",
#             as_index=False
#         )["Stream"]
#         .sum()
#         .sort_values(
#             "Stream",
#             ascending=False
#         )
#         .head(10)
#         .reset_index(drop=True)
#     )

#     # Create bar position
#     top_tracks["Rank"] = range(1, len(top_tracks) + 1)

#     fig2 = px.bar(
#         top_tracks,
#         x="Rank",
#         y="Stream",
#         color="Track",
#         hover_data={
#             "Track": True,
#             "Stream": ":,",
#             "Rank": False
#         },
#         title="Top 10 Tracks by Streams"
#     )

#     fig2.update_layout(
#         showlegend=False,
#         xaxis_title=None,
#         yaxis_title="Streams",
#         xaxis=dict(
#             showticklabels=False
#         )
#     )

#     st.plotly_chart(
#         fig2,
#         use_container_width=True
#     )
# # ==========================================
# # TOP ARTISTS BY NUMBER OF SONGS
# # ==========================================

# st.markdown("<div id='top-artists-songs'></div>", unsafe_allow_html=True)

# st.subheader("🎤 Top Artists by Number of Songs")


# # Count number of songs for each artist

# artist_song_count = (
#     df.groupby(
#         "Artist",
#         as_index=False
#     )["Track"]
#     .count()
#     .rename(
#         columns={
#             "Track": "Song_Count"
#         }
#     )
#     .sort_values(
#         "Song_Count",
#         ascending=False
#     )
#     .head(10)
# )


# # Interactive Chart

# fig3 = px.bar(
#     artist_song_count,
#     x="Artist",
#     y="Song_Count",
#     color="Artist",
#     title="Top 10 Artists by Number of Songs",
#     hover_data={
#         "Artist": True,
#         "Song_Count": True
#     }
# )


# fig3.update_layout(
#     showlegend=False,
#     xaxis_title="Artist",
#     yaxis_title="Number of Songs"
# )


# st.plotly_chart(
#     fig3,
#     use_container_width=True
# )


# st.markdown("---")


# # ==========================================
# # LIKES VS VIEWS
# # ==========================================

# st.markdown("<div id='likes-views'></div>", unsafe_allow_html=True)

# st.subheader("❤️ Likes vs Views")


# # Interactive Scatter Plot

# fig4 = px.scatter(
#     df,
#     x="Views",
#     y="Likes",
#     hover_data=[
#         "Artist",
#         "Track",
#         "Views",
#         "Likes"
#     ],
#     title="Relationship Between Views and Likes"
# )


# fig4.update_layout(
#     xaxis_title="Views",
#     yaxis_title="Likes"
# )


# st.plotly_chart(
#     fig4,
#     use_container_width=True
# )


# st.markdown("---")


# # ==========================================
# # MOOD ANALYSIS (Valence vs Energy quadrants)
# # ==========================================

# st.markdown("<div id='mood-analysis'></div>", unsafe_allow_html=True)

# st.subheader("🎭 Mood Analysis: What Kind of Songs Go Viral?")


# def get_mood(row):
#     if row["Valence"] >= 0.5 and row["Energy"] >= 0.5:
#         return "Happy / Energetic"
#     if row["Valence"] >= 0.5 and row["Energy"] < 0.5:
#         return "Happy / Calm"
#     if row["Valence"] < 0.5 and row["Energy"] >= 0.5:
#         return "Angry / Intense"
#     return "Sad / Calm"


# df["Mood"] = df.apply(get_mood, axis=1)

# mood_summary = (
#     df.groupby("Mood", as_index=False)["Views"]
#     .mean()
#     .sort_values("Views", ascending=False)
# )

# col1, col2 = st.columns(2)

# with col1:
#     fig_mood_count = px.pie(
#         df,
#         names="Mood",
#         title="Distribution of Songs by Mood",
#         hole=0.4,
#     )
#     st.plotly_chart(fig_mood_count, use_container_width=True)

# with col2:
#     fig_mood_views = px.bar(
#         mood_summary,
#         x="Mood",
#         y="Views",
#         color="Mood",
#         title="Average Views by Mood Category",
#     )
#     fig_mood_views.update_layout(showlegend=False)
#     st.plotly_chart(fig_mood_views, use_container_width=True)


# st.markdown("---")


# # ==========================================
# # OFFICIAL VIDEO & LICENSING IMPACT
# # ==========================================

# # st.markdown("<div id='video-license'></div>", unsafe_allow_html=True)

# # st.subheader("🎬 Does an Official Video / License Actually Help?")

# # col1, col2 = st.columns(2)

# # with col1:
# #     video_summary = (
# #         df.groupby("official_video", as_index=False)["Views"]
# #         .mean()
# #         .dropna()
# #     )
# #     fig_video = px.bar(
# #         video_summary,
# #         x="official_video",
# #         y="Views",
# #         title="Avg Views: Official Video vs None",
# #         color="official_video",
# #     )
# #     fig_video.update_layout(showlegend=False, xaxis_title="Has Official Video?")
# #     st.plotly_chart(fig_video, use_container_width=True)

# # with col2:
# #     license_summary = (
# #         df.groupby("Licensed", as_index=False)["Views"]
# #         .mean()
# #         .dropna()
# #     )
# #     fig_license = px.bar(
# #         license_summary,
# #         x="Licensed",
# #         y="Views",
# #         title="Avg Views: Licensed vs Not",
# #         color="Licensed",
# #     )
# #     fig_license.update_layout(showlegend=False, xaxis_title="Licensed?")
# #     st.plotly_chart(fig_license, use_container_width=True)


# # st.markdown("---")


# # ==========================================
# # HIDDEN GEMS: HIGH ENGAGEMENT, LOWER VIEWS
# # ==========================================

# st.markdown("<div id='hidden-gems'></div>", unsafe_allow_html=True)

# st.subheader("💎 Hidden Gems (High Like-Rate Relative to Views)")

# gems_df = df.copy()
# gems_df["Engagement_Rate"] = (gems_df["Likes"] / gems_df["Views"]) * 100
# gems_df = gems_df[gems_df["Views"] > 500000]  # filter out near-zero-view noise

# top_gems = gems_df.nlargest(10, "Engagement_Rate")[
#     ["Artist", "Track", "Views", "Likes", "Engagement_Rate"]
# ].reset_index(drop=True)

# top_gems["Engagement_Rate"] = top_gems["Engagement_Rate"].round(2)

# st.caption("Tracks people love (high like %) even if not the most viewed")
# st.dataframe(top_gems, use_container_width=True)


# st.markdown("---")


# # ==========================================
# # WHAT AUDIO FEATURES CORRELATE WITH POPULARITY?
# # ==========================================

# st.markdown("<div id='audio-features'></div>", unsafe_allow_html=True)

# st.subheader("🎚️ Which Audio Features Drive Popularity?")

# audio_features = [
#     "Danceability", "Energy", "Loudness", "Speechiness",
#     "Acousticness", "Instrumentalness", "Liveness", "Valence",
#     "Tempo", "Duration_min",
# ]

# corr_df = df[audio_features + ["Views"]].corr()[["Views"]].drop("Views")
# corr_df = corr_df.rename(columns={"Views": "Correlation_with_Views"}).reset_index()
# corr_df = corr_df.rename(columns={"index": "Feature"})
# corr_df = corr_df.sort_values("Correlation_with_Views", ascending=True)

# fig_corr = px.bar(
#     corr_df,
#     x="Correlation_with_Views",
#     y="Feature",
#     orientation="h",
#     title="Correlation of Audio Features with Views",
#     color="Correlation_with_Views",
#     color_continuous_scale="RdBu",
# )
# st.plotly_chart(fig_corr, use_container_width=True)


# st.markdown("---")


# # ==========================================
# # ALBUM TYPE COMPARISON
# # ==========================================

# st.markdown("<div id='album-type'></div>", unsafe_allow_html=True)

# st.subheader("💿 Album vs Single vs Compilation — Which Performs Best?")

# album_summary = (
#     df.groupby("Album_type", as_index=False)
#     .agg(Avg_Views=("Views", "mean"), Track_Count=("Track", "count"))
#     .sort_values("Avg_Views", ascending=False)
# )

# fig_album = px.bar(
#     album_summary,
#     x="Album_type",
#     y="Avg_Views",
#     color="Album_type",
#     title="Average Views by Release Type",
#     hover_data=["Track_Count"],
# )
# fig_album.update_layout(showlegend=False)
# st.plotly_chart(fig_album, use_container_width=True)


# st.markdown("---")


# # ==========================================
# # PLATFORM PREFERENCE (Spotify vs YouTube)
# # ==========================================

# st.markdown("<div id='platform-split'></div>", unsafe_allow_html=True)

# st.subheader("📱 Where Do Songs Get Streamed Most?")

# platform_counts = df["most_playedon"].value_counts().reset_index()
# platform_counts.columns = ["Platform", "Count"]

# fig_platform = px.pie(
#     platform_counts,
#     names="Platform",
#     values="Count",
#     title="Most-Played-On Platform Split",
#     hole=0.4,
# )
# st.plotly_chart(fig_platform, use_container_width=True)


# st.markdown("---")


# # ==========================================
# # ARTIST DETAILS
# # ==========================================

# st.markdown("<div id='artist-details'></div>", unsafe_allow_html=True)

# st.subheader("🎤 Artist Details")


# # Get unique artist names

# artist_list = sorted(
#     df["Artist"]
#     .dropna()
#     .unique()
# )


# # Check if artists are available

# if len(artist_list) > 0:

#     # Artist Selection

#     artist = st.selectbox(
#         "Select Artist",
#         artist_list
#     )


#     # Filter selected artist

#     artist_df = df[
#         df["Artist"] == artist
#     ]


#     # ==========================================
#     # SELECTED ARTIST KPIs
#     # ==========================================

#     col1, col2, col3 = st.columns(3)


#     col1.metric(
#         "🎵 Songs",
#         len(artist_df)
#     )


#     col2.metric(
#         "👀 Views",
#         f"{int(artist_df['Views'].sum()):,}"
#     )


#     col3.metric(
#         "▶️ Streams",
#         f"{int(artist_df['Stream'].sum()):,}"
#     )


#     # ==========================================
#     # ARTIST TRACK DETAILS
#     # ==========================================

#     st.dataframe(
#         artist_df[
#             [
#                 "Track",
#                 "Views",
#                 "Likes",
#                 "Stream"
#             ]
#         ],
#         use_container_width=True
#     )


# else:

#     st.warning(
#         "No artist found. Please try another artist name."
#     )






























import streamlit as st
import pandas as pd
import plotly.express as px


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Spotify Data Dashboard",
    page_icon="🎧",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

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

/* ---- Sidebar quick-navigation buttons ---- */
.nav-button {
    display: block;
    width: 100%;
    padding: 10px 14px;
    margin-bottom: 8px;
    background-color: #1DB954;
    color: black !important;
    font-weight: 600;
    text-align: left;
    text-decoration: none !important;
    border-radius: 8px;
    transition: background-color 0.15s ease-in-out;
}

.nav-button:hover {
    background-color: #17a34a;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# TITLE
# ==========================================

st.title("🎧 Spotify Data Dashboard")

st.markdown(
    "### Analyze songs, artists, views, likes, and streaming trends"
)


# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("spotify.csv")


# ==========================================
# SIDEBAR FILTER
# ==========================================

st.sidebar.title("🎛 Filter Panel")

search = st.sidebar.text_input(
    "🔍 Search Artist"
)


# Artist Search Filter
if search:

    df = df[
        df["Artist"].str.contains(
            search,
            case=False,
            na=False
        )
    ]


# ==========================================
# SIDEBAR QUICK NAVIGATION
# (click any button -> page scrolls to that section)
# ==========================================

st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 Quick Navigation")

nav_items = {
    "📊 Overview / KPIs": "overview",
    "🔥 Top Artists by Views": "top-artists-views",
    "🎵 Top Tracks by Streams": "top-tracks-streams",
    "🎤 Top Artists by Song Count": "top-artists-songs",
    "❤️ Likes vs Views": "likes-views",
    "🎭 Mood Analysis": "mood-analysis",
    "💎 Hidden Gems": "hidden-gems",
    "🎚️ Audio Feature Correlation": "audio-features",
    "💿 Album Type Comparison": "album-type",
    "📱 Platform Split": "platform-split",
    "🎤 Artist Details": "artist-details",
}

nav_html = ""
for label, anchor in nav_items.items():
    nav_html += f'<a class="nav-button" href="#{anchor}">{label}</a>'

st.sidebar.markdown(nav_html, unsafe_allow_html=True)


# ==========================================
# KPI SECTION
# ==========================================

st.markdown("<div id='overview'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)


col1.metric(
    "🎵 Total Songs",
    len(df)
)


col2.metric(
    "👀 Total Views",
    f"{int(df['Views'].sum()):,}"
)


col3.metric(
    "▶️ Total Streams",
    f"{int(df['Stream'].sum()):,}"
)


st.markdown("---")


# ==========================================
# TOP ARTISTS BY VIEWS
# ==========================================

st.markdown("<div id='top-artists-views'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.subheader("🔥 Top Artists by Views")

    top_artists = (
        df.groupby(
            "Artist",
            as_index=False
        )["Views"]
        .sum()
        .sort_values(
            "Views",
            ascending=False
        )
        .head(10)
        .reset_index(drop=True)
    )

    # Create bar position
    top_artists["Rank"] = range(1, len(top_artists) + 1)

    fig1 = px.bar(
        top_artists,
        x="Rank",
        y="Views",
        color="Artist",
        hover_data={
            "Artist": True,
            "Views": ":,",
            "Rank": False
        },
        title="Top 10 Artists by Views"
    )

    fig1.update_layout(
        showlegend=False,
        xaxis_title=None,
        yaxis_title="Views",
        xaxis=dict(
            showticklabels=False
        )
    )

    st.plotly_chart(
        fig1,
        width="stretch"
    )

# ==========================================
# TOP TRACKS BY STREAMS
# ==========================================

with col2:

    st.markdown("<div id='top-tracks-streams'></div>", unsafe_allow_html=True)

    st.subheader("🎵 Top Tracks by Streams")

    top_tracks = (
        df.groupby(
            "Track",
            as_index=False
        )["Stream"]
        .sum()
        .sort_values(
            "Stream",
            ascending=False
        )
        .head(10)
        .reset_index(drop=True)
    )

    # Create bar position
    top_tracks["Rank"] = range(1, len(top_tracks) + 1)

    fig2 = px.bar(
        top_tracks,
        x="Rank",
        y="Stream",
        color="Track",
        hover_data={
            "Track": True,
            "Stream": ":,",
            "Rank": False
        },
        title="Top 10 Tracks by Streams"
    )

    fig2.update_layout(
        showlegend=False,
        xaxis_title=None,
        yaxis_title="Streams",
        xaxis=dict(
            showticklabels=False
        )
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )
# ==========================================
# TOP ARTISTS BY NUMBER OF SONGS
# ==========================================

st.markdown("<div id='top-artists-songs'></div>", unsafe_allow_html=True)

st.subheader("🎤 Top Artists by Number of Songs")


# Count number of songs for each artist

artist_song_count = (
    df.groupby(
        "Artist",
        as_index=False
    )["Track"]
    .count()
    .rename(
        columns={
            "Track": "Song_Count"
        }
    )
    .sort_values(
        "Song_Count",
        ascending=False
    )
    .head(10)
)


# Interactive Chart

fig3 = px.bar(
    artist_song_count,
    x="Artist",
    y="Song_Count",
    color="Artist",
    title="Top 10 Artists by Number of Songs",
    hover_data={
        "Artist": True,
        "Song_Count": True
    }
)


fig3.update_layout(
    showlegend=False,
    xaxis_title="Artist",
    yaxis_title="Number of Songs"
)


st.plotly_chart(
    fig3,
    width="stretch"
)


st.markdown("---")


# ==========================================
# LIKES VS VIEWS
# ==========================================

st.markdown("<div id='likes-views'></div>", unsafe_allow_html=True)

st.subheader("❤️ Likes vs Views")


# Interactive Scatter Plot

fig4 = px.scatter(
    df,
    x="Views",
    y="Likes",
    hover_data=[
        "Artist",
        "Track",
        "Views",
        "Likes"
    ],
    title="Relationship Between Views and Likes"
)


fig4.update_layout(
    xaxis_title="Views",
    yaxis_title="Likes"
)


st.plotly_chart(
    fig4,
    width="stretch"
)


st.markdown("---")


# ==========================================
# MOOD ANALYSIS (Valence vs Energy quadrants)
# ==========================================

st.markdown("<div id='mood-analysis'></div>", unsafe_allow_html=True)

st.subheader("🎭 Mood Analysis: What Kind of Songs Go Viral?")


def get_mood(row):
    if row["Valence"] >= 0.5 and row["Energy"] >= 0.5:
        return "Happy / Energetic"
    if row["Valence"] >= 0.5 and row["Energy"] < 0.5:
        return "Happy / Calm"
    if row["Valence"] < 0.5 and row["Energy"] >= 0.5:
        return "Angry / Intense"
    return "Sad / Calm"


df["Mood"] = df.apply(get_mood, axis=1)

mood_summary = (
    df.groupby("Mood", as_index=False)["Views"]
    .mean()
    .sort_values("Views", ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    fig_mood_count = px.pie(
        df,
        names="Mood",
        title="Distribution of Songs by Mood",
        hole=0.4,
    )
    st.plotly_chart(fig_mood_count, width="stretch")

with col2:
    fig_mood_views = px.bar(
        mood_summary,
        x="Mood",
        y="Views",
        color="Mood",
        title="Average Views by Mood Category",
    )
    fig_mood_views.update_layout(showlegend=False)
    st.plotly_chart(fig_mood_views, width="stretch")


st.markdown("---")


# ==========================================
# OFFICIAL VIDEO & LICENSING IMPACT
# ==========================================

# st.markdown("<div id='video-license'></div>", unsafe_allow_html=True)

# st.subheader("🎬 Does an Official Video / License Actually Help?")

# col1, col2 = st.columns(2)

# with col1:
#     video_summary = (
#         df.groupby("official_video", as_index=False)["Views"]
#         .mean()
#         .dropna()
#     )
#     fig_video = px.bar(
#         video_summary,
#         x="official_video",
#         y="Views",
#         title="Avg Views: Official Video vs None",
#         color="official_video",
#     )
#     fig_video.update_layout(showlegend=False, xaxis_title="Has Official Video?")
#     st.plotly_chart(fig_video, width="stretch")

# with col2:
#     license_summary = (
#         df.groupby("Licensed", as_index=False)["Views"]
#         .mean()
#         .dropna()
#     )
#     fig_license = px.bar(
#         license_summary,
#         x="Licensed",
#         y="Views",
#         title="Avg Views: Licensed vs Not",
#         color="Licensed",
#     )
#     fig_license.update_layout(showlegend=False, xaxis_title="Licensed?")
#     st.plotly_chart(fig_license, width="stretch")


# st.markdown("---")


# ==========================================
# HIDDEN GEMS: HIGH ENGAGEMENT, LOWER VIEWS
# ==========================================

st.markdown("<div id='hidden-gems'></div>", unsafe_allow_html=True)

st.subheader("💎 Hidden Gems (High Like-Rate Relative to Views)")

gems_df = df.copy()
gems_df["Engagement_Rate"] = (gems_df["Likes"] / gems_df["Views"]) * 100
gems_df = gems_df[gems_df["Views"] > 500000]  # filter out near-zero-view noise

top_gems = gems_df.nlargest(10, "Engagement_Rate")[
    ["Artist", "Track", "Views", "Likes", "Engagement_Rate"]
].reset_index(drop=True)

top_gems["Engagement_Rate"] = top_gems["Engagement_Rate"].round(2)

st.caption("Tracks people love (high like %) even if not the most viewed")
st.dataframe(top_gems, width="stretch")


st.markdown("---")


# ==========================================
# WHAT AUDIO FEATURES CORRELATE WITH POPULARITY?
# ==========================================

st.markdown("<div id='audio-features'></div>", unsafe_allow_html=True)

st.subheader("🎚️ Which Audio Features Drive Popularity?")

audio_features = [
    "Danceability", "Energy", "Loudness", "Speechiness",
    "Acousticness", "Instrumentalness", "Liveness", "Valence",
    "Tempo", "Duration_min",
]

corr_df = df[audio_features + ["Views"]].corr()[["Views"]].drop("Views")
corr_df = corr_df.rename(columns={"Views": "Correlation_with_Views"}).reset_index()
corr_df = corr_df.rename(columns={"index": "Feature"})
corr_df = corr_df.sort_values("Correlation_with_Views", ascending=True)

fig_corr = px.bar(
    corr_df,
    x="Correlation_with_Views",
    y="Feature",
    orientation="h",
    title="Correlation of Audio Features with Views",
    color="Correlation_with_Views",
    color_continuous_scale="RdBu",
)
st.plotly_chart(fig_corr, width="stretch")


st.markdown("---")


# ==========================================
# ALBUM TYPE COMPARISON
# ==========================================

st.markdown("<div id='album-type'></div>", unsafe_allow_html=True)

st.subheader("💿 Album vs Single vs Compilation — Which Performs Best?")

album_summary = (
    df.groupby("Album_type", as_index=False)
    .agg(Avg_Views=("Views", "mean"), Track_Count=("Track", "count"))
    .sort_values("Avg_Views", ascending=False)
)

fig_album = px.bar(
    album_summary,
    x="Album_type",
    y="Avg_Views",
    color="Album_type",
    title="Average Views by Release Type",
    hover_data=["Track_Count"],
)
fig_album.update_layout(showlegend=False)
st.plotly_chart(fig_album, width="stretch")


st.markdown("---")


# ==========================================
# PLATFORM PREFERENCE (Spotify vs YouTube)
# ==========================================

st.markdown("<div id='platform-split'></div>", unsafe_allow_html=True)

st.subheader("📱 Where Do Songs Get Streamed Most?")

platform_counts = df["most_playedon"].value_counts().reset_index()
platform_counts.columns = ["Platform", "Count"]

fig_platform = px.pie(
    platform_counts,
    names="Platform",
    values="Count",
    title="Most-Played-On Platform Split",
    hole=0.4,
)
st.plotly_chart(fig_platform, width="stretch")


st.markdown("---")


# ==========================================
# ARTIST DETAILS
# ==========================================

st.markdown("<div id='artist-details'></div>", unsafe_allow_html=True)

st.subheader("🎤 Artist Details")


# Get unique artist names

artist_list = sorted(
    df["Artist"]
    .dropna()
    .unique()
)


# Check if artists are available

if len(artist_list) > 0:

    # Artist Selection

    artist = st.selectbox(
        "Select Artist",
        artist_list
    )


    # Filter selected artist

    artist_df = df[
        df["Artist"] == artist
    ]


    # ==========================================
    # SELECTED ARTIST KPIs
    # ==========================================

    col1, col2, col3 = st.columns(3)


    col1.metric(
        "🎵 Songs",
        len(artist_df)
    )


    col2.metric(
        "👀 Views",
        f"{int(artist_df['Views'].sum()):,}"
    )


    col3.metric(
        "▶️ Streams",
        f"{int(artist_df['Stream'].sum()):,}"
    )


    # ==========================================
    # ARTIST TRACK DETAILS
    # ==========================================

    st.dataframe(
        artist_df[
            [
                "Track",
                "Views",
                "Likes",
                "Stream"
            ]
        ],
        width="stretch"
    )


else:

    st.warning(
        "No artist found. Please try another artist name."
    )