"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    
    print(f"Loaded songs: {len(songs)}")
    # print(songs[0])

    # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    # user_prefs = {
    # "genre": "pop",
    # "mood": "happy",
    # "energy": 0.8,
    # "tempo_bpm": 120.0,
    # "valence": 0.8
    # }
    profiles = [
    {
        "name": "Happy Pop",
        "prefs": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "tempo_bpm": 120.0,
            "valence": 0.8
        }
    },
    {
        "name": "Chill Lofi",
        "prefs": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3,
            "tempo_bpm": 80.0,
            "valence": 0.5
        }
    },
    {
        "name": "Intense Rock",
        "prefs": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "tempo_bpm": 150.0,
            "valence": 0.6
        }
    }
   ]

    # recommendations = recommend_songs(user_prefs, songs, k=5)

    # print("\nTop recommendations:\n")

    # for i, rec in enumerate(recommendations, start=1):
    #     song, score, explanation = rec
    #     print(f"{i}. {song['title']} by {song['artist']}")
    #     print(f"   Score: {score:.2f}")
    #     print(f"   Why: {explanation}")
    #     print()
    
    for profile in profiles:
        print(f"\n===== {profile['name']} =====\n")

        recommendations = recommend_songs(profile["prefs"], songs, k=5)

        for i, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print()

if __name__ == "__main__":
    main()
