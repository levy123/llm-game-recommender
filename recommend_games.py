def recommend_games(query_game_dict, top_k=5):
    import json, faiss, numpy as np
    from openai import OpenAI
    from dotenv import load_dotenv
    import os

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    index = faiss.read_index("game_index_cosine.faiss")
    with open("game_metadata.json", "r") as f:
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
    D, I = index.search(query_vector, top_k)
    return [games[i] for i in I[0]]