# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.
- My recommender compares genre, mood, energy, tempo, valence
- Songs get higher score if they match user preferences
- Then I rank songs and recommend the top ones

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

This recommendation system uses a content-based approach to suggest songs to users. It compares song features such as genre, mood, energy, tempo, and valence with the user’s preferences.
Each song is given a score based on how closely it matches the user’s taste. Songs that have the same genre and mood as the user are given higher priority. Numerical features like energy, tempo, and valence are scored based on how close they are to the user’s preferred values.
After scoring all songs, the system ranks them from highest to lowest score and recommends the top results.

## Features Used

### Song Features:
- genre
- mood
- energy
- tempo_bpm
- valence

### User Profile Features:
- preferred_genre
- preferred_mood
- preferred_energy
- preferred_tempo_bpm
- preferred_valence

## Scoring Logic

The system assigns a score to each song using the following rules:

- +1 point if the song's genre matches the user's preferred genre
- +1 point if the song's mood matches the user's preferred mood
- Add higher points if the song’s energy is close to the user’s preferred energy
- Add higher points if the song’s tempo is close to the user’s preferred tempo
- Add higher points if the song’s valence is close to the user’s preferred valence

Genre is given slightly higher importance than mood because it defines the overall type of music, while mood can vary more depending on the situation.

## Scoring vs Ranking

The scoring rule determines how well a single song matches the user’s preferences.
The ranking rule sorts all songs based on their scores and selects the top results to recommend.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Example Output
Images/image1.png

## Evaluation

### Happy Pop
!Images/Image2.png

### Chill Lofi
!Images/Image3.png

### Intense Rock
!Images/Image4.png

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I tested a smaller genre weight, and the recommendations became slightly more diverse because energy and tempo had more influence.
---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me understand how recommender systems turn user preferences into scores and rankings. I learned that even a simple scoring system can produce reasonable recommendations, but small design choices like feature weights can strongly affect the final output.
It also showed me that recommendation systems can easily become biased toward certain features or repeated items, especially when the dataset is small. Human judgment still matters when deciding whether the recommendations actually feel right.

## Evaluation

I tested the recommender with three user profiles: Happy Pop, Chill Lofi, and Intense Rock.
For Happy Pop, the system recommended upbeat, energetic songs such as "Sunrise City" and "Gym Hero," which matched the profile well.
For Chill Lofi, the recommendations shifted toward calmer and lower-energy tracks like "Library Rain," "Midnight Coding," and "Focus Flow." This suggests the energy, tempo, and genre features were working together well.
For Intense Rock, "Storm Runner" ranked first, which made sense because it matched both genre and mood strongly. However, some non-rock songs still appeared lower in the list because they had similar energy and tempo values.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

## Limitations and Bias

One limitation is that the recommender depends on a very small dataset, so the same songs can appear often across different profiles.
Another weakness is that genre has a strong influence, which may reduce diversity in the results.
The system also simplifies music taste into only a few features like genre, mood, energy, tempo, and valence, so it cannot capture more complex preferences such as lyrics, cultural context, or artist loyalty.

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

