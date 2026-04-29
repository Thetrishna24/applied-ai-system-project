from src.guardrails import validate_input
from src.recommender import recommend_songs
from src.explainer import explain_recommendation


def main():
    print("🎵 MoodSync AI: Music Recommendation System")
    print("------------------------------------------")

    user_mood = input("Enter your mood (happy, sad, calm, focused, motivated): ")
    user_context = input("Enter your context (studying, gym, relaxing, commute, sleep, party): ")

    is_valid, message = validate_input(user_mood, user_context)

    if not is_valid:
        print(f"Error: {message}")
        return

    recommendations = recommend_songs(user_mood, user_context)

    print("\nTop Recommendations:")
    for index, song in enumerate(recommendations, start=1):
        print(f"\n{index}. {song['title']} by {song['artist']}")
        print(explain_recommendation(song, user_mood, user_context))


if __name__ == "__main__":
    main()
