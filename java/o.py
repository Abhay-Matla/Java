import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Ensure VADER resources are available
nltk.download('vader_lexicon')

# Sample list of product reviews
reviews = [
    "The product is amazing! I loved the quality and the design.",
    "This is the worst purchase I have ever made. Totally disappointing.",
    "The product is okay, but the delivery was late.",
    "I am extremely happy with the product. It works perfectly!",
    "Not worth the price. The quality is bad.",
]

# Initialize VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

# Function to analyze sentiment using VADER
def vader_sentiment(review):
    score = vader_analyzer.polarity_scores(review)
    if score['compound'] >= 0.05:
        return "positive"
    elif score['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

# Function to analyze sentiment using TextBlob
def textblob_sentiment(review):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity < 0:
        return "negative"
    else:
        return "neutral"

# Analyze sentiments and store results
results = {
    "review": [],
    "vader_sentiment": [],
    "textblob_sentiment": []
}

for review in reviews:
    vader_result = vader_sentiment(review)
    textblob_result = textblob_sentiment(review)
    results["review"].append(review)
    results["vader_sentiment"].append(vader_result)
    results["textblob_sentiment"].append(textblob_result)

# Output the results
print("Review Sentiment Analysis Results:")
for i, review in enumerate(reviews):
    print(f"Review: {review}")
    print(f"VADER Sentiment: {results['vader_sentiment'][i]}")
    print(f"TextBlob Sentiment: {results['textblob_sentiment'][i]}")
    print("-" * 60)

# Calculate overall sentiment distribution
def sentiment_distribution(sentiments):
    distribution = {"positive": 0, "neutral": 0, "negative": 0}
    for sentiment in sentiments:
        distribution[sentiment] += 1
    return distribution

# Summary of sentiment analysis
vader_distribution = sentiment_distribution(results["vader_sentiment"])
textblob_distribution = sentiment_distribution(results["textblob_sentiment"])

print("Overall Sentiment Distribution:")
print(f"VADER: {vader_distribution}")
print(f"TextBlob: {textblob_distribution}")
