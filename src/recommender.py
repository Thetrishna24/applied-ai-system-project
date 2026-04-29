from src.retriever import retrieve_songs
from src.logger import log_event


def score_song(song, user_mood, user_context):
    score = 0

    if song["mood"].lower() == user_mood.lower():
        score += 3

    if song["context"].lower() == user_context.lower():
        score += 3

    score += float(song["similarity"]) * 4

    confidence = min(score / 10, 1.0)

    return score, confidence


def recommend_songs(user_mood, user_context, top_n=3):
    candidates = retrieve_songs(user_mood, user_context)

    scored = []

    for _, song in candidates.iterrows():
        score, confidence = score_song(song, user_mood, user_context)

        scored.append({
            "title": song["title"],
            "artist": song["artist"],
            "genre": song["genre"],
            "mood": song["mood"],
            "context": song["context"],
            "score": round(score, 2),
            "confidence": round(confidence, 2),
            "description": song["description"]
        })

    ranked = sorted(scored, key=lambda x: x["score"], reverse=True)[:top_n]

    log_event(f"Ranked top {len(ranked)} recommendations")

    return ranked
