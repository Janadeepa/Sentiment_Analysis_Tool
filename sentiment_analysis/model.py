from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment_advanced(text):
    result = sentiment_pipeline(text)[0]
    return result["label"]
