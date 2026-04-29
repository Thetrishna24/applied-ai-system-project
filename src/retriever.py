import pandas as pd
from src.logger import log_event


def load_songs(file_path="data/songs.csv"):
    return pd.read_csv(file_path)


def keyword_similarity(query, song_text):
    query_words = set(query.lower().split())
    song_words = set(song_text.lower().split())

    if not query_words:
        return 0

    matches = query_words.intersection(song_words)
    return len(matches) / len(query_words)


def retrieve_songs(user_mood, user_context, top_k=5):
    songs = load_songs()

    query = f"{user_mood} {user_context}"

    songs["combined_text"] = (
        songs["title"] + " "
        + songs["artist"] + " "
        + songs["genre"] + " "
        + songs["mood"] + " "
        + songs["context"] + " "
        + songs["description"]
    )

    songs["similarity"] = songs["combined_text"].apply(
        lambda text: keyword_similarity(query, text)
    )

    ranked = songs.sort_values(by="similarity", ascending=False).head(top_k)

    log_event(f"Retrieved {len(ranked)} songs for query: {query}")

    return ranked
