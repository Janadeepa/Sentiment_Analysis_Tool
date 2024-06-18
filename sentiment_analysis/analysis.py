from textblob import TextBlob
from .preprocessing import preprocess_text

def analyze_sentiment(text):
    preprocessed_text = preprocess_text(text)
    blob = TextBlob(preprocessed_text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
