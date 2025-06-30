# llm-game-recommender

This is a prototype slot game recommendation system where a user selects the game they ave just played and the app recommends five similar games based on game features using an LLM and vector similary search.

## Components

### LLM
OpenAI's API was chosen for it's ease of use through the well documented SDK and fast response times.

### Dataset
The dataset features were chosen based on pointers from the task description (Volitility, Theme, Title) and by going onto the Bally's Casion Games website to see what information is given about the slot games which users may use to inform their choice of game e.g. minimum bet, playlines and max win multiplier. I used gpt-4 as it is the most creative model and I used a temperature of 0.7 to improve the diversity of the generated data.

### Vectorisation
The OpenAI embedding model was used for it's ability to create rich dense embeddings that have semantic meaning encoded within them.

### Index
I used a FAISS index because unlike LLM comparisons it uses consistant similarity search methods. It's open source easy to use index which can be built in just a few lines of code and works well with OpenAI embeddings. It's optimised for fast similarity search and can handle millions of vectors. Given the dataset of just 150 games/vectors FAISS quickly returns recommendations. Lastly it can also be used for production environments.

### Explainer
I used OpenAI's gpt-4o-mini for the explanations for the following reasons:
1. Any one of OpenAI's active LLM's are capable of comparing data where numerical or textual. 
2. Originall gpt-4 was used for the comparison, however this made returning recommendations in the front end too slow so 4o-mini was chosen as it's a smaller faster model.

### Front End
I used a simple streamlit frontend as I am most familiar with streamlit.

## Project structure
app.py                    # Streamlit front end
recommend_games.py        # Core recommendation engine
generate_explanations.py  # LLM-based similarity explanations
./data/game_metadata.json # Dataset of slot games
./indexes/game_index_cosine.faiss # FAISS cosine index
📄 requirements.txt
📄 README.md

## How to run locally

1. Clone this repo

git clone https://github.com/levy123/llm-game-recommender.git

2. Install dependencies

pip install -r requirements.txt

3. Set your OpenAI key in the terminal or in a .env file (Set in terminal):

export OPENAI_API_KEY=your-key-here

4. Run the app
streamlit run app.py
