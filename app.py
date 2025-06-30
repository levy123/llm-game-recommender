import streamlit as st
import json
from recommend_games import recommend_games, generate_explanations

# Load game metadata to populate the dropdown
with open("./data/game_metadata.json", "r") as f:
    metadata = json.load(f)

# Convert to list if it's a dict
games = list(metadata.values()) if isinstance(metadata, dict) else metadata

# Build dropdown
st.title("🎰 Slot Game Recommender")
titles = [game["title"] for game in games]
selected_title = st.selectbox("Select a game you just played:", titles)

# Trigger recommendation
if selected_title:
    query_game = next(game for game in games if game["title"] == selected_title)

    # Use your custom recommend_games function
    result = recommend_games(query_game)
    recommended_games = result["recommended_games"]

    # Generate explanations
    explanations = generate_explanations(result["query_game"], recommended_games)

    # Display results
    st.subheader("Recommended Games")
    for game, explanation in zip(recommended_games, explanations):
        st.markdown(f"**🎲 {game['title']}**")
        st.caption(f"Theme: {game['theme']} | Volatility: {game['volatility']} | Payout: {game['payout_percentage']}%")
        st.markdown(f"🧠 _{explanation}_")
        st.markdown("---")
