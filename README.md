# Sentiment Analyzer

Real-time sentiment analysis tool for text data using lexicon-based and ML approaches.

## Features
- Lexicon-based sentiment scoring (VADER-inspired)
- Aspect-based sentiment analysis
- Batch processing support
- REST API endpoint

## Usage
```python
from analyzer import SentimentAnalyzer
sa = SentimentAnalyzer()
result = sa.analyze("This product is amazing!")
print(result)  # {'positive': 0.85, 'negative': 0.05, 'neutral': 0.10}
```
