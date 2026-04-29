VALID_MOODS = ["happy", "sad", "calm", "focused", "motivated", "energetic"]
VALID_CONTEXTS = ["studying", "gym", "relaxing", "commute", "sleep", "party"]


def validate_input(user_mood, user_context):
    if not user_mood or not user_mood.strip():
        return False, "Mood cannot be empty."

    if not user_context or not user_context.strip():
        return False, "Context cannot be empty."

    if user_mood.lower().strip() not in VALID_MOODS:
        return False, f"Invalid mood. Choose from: {', '.join(VALID_MOODS)}"

    if user_context.lower().strip() not in VALID_CONTEXTS:
        return False, f"Invalid context. Choose from: {', '.join(VALID_CONTEXTS)}"

    return True, "Input is valid."
