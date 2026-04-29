from src.recommender import recommend_songs


def test_happy_party_recommendation():
    results = recommend_songs("happy", "party")
    assert len(results) > 0
    assert results[0]["title"] == "Good Day"
    assert results[0]["confidence"] > 0.8


def test_calm_studying_recommendation():
    results = recommend_songs("calm", "studying")
    assert len(results) > 0
    assert results[0]["context"] == "studying"


def test_motivated_gym_recommendation():
    results = recommend_songs("motivated", "gym")
    assert len(results) > 0
    assert results[0]["title"] == "Heavy Lift"
