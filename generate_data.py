from openai import OpenAI
import json, os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

sample_schema = {
  "slot_games":[ 
      {
      "title": "Jungle Riches",
      "theme": "Jungle/Adventure",
      "volatility": "High",
      "features": ["Free Spins", "Wild Symbols", "Multiplier"],
      "reels": 5,
      "art_style": "Cartoonish",
      "soundtrack_style": "Tribal Drums",
      "payout_percentage": 96.5,
      "minimum_bet_gbp": 0.4,
      "playlines": 20,
      "max_win_multiplier": 972,
      }
  ]
}

prompt = f"Generate a JSON array of 150 fictional casino slot games following this schema: {sample_schema}"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    response_format={"type": "json_object"}
)

with open("./data/games.json", "w") as f:
    json.dump(json.loads(response.choices[0].message.content), f, indent=2)

