from openai import OpenAI
import json, os
from dotenv import load_dotenv
import faiss
import numpy as np

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("./data/games.json", "r") as f:
    games = json.load(f)

slot_games = games["slot_games"]

game_texts = [json.dumps(game, ensure_ascii=False) for game in slot_games]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=game_texts
)

game_vectors = np.array([r.embedding for r in response.data], dtype="float32")

faiss.normalize_L2(game_vectors)

index = faiss.IndexFlatIP(game_vectors.shape[1])
index.add(game_vectors)

faiss.write_index(index, "./indexes/game_index_cosine.faiss")
with open("./data/game_metadata.json", "w") as f:
    json.dump(slot_games, f)
