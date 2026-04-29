
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

### AI Collaboration
This project demonstrates how retrieval-based systems can simulate intelligent behavior without relying on large pretrained models. The combination of retrieval, scoring, and explanation mimics an AI assistant pipeline.

### Bias
The dataset is small and may not represent diverse music preferences or cultures. Recommendations may be biased toward limited genres and moods.

### Testing Results
All 6 unit tests passed successfully. The system was consistent across repeated runs and correctly handled invalid inputs through guardrails.
