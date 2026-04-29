def explain_recommendation(song, user_mood, user_context):
    reasons = []

    if song["mood"].lower() == user_mood.lower():
        reasons.append("it matches your mood")

    if song["context"].lower() == user_context.lower():
        reasons.append("it fits your current activity")

    if not reasons:
        reasons.append("it is similar to your preferences")

    reason_text = " and ".join(reasons)

    return (
        f"{song['title']} by {song['artist']} is recommended because {reason_text}. "
        f"It is a {song['genre']} track described as: {song['description']}. "
        f"Confidence score: {song['confidence']}"
    )
