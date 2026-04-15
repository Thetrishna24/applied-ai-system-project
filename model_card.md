# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Simple Music Recommender (VibeFinder 1.0)
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender is designed to suggest songs based on a user’s preferences such as genre, mood and energy level. It generates a ranked list of songs that best match these preferences.
The system assumes that users have clear preferences such as liking “happy” songs or “high-energy” music. It does not learn from past behavior, it only uses the preferences given at runtime.
This project is intended for classroom exploration to understand how recommendation systems work, not for real-world deployment.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model evaluates each song based on how well it matches the user’s preferences.
It uses features like:
- Genre  
- Mood  
- Energy  
- Tempo  
- Valence  

The system gives points when a song matches the user’s preferred genre or mood. For numerical features like energy or tempo, it calculates how close the song’s value is to the user’s preference.
All these values are combined into a final score, and songs are ranked from highest to lowest score.
Compared to the starter logic, I added clearer weighting and explanation output so users can understand 'why' a song was recommended.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset contains around 10 songs with features such as genre, mood, energy, tempo, valence, danceability, and acousticness.
The dataset includes a mix of pop, lofi, and rock songs, but it is small and limited in diversity.
No additional data was added or removed.
Because of the small size, many types of music and user tastes are not represented.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well when user preferences are clear and aligned (like “happy pop” or “chill lofi”).
It captures intuitive patterns such as:
- Matching genre strongly improves recommendations  
- Energy closeness helps rank songs more realistically  
In many cases, the top recommendations felt reasonable and aligned with expectations for each profile.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system is limited by its small dataset, which causes the same songs to appear frequently across different user profiles.
It also heavily favors genre matching, which can overpower other features like mood or tempo.
The model does not consider:
- Lyrics  
- Artist similarity  
- User listening history
Because of this, it may not reflect real user preferences accurately and can feel repetitive.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the system using multiple user profiles such as:
- Happy Pop  
- Chill Lofi  
- Intense Rock  
For each profile, I checked whether the top recommendations made sense based on the preferences.
One surprising result was that some songs appeared in multiple profiles, showing that the scoring system can be biased toward certain features.
I also observed how changing preferences affected ranking order.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

- Use a larger and more diverse dataset  
- Add more features like artist similarity or lyrics  
- Improve scoring weights dynamically  
- Increase diversity in recommendations  
- Possibly apply machine learning instead of fixed scoring 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

This project helped me understand how recommendation systems can be built using simple logic. Even without machine learning, combining a few features can produce meaningful results.
One interesting discovery was how sensitive the system is to scoring weights, small changes can significantly impact recommendations.
It also showed me why real-world systems are much more complex, as they need to handle diverse users and large datasets.
