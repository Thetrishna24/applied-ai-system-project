from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs
    # print(f"Loading songs from {csv_path}...")
    # return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Genre match
    if "genre" in user_prefs and song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match
    if "mood" in user_prefs and song["mood"] == user_prefs["mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    # Energy closeness
    if "energy" in user_prefs:
        energy_diff = abs(song["energy"] - user_prefs["energy"])
        energy_score = max(0.0, 1.5 - (energy_diff * 1.5))
        score += energy_score
        reasons.append(f"energy closeness (+{energy_score:.2f})")

    # Tempo closeness
    if "tempo_bpm" in user_prefs:
        tempo_diff = abs(song["tempo_bpm"] - user_prefs["tempo_bpm"])
        tempo_score = max(0.0, 1.0 - (tempo_diff / 100))
        score += tempo_score
        reasons.append(f"tempo closeness (+{tempo_score:.2f})")

    # Valence closeness
    if "valence" in user_prefs:
        valence_diff = abs(song["valence"] - user_prefs["valence"])
        valence_score = max(0.0, 1.0 - valence_diff)
        score += valence_score
        reasons.append(f"valence closeness (+{valence_score:.2f})")

    return score, reasons
    # Expected return format: (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)

    return scored_songs[:k]
    # Expected return format: (song_dict, score, explanation)
