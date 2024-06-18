import unittest
from sentiment_analysis.analysis import analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):

    def test_positive_sentiment(self):
        self.assertEqual(analyze_sentiment("I love this!"), "Positive")

    def test_negative_sentiment(self):
        self.assertEqual(analyze_sentiment("I hate this!"), "Negative")

    def test_neutral_sentiment(self):
        self.assertEqual(analyze_sentiment("This is okay."), "Neutral")

if __name__ == "__main__":
    unittest.main()
