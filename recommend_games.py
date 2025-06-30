def recommend_games(query_game_dict, top_k=5):
    """
    Given a query game return top_k recommended games.
    
    Parameters:
    - query_game (dict): The game that was selected/played.
    - top_k (int): The number of similar games to return

    Returns:
    - dictionary of the queried game and the recommended games
    """
    import json, faiss, numpy as np
    from openai import OpenAI
    from dotenv import load_dotenv
    import os

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    index = faiss.read_index("./indexes/game_index_cosine.faiss")
    with open("./data/game_metadata.json", "r") as f:
        games = json.load(f)

    # Embed and normalize query
    query_text = json.dumps(query_game_dict, ensure_ascii=False)
    query_vector = client.embeddings.create(
        model="text-embedding-3-small",
        input=query_text
    ).data[0].embedding

    query_vector = np.array([query_vector]).astype("float32")
    faiss.normalize_L2(query_vector)

    # Search for top_k similar games
    D, I = index.search(query_vector, top_k+1)
    returned_games = [games[i] for i in I[0]]
    result = {
        "query_game": query_game_dict,
        "recommended_games": returned_games[1:top_k+1]
    }
    return result

def generate_explanations(query_game, recommended_games, model="gpt-4o-mini"):
    """
    Given a query game and a list of recommended games, return explanations for each recommendation.
    
    Parameters:
    - query_game (dict): The game that was selected/played.
    - recommended_games (list of dict): List of recommended games to explain.
    - model (str): The OpenAI model to use (default: gpt-4o-mini).

    Returns:
    - list of str: Explanations for each recommended game.
    """
    import openai
    import os
    from dotenv import load_dotenv
    import json

    load_dotenv()
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    explanations = []

    for rec_game in recommended_games:
        prompt = f"""Explain in an end user friendly way in 1 short sentence why game B is similar to game b in this format: This game is similar because...:

    Game A:
    {json.dumps(query_game, indent=2)}

    Game B:
    {json.dumps(rec_game, indent=2)}"""

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        explanation = response.choices[0].message.content.strip()
        explanations.append(explanation)

    return explanations