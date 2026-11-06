from textblob import TextBlob

# Realistic sample book reviews
reviews = [
    "This book was absolutely fantastic! The story was engaging and the characters were well developed.",
    "I really enjoyed reading this novel. Highly recommended for anyone who loves mystery.",
    "The book was average. Some parts were interesting but it became boring halfway through.",
    "Waste of money. The plot was weak and the writing style was poor.",
    "One of the best books I have read this year. I couldn't put it down!",
    "Not what I expected. The ending was very disappointing.",
    "A beautifully written story with deep emotions and great storytelling.",
    "It was okay, but I wouldn't read it again.",
    "Terrible book. I stopped reading after the first few chapters.",
    "Amazing! The author did a wonderful job with the character development."
]

print("========== BOOK REVIEWS SENTIMENT ANALYSIS ==========\n")

positive_count = 0
negative_count = 0
neutral_count = 0

for i, review in enumerate(reviews, 1):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
        positive_count += 1
    elif polarity < -0.1:
        sentiment = "Negative"
        negative_count += 1
    else:
        sentiment = "Neutral"
        neutral_count += 1

    print("Review", i, ":", review)
    print("Polarity Score:", round(polarity, 2), "→", sentiment)
    print("-" * 60)

print("\n========== SUMMARY ==========")
print("Positive Reviews:", positive_count)
print("Negative Reviews:", negative_count)
print("Neutral Reviews :", neutral_count)
print("\nSentiment Analysis Completed Successfully!")
