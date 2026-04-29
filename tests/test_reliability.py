from src.guardrails import validate_input
from src.recommender import recommend_songs


def test_empty_mood_is_rejected():
    is_valid, message = validate_input("", "party")
    assert is_valid is False
    assert "Mood cannot be empty" in message


def test_invalid_mood_is_rejected():
    is_valid, message = validate_input("hapy", "party")
    assert is_valid is False
    assert "Invalid mood" in message


def test_consistent_recommendations():
    result_1 = recommend_songs("happy", "party")
    result_2 = recommend_songs("happy", "party")
    assert result_1 == result_2
