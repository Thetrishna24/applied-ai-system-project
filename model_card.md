
# Model Card: MoodSync AI

## Model Type
Rule-based + Retrieval-Augmented Recommendation System

## Inputs
- Mood (string)
- Context (string)

## Outputs
- Ranked list of songs
- Explanation for each recommendation
- Confidence score

## Training Data
- Static CSV dataset of songs with attributes (mood, context, energy, description)

## Evaluation
- Unit tests using pytest
- Consistency and correctness checks

## Limitations
- No real user personalization
- No deep learning model
- Small dataset

## Ethical Considerations
- Bias in dataset
- Not suitable for mental health advice
