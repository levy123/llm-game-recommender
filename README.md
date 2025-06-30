# llm-game-recommender

This is a prototype slot game recommendation system where a user selects the game they ave just played and the app recommends five similar games based on game features using an LLM and vector similary search.

## Components

### LLM
OpenAI's API was chosen for it's ease of use through the well documented SDK and fast response times.

### Dataset
The dataset features were chosen based on pointers from the task description (Volitility, Theme, Title) and by going onto the Bally's Casion Games website to see what information is given about the slot games which users may use to inform their choice of game e.g. minimum bet, playlines and max win multiplier.

### Vectorisation
The OpenAI embedding model was used for it's ability to create rich embeddings that have semantic meaning encoded within them.

### Index
I used a FAISS index because this is an open source easy to use index which can be built in just a few lines of code. It's optimised for fast similarity search 


## Why I chose the json schema for the games

## OpenAI clieny paramaters

temperature , goal rich and diverse dataset